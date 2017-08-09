<?php
//https://pastebin.com/raw/XP6n11gX
   $str = $_POST["data"];
   $file = fopen("infeed.txt","w");
   fwrite($file,$str);
   fclose($file);
?>