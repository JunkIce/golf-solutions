; Bytes
.global _start;_start:mov $p,%rsi;mov $1,%rax;mov $1,%rdi;mov $255,%rdx;syscall;mov $q,%rsi;mov $1,%rax;mov $1,%rdx;syscall;mov $p,%rsi;mov $1,%rax;mov $255,%rdx;syscall;mov $q,%rsi;mov $1,%rax;mov $1,%rdx;syscall;mov $60,%rax;syscall;q:.byte 34;p:.ascii ".global _start;_start:mov $p,%rsi;mov $1,%rax;mov $1,%rdi;mov $255,%rdx;syscall;mov $q,%rsi;mov $1,%rax;mov $1,%rdx;syscall;mov $p,%rsi;mov $1,%rax;mov $255,%rdx;syscall;mov $q,%rsi;mov $1,%rax;mov $1,%rdx;syscall;mov $60,%rax;syscall;q:.byte 34;p:.ascii "
; --
; Chars

