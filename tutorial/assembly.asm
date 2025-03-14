; Bytes
SYS_WRITE = 1
STDOUT_FILENO = 1

# Printing
.data
buffer: .string "Hello, World!\n"
bufferLen = . - buffer

.text
mov $SYS_WRITE, %eax
mov $STDOUT_FILENO, %edi
mov $buffer, %esi
mov $bufferLen, %edx
syscall

# Looping
.data
digit: .byte   '0', '\n'

.text
mov $10, %bl
numberLoop:
    mov $SYS_WRITE, %eax
    mov $STDOUT_FILENO, %edi
    mov $digit, %esi
    mov $2, %edx
    syscall

    incb (%rsi)
    dec %bl
    jnz numberLoop

# Accessing arguments
pop %rbx
pop %rax

argLoop:
    dec %rbx
    jz endArgLoop

    pop %rsi
    mov %rsi, %rdi

    mov $-1, %ecx
    xor %al, %al
    repnz scasb

    not %ecx
    movb $'\n', -1(%rsi, %rcx)

    mov %ecx, %edx
    mov $SYS_WRITE, %eax
    mov $STDOUT_FILENO, %edi
    syscall

    jmp argLoop
endArgLoop:
; --
; Chars

