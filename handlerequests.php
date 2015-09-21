<?php
header('Access-Control-Allow-Origin: *');
exec('python dumpfacebookpagephotos.py. '.$_POST['ahead']." ".$_POST['pagename']);
?>