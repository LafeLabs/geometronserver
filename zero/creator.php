<?php
$basecube = file_get_contents("origin.txt");
$basecubearray = explode("\n", $basecube);
$subarray = explode(":",$basecubearray[0]);
$indexhtml = byteCode2string($subarray[1]);
$indexhtml .= "\n";
$indexhtml .= $basecube;
$indexhtml .= "\n";
$indexhtml .= file_get_contents('root.txt');
$indexhtml .= "\n";
$indexhtml .= file_get_contents('font.txt');
$indexhtml .= "\n";
$indexhtml .= file_get_contents('shapes.txt');
$indexhtml .= "\n";
$indexhtml .= file_get_contents('geometron.txt');
$indexhtml .= "\n";
$indexhtml .= file_get_contents('generators.txt');
$indexhtml .= "\n";
$indexhtml .= file_get_contents('scrolls.txt');
$indexhtml .= "\n";
for($index = 1;$index < count($basecubearray);$index++){    
    $subarray = explode(":",$basecubearray[$index]);
    $indexhtml .= byteCode2string($subarray[1]);
}
$file = fopen("index.html","w");
fwrite($file,$indexhtml);
fclose($file);

##############
function byteCode2string($inputbytecode) {
    $bytecodearray = explode(",", $inputbytecode);
    $outputstring = " ";
    for ($index = 0; $index < count($bytecodearray); $index++) {
        if(strlen($bytecodearray[$index]) > 1){
            $outputstring .= chr(octdec($bytecodearray[$index]));
        }
    }
    return $outputstring;
}
function string2byteCode($inputstring){
    $outputcode = "";
    for( $index = 0; $index < strlen($inputstring);$index++){
        $outputcode .= "0".decoct(ord($inputstring[$index])).",";
    }
    return $outputcode;
}
?>