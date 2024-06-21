.model small
.stack 100h
.data
    hello_msg db 'Hello, World!$'
.code
main proc
    mov ax, @data
    mov ds, ax

    ; Print the hello message
    mov ah, 09h
    lea dx, hello_msg
    int 21h

    ; Exit program
    mov ah, 4Ch
    int 21h
main endp
end main
