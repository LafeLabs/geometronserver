<?php
//this pairs with buttons.html and byteaction.py(obvoiusly)
   $str = $_POST["byte"];
   $file = fopen("byte.txt","w");
   fwrite($file,$str);
   fclose($file);
   exec ("./byteaction.py");
?>