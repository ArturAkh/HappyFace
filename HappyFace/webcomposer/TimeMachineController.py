import sys, os, popen2

class TimeMachineController(object):
	
    def __init__(self):

	self.output = """	
	<div class="HappyTitleBar">
	    <div class="HappyTitleBarElement"><table border="0" class="HappyTitleBarElementTable"><tr><td colspan="2" style="color:#FF9900;vertical-align:top;text-align:left;">The Happy Face</td></tr><tr><td style="color:#FF9900;vertical-align:middle;text-align:left;">Project <td style="font-size:0.7em;color:#FFFFFF;vertical-align:middle;text-align:right;">Rev.%s</td></tr></table></div>
	    <div class="HappyTitleBarElement"><table border="0" class="HappyTitleBarElementTable"><tr><td><?php printf($time_message); ?></td></tr></table></div>
	    <div class="HappyTitleBarElement"><table border="0" class="HappyTitleBarElementTable">
	    <tr><td>
	    <form action="<?php echo $PHP_SELF; ?>" method="get">
	    <div>
		 <input name="date" type="text" size="10" style="text-align:center;" value="<?php echo $date_string; ?>" />
		 - <input name="time" type="text" size="4" style="text-align:center;" value="<?php echo $time_string; ?>" />
  	         <button onclick="javascript:submit()" onfocus="this.blur()">Goto</button>
	    </div></form>
	    </td><td>
	    <form action="<?php echo $PHP_SELF; ?>" method="get">
	    <div>
  	         <button onclick="javascript:submit()" onfocus="this.blur()">&lt;--</button>
	    </div>
	    </form>
	    </td><td>
	    <form action="<?php echo $PHP_SELF; ?>" method="get">
	    <div>
  	         <button onclick="javascript:submit()" onfocus="this.blur()">--&gt;</button>
	    </div>
	    </form>	   
	    </td><td>
	    <form action="<?php reset_time(); echo $PHP_SELF; ?>" method="get">
	    <div>
		 <button onclick="javascript:document.getElementById('ReloadForm').submit()" onfocus="this.blur()">Reset</button>
	    </div>
	    </form>
            </td><td>
	    <?php printf($time_error_message); ?></td></tr></table></div>
	</div>
	""" % popen2.popen2('svnversion %s' % "../")[0].read().strip()
