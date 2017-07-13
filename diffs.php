<?php
$diffstack = $_POST["diffstack"];
$diffarray = explode("<p>", $diffstack);
$cubetxt = "";
for ($index = 0; $index < count($diffarray); $index++) {
    $cubetxt .= "\n";
    $cube = fopen($diffarray[$index]);
    $cubetxt .= fread($cube);
    fclose($file);
 //   $cubetxt .= file_get_contents($diffarray[$index]);
}
$file = fopen("cube.txt","w");
fwrite($file,$cubetxt);
fclose($file);
?>