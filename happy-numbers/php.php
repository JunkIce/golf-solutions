// Bytes
function utf8_ord($char) {
    $bytes = array_map('ord', str_split($char));
    if ($bytes[0] < 128) return $bytes[0];
    if ($bytes[0] < 224) return ($bytes[0] - 192) * 64 + ($bytes[1] - 128);
    if ($bytes[0] < 240) return ($bytes[0] - 224) * 4096 + ($bytes[1] - 128) * 64 + ($bytes[2] -128);
    return ($bytes[0] - 240) * 262144 + ($bytes[1] - 128) * 4096 + ($bytes[2] - 128) * 64 + ($bytes[3] - 128);
}

foreach(preg_split('//u', '¢¨«®´¸½ÀÁÍÒåçðó÷üÿĂąĈĎĢģĦĬňőŝşšŢ', -1, PREG_SPLIT_NO_EMPTY) as $n)echo utf8_ord($n) - 161,"\n";
// --
// Chars

function utf8_ord($char) {
    $bytes = array_map('ord', str_split($char));
    if ($bytes[0] < 128) return $bytes[0];
    if ($bytes[0] < 224) return ($bytes[0] - 192) * 64 + ($bytes[1] - 128);
    if ($bytes[0] < 240) return ($bytes[0] - 224) * 4096 + ($bytes[1] - 128) * 64 + ($bytes[2] -128);
    return ($bytes[0] - 240) * 262144 + ($bytes[1] - 128) * 4096 + ($bytes[2] - 128) * 64 + ($bytes[3] - 128);
}

foreach(preg_split('//u', '¢¨«®´¸½ÀÁÍÒåçðó÷üÿĂąĈĎĢģĦĬňőŝşšŢ', -1, PREG_SPLIT_NO_EMPTY) as $n)echo utf8_ord($n) - 161,"\n";

