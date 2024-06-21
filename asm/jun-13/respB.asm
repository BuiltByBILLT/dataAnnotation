DATA SEGMENT
BIN db 0h, 11h, 0h, 10h, 11h, 10h, 01h, 10h, 11h, 0h
DATA ENDS

CODE SEGMENT
ASSUME CS:CODE, DS:DATA

START:
    ; Setup data segment
    MOV AX, DATA
    MOV DS, AX
    
    ; Initialize DI to point at the array
    LEA DI, BIN
    
    ; Loop through the array and print each byte in hexadecimal
    MOV CX, 10  ; Loop 10 times (for 10 bytes)
PRINT_LOOP:
    MOV AL, [DI]
    CALL PRINT_HEX
    INC DI
    LOOP PRINT_LOOP  ; Loop until CX is 0

    ; Exit program
    MOV AH, 4CH
    INT 21H

; Procedure to Print Hexadecimal
PRINT_HEX PROC NEAR
    PUSH AX
    PUSH BX
    PUSH DX

    MOV BX, AX
    MOV CL, 4
    ; Print the higher nibble
    ROR AL, CL
    AND AL, 0Fh
    CALL PRINT_DIGIT
    
    ; Print the lower nibble
    MOV AL, BL
    AND AL, 0Fh
    CALL PRINT_DIGIT

    POP DX
    POP BX
    POP AX
    RET
PRINT_HEX ENDP

; Procedure to Print a Single Hex Digit
PRINT_DIGIT PROC NEAR
    ADD AL, 30h
    CMP AL, 39h
    JBE DIGIT_OK
    ADD AL, 7
DIGIT_OK:
    MOV DL, AL
    MOV AH, 02h
    INT 21H
    RET
PRINT_DIGIT ENDP

CODE ENDS
END START