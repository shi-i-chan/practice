# 2018

.include "C:\VMLAB\include\m8def.inc"
.def temp = R16
.def razr1 = R17
.def razr2 = R18
.def razr3 = R19

Reset:
	rjmp Init
	
Init:
   ldi temp,LOW(RAMEND)
   out SPL, temp
   ldi temp, HIGH(RAMEND)
   out SPH, temp

	ldi temp, 0xFF
	out DDRB, temp
	out PORTB, temp
	ldi temp, (1<<PD0)
	out DDRD, temp
	out PORTD, temp
	
Main:
	ldi temp, 0b11000000
	out PORTB, temp
	rcall Delay
	
	ldi temp, 0b11111001
	out PORTB, temp
	rcall Delay
	
	ldi temp, 0b10100100
	out PORTB,temp
 	rcall Delay
 	
	ldi temp, 0b10110000
	out PORTB, temp
	rcall Delay
	
	ldi temp, 0b10011001
	out PORTB, temp
	rcall Delay
	
	ldi temp, 0b10010010
	out PORTB, temp
	rcall Delay
	
	ldi temp, 0b10000010
	out PORTB, temp
	rcall Delay
	
	ldi temp, 0b11111000
	out PORTB, temp
	rcall Delay
	
	ldi temp, 0b10000000
	out PORTB, temp
	rcall Delay
	
	ldi temp, 0b10010000
	out PORTB, temp
	rcall Delay
	
rjmp Main

Delay:
	ldi razr1, 255
	ldi razr2, 255
	ldi razr3, 2
	rjmp PDelay
ret	

PDelay:
	dec razr1
	brne PDelay
	
	dec razr2
	brne PDelay
	
	dec razr3
	brne PDelay
ret