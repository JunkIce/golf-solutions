# Bytes
echo '¢¨«®´¸½ÀÁÍÒåçðó÷üÿĂąĈĎĢģĦĬňőŝşšŢ'|while IFS= read -rn1 c;do [[ $c ]]&&printf '%d\n' "'$c";done|while read n;do echo $((n-161));done
# --
# Chars
echo '¢¨«®´¸½ÀÁÍÒåçðó÷üÿĂąĈĎĢģĦĬňőŝşšŢ'|while IFS= read -rn1 c;do [[ $c ]]&&printf '%d\n' "'$c";done|while read n;do echo $((n-161));done
