import sys, os, subprocess

from HTMLOutput import *

class TimeMachineController(HTMLOutput):

    def __init__(self, logo_image, theDocumentationURL):
	HTMLOutput.__init__(self, 2)

	rev = subprocess.Popen(['svnversion', '../'], 0, None, None, subprocess.PIPE).stdout.read().strip()

	output = []
	output.append(   '<div class="HappyTitleBar">')
	output.append(   ' <div class="HappyTitleBarElement">')
	output.append(   '  <table border="0" class="HappyTitleBarElementTable">')
	output.append(   '   <tr>')
	output.append(   '    <td>')
	output.append(   '     <img style="border:solid 1px #000;height:35px;" alt="" src="' + logo_image + '" />')
	output.append(   '    </td>')
	output.append(   '   </tr>')
	output.append(   '  </table>')
	output.append(   ' </div>')
	output.append(   ' <div class="HappyTitleBarElement">')
	output.append(   '  <table border="0" class="HappyTitleBarElementTable">')
	output.append(   '   <tr>')
	output.append(   '    <td colspan="2" style="color:#FF9900;vertical-align:top;text-align:left;">The Happy Face</td>')
	output.append(   '   </tr>')
	output.append(   '   <tr>')
	output.append(   '    <td style="color:#FF9900;vertical-align:middle;text-align:left;">Project</td>')
	output.append( """    <td style="font-size:0.7em;color:#FFFFFF;vertical-align:middle;text-align:right;">Rev.""" + rev + """</td>""")
	output.append(   '   </tr>')
	output.append(   '  </table>')
	output.append(   ' </div>')
	output.append(   ' <div class="HappyTitleBarElement">')
	output.append(   '  <table border="0" class="HappyTitleBarElementTable">')
	output.append(   '   <tr>')
	output.append( """    <td colspan="2"><a href="?action=getxml&amp;date=' . $date_string . '&amp;time=' . $time_string . '" onfocus="this.blur()"><img src="config/images/xml_icon.gif" width="34" height="13" alt="XML icon" style="border: none; vertical-align: middle;"/></a></td>""")
	output.append(   '   </tr>')
        output.append(   '   <tr>')
	output.append( """    <td><img src="' . $lock_icon . '" onmouseover="javascript:HappyCertInfo(\\\'over\\\');" onmouseout="javascript:HappyCertInfo(\\\'out\\\');" width="15" height="13" alt="Lock icon" style="border: none; vertical-align: middle;"/></td>""")
        output.append( """    <td><a href=" """ + theDocumentationURL + """ " onfocus="this.blur()"><img src="config/images/help_icon.gif" width="15" height="13" alt="Help icon" style="border: none; vertical-align: middle;"/></a></td>""")
        output.append(   '   </tr>')
 	output.append(   '  </table>')
	output.append(   ' </div>')
	output.append(   ' <div class="HappyTitleBarElement">')
	output.append(   '  <table border="0" class="HappyTitleBarElementTable">')
	output.append(   '   <tr>')
	output.append( """    <td><div style="text-align: left;">' . $date_message_short . '</div></td>""")
	output.append(   '   </tr>')
	output.append(   '   <tr>')
	output.append( """    <td><div style="text-align: center;">' . $time_message . '</div></td>""")
	output.append(   '   </tr>')
	output.append(   '  </table>')
	output.append(   ' </div>')
	output.append(   ' <div class="HappyTitleBarElement">')
	output.append( """  <form id="HistoForm1" class="HappyTitleBarForm" action="' . $_SERVER['PHP_SELF'] . '" method="get">""")
	output.append(   '   <table border="0" class="HappyTitleBarElementTable">')
	output.append(   '    <tr>')
	output.append(   '     <td>')
	output.append(   '      <div>')
	output.append( """       <button onclick="javascript:HappyHistoNav(\\\'back\\\',\\\'' . $timestamp . '\\\')" onfocus="this.blur()">&lt;--</button>""")
	output.append(   '      </div>')
	output.append(   '     </td>')
	output.append(   '     <td>')
	output.append(   '      <div>')
	output.append( """       <input type="text" id="HistoStep" name="s" size="5" style="text-align:center;" value="' . $histo_step . '" />""")
	output.append( """       <input type="hidden" id="HistoNavDate" name="date" value="' . $date_string . '" />""")
	output.append( """       <input type="hidden" id="HistoNavTime" name="time" value="' . $time_string . '" />""")
	output.append( """       <input type="hidden" id="HistoReloadTab1" name="t" value="' . $selectedTab . '" />""")
	output.append( """       <input type="hidden" id="HistoReloadMod1" name="m" value="' . $selectedMod . '" />""")
	output.append(   '       <input type="hidden" id="HistoReloadExpand1" name="expand" value="" />')
	output.append(   '      </div>')
	output.append(   '     </td>')
	output.append(   '     <td>')
	output.append(   '      <div>')
	output.append( """       <button onclick="javascript:HappyHistoNav(\\\'fwd\\\',\\\'' .$timestamp . '\\\')" onfocus="this.blur()">--&gt;</button>""")
	output.append(   '      </div>')
	output.append(   '     </td>')
	output.append(   '    </tr>')
	output.append(   '   </table>')
	output.append(   '  </form>')
	output.append(   ' </div>')
	output.append(   '')
	output.append(   ' <div class="HappyTitleBarElement">')
	output.append( """  <form id="HistoForm2" class="HappyTitleBarForm" action="' . $_SERVER['PHP_SELF'] . '" method="get">""")
	output.append(   '   <table border="0" class="HappyTitleBarElementTable">')
	output.append(   '    <tr>')
	output.append(   '     <td>')
	output.append(   '      <div>')
	output.append( """       <input name="date" type="text" size="10" style="text-align:center;" value="' . $date_string . '" />""")
	output.append(  '       -')
	output.append( """       <input name="time" type="text" size="5" style="text-align:center;" value="' . $time_string . '" />""")
	output.append( """       <input type="hidden" id="HistoReloadTab2" name="t" value="' . $selectedTab . '" />""")
	output.append( """       <input type="hidden" id="HistoReloadMod2" name="m" value="' . $selectedMod . '" />""")
	output.append(   '       <input type="hidden" id="HistoReloadExpand2" name="expand" value="" />')
	output.append(   '       <button onclick="javascript:submit()" onfocus="this.blur()">Goto</button>')
	output.append(   '      </div>')
	output.append(   '     </td>')
	output.append(   '    </tr>')
	output.append(   '   </table>')
	output.append(   '  </form>')
	output.append(   ' </div>')
	output.append(   ' <div class="HappyTitleBarElement">')
	output.append( """  <form class="HappyTitleBarForm" action="' . $_SERVER['PHP_SELF'] . '" method="get">""")
	output.append(   '   <table border="0" class="HappyTitleBarElementTable">')
	output.append(   '    <tr>')
	output.append(   '     <td>')
	output.append(   '      <div>')
	output.append( """       <button onclick="javascript:document.getElementById(\\\'ReloadForm\\\').submit()" onfocus="this.blur()">Reset</button>""")
	output.append(   '      </div>')
	output.append(   '     </td>')
	output.append(   '    </tr>')
	output.append(   '   </table>')
	output.append(   '  </form>')
	output.append(   ' </div>')

	error_msg = []
	error_msg.append(' <div class="HappyTitleBarElement">')
	error_msg.append('  <table border="0" class="HappyTitleBarElementTable">')
	error_msg.append('   <tr>')
	error_msg.append('    <td>')
	error_msg.append('     <div>')
	error_msg.append("      ' . $time_error_message . '")
	error_msg.append('     </div>')
	error_msg.append('    </td>')
	error_msg.append('   </tr>')
	error_msg.append('  </table>')
	error_msg.append(' </div>')

	end = []
	end.append(      '</div>')

	out = """<?php
	
	$ssl_client_verify = 'NONE';
	if (array_key_exists('SSL_CLIENT_VERIFY', $_SERVER)) { $ssl_client_verify = $_SERVER['SSL_CLIENT_VERIFY']; }
	if ( $ssl_client_verify == "SUCCESS") {
		$lock_icon = "config/images/lock_icon_on.gif";
		print('<div id="HappyCertInfoDiv">
			Used browser certificate for authentication:
			<br />
			<span style="color:#FF9900;">'.$_SERVER['SSL_CLIENT_S_DN'].'</span>
			<br /><br />
			Certificate authority:
			<br />
			<span style="color:#FF9900;">'.$_SERVER['SSL_CLIENT_I_DN'].'</span>
		       </div>');
	} else {
		$lock_icon = "config/images/lock_icon_off.gif";
		print('<div id="HappyCertInfoDiv">
			No browser authentication credentials found or non-https web access.
			<br />
			Using standard HappyFace display mode.
		       </div>');
	}

	print('""" + self.PHPArrayToString(output) + """');
	reset_time();

	if($time_error_message != "")
	    print('""" + self.PHPArrayToString(error_msg) + """');

	print('""" + self.PHPArrayToString(end) + """');

	?>"""

	self.output = out
