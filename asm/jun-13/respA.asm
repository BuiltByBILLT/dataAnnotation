DATA SEGMENT
BIN db 0h, 11h, 0h, 10h, 11h, 10h, 01h, 10h, 11h, 0h
DATA_LEN EQU $-BIN  ; Calculate the length of the BIN array
DATA ENDS

CODE SEGMENT
    ASSUME CS:CODE
    ASSUME DS:DATA
START:
    MOV AX, DATA
    MOV DS, AX
    MOV SI, offset BIN  ; Use SI as the source index
    MOV CX, DATA_LEN / 2 ; Initialize loop counter to process pairs of bytes

LOOP_START:
    MOV AX, [SI]
    ADD SI, 2
    CALL bcd
    MOV BH, BL   ; Store the first BCD result in BH
    MOV CL, 4h
    SHL BH, CL   ; Shift left to make space for the second BCD result

    MOV AX, [SI]
    ADD SI, 2
    CALL bcd
    OR BH, BL    ; Combine the two BCD results
    MOV AL, BH
    CALL printl

    DEC CX          ; Decrement CX
    JCXZ END_LOOP   ; Jump to END_LOOP if CX is zero

    JMP LOOP_START  ; Continue looping

END_LOOP:

    MOV AH, 4CH
    INT 21H

bcd proc near
    push ax
    push cx
    xor bl, bl
    mov cx, 4h

lop:
    push cx
    mov cx, 4h
    rol ax, cl
    mov ch, al
    and ch, 01h
    add bl, ch
    shl bl, 1
    pop cx
    loop lop

    pop cx
    pop ax
    ret
bcd endp

printl PROC NEAR
    PUSH AX
    PUSH BX
    PUSH DX

    MOV CL, 4
    MOV BX, AX
    ROR AL, CL
    AND AL, 0Fh
    ADD AL, 30h
    CMP AL, 58
    JB p1
    ADD AL, 7
p1:
    MOV DL, AL
    MOV AH, 02h
    INT 21H

    MOV AL, BL
    AND AL, 0FH
    ADD AL, 30h
    CMP AL, 58
    JB p2
    ADD AL, 7
p2:
    MOV DL, AL
    INT 21H

    POP DX
    POP BX
    POP AX
    RET
printl ENDP

CODE ENDS
END START