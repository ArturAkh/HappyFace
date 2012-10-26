#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2012 Institut für Experimentelle Kernphysik - Karlsruher Institut für Technologie
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

import os,sys


cur_path = os.path.dirname(os.path.abspath(__file__)) if __file__ else os.getcwd()
if __name__ != '__main__' and os.path.abspath(cur_path) != os.getcwd():
    # unfortunately we need this rather hacky path change
    # because mod_wsgi for some reason does not want to
    # set PYTHONPATH as we want it or the interpreted
    # doesn't read it, idk
    os.chdir(os.path.dirname(cur_path))
    sys.path.append(os.path.dirname(cur_path))

import hf, cherrypy, logging
import ConfigParser
import atexit

logger = logging.getLogger(__name__)


hf.hf_dir = cur_path
hf.configtools.readConfigurationAndEnv()
hf.configtools.setupLogging('render_logging_cfg')
cp_config = {}
for section in hf.config.sections():
    if section == "global" or section.startswith("/"):
        config = dict(hf.config.items(section))
        for key,val in config.iteritems():
            try:
                config[key] = eval(val)
            except ValueError:
                pass
        cp_config[section] = config
cherrypy.config.update(cp_config)

hf.module.importModuleClasses()
hf.auth.init()

hf.database.connect(implicit_execution = True)

if __name__ == '__main__':
    cherrypy.quickstart(root=hf.RootDispatcher(), script_name=hf.config.get("paths", "happyface_url"), config=cp_config)
    hf.database.disconnect()
else:
    cherrypy.config.update({'environment': 'embedded'})
    if cherrypy.__version__.startswith('3.0') and cherrypy.engine.state == 0:
        cherrypy.engine.start(blocking=False)
        atexit.register(cherrypy.engine.stop)
    application = cherrypy.Application(root=hf.RootDispatcher(), script_name=hf.config.get("paths", "happyface_url"), config=cp_config)
