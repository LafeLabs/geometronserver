<?php
//
   $str = $_POST["data"];
   $file = fopen("outfeed.txt","w");
   fwrite($file,$str);
   fclose($file);
?>