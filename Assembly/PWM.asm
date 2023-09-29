# 2018

.include "C:\VMLAB\include\m8def.inc"

.def  temp  = r16
.def  feet  = r17
.def  delay = r18

reset:
   rjmp init

init:
   ldi temp, (1<<ADEN)
   out ADCSR, temp
   ldi temp, (0<<REFS1) | (1<<REFS0) | (1<<ADLAR) | (1<<MUX2) | (1<<MUX1)
   out ADMUX, temp

   ldi temp, (1<<PB0)
   out DDRB, temp 

   ldi temp, high (RAMEND)
   out SPH, temp
   ldi temp, low (RAMEND)
   out SPL, temp

main:
   call convert
   clr delay
   sub delay, feet
   inc feet

   ldi temp, (0<<PB0)
   out PORTB, temp

   mov temp, delay
   call sleep

   ldi temp, (1<<PB0)
   out PORTB, temp

   mov temp, feet
   call sleep
rjmp main


sleep:
   cycle: dec temp
   brne cycle
ret


convert:
	sbi ADCSR, ADSC
	sbis ADCSR , ADIF
	rjmp PC-1
	in feet, ADCH
ret