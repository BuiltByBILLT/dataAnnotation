DATA  SEGMENT
BIN db 0h, 11h, 0h, 10h, 11h, 10h, 01h, 10h, 11h, 0h;
DATA ENDS
CODE SEGMENT
    ASSUME  CS:CODE
    Assume  DS:DATA
START:
    MOV  AX, DATA
    MOV  DS, AX
    MOV  DI, offset BIN
    xor  ax, ax
    mov  [di + 10], ax  ;??
    mov  ax, [di]
    add  di, 2
    call bcd
    mov  bh, bl
    mov  cl, 4h
    shl  bh, cl
    mov  ax, [di]
    add  di, 2
    call bcd
    or   bh, bl
    mov  al, bh
    call printl
    mov  ax, [di]
    add  di, 2
    call bcd
    mov  al, bl
    call printl

    MOV  AH, 4CH
    INT  21H 

bcd proc near ;(ax, &bl)
    push ax
    push cx
    xor  bl, bl
    mov  cx, 4h
lop:
    push cx
    mov  cx, 4h
    rol  ax, cl
    mov  ch, al
    and  ch, 01h
    add  bl, ch
    shl  bl, 1
    and  ax, ax
    pop  cx
    loop lop
    pop  cx
    pop  ax
    ret
bcd endp
printl  PROC NEAR ;(AL) -> void
        PUSH AX
        PUSH BX
        PUSH DX  ;????
        MOV  CL, 4
        MOV BX, AX
        ROR aL, CL  ;?????
        and al, 0Fh
        add al, 30h
        cmp al, 58
        jb  p1
        add al, 7
p1:
        mov dl, al
        MOV AH, 02h
        INT 21H
        mov aL, BL
        and aL, 0FH
        add aL, 30h
        cmp al, 58
        jb p2
        add al, 7
p2:
        mov dl, al
        INT 21H
        POP DX  ;????
        POP BX
        POP AX
        RET
printl  ENDP
CODE    ENDS
    END START