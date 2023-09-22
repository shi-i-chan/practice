module PWM1(
	number,
	clk,
	pwm1,
	pwm2);
	
	input[7:0] number;
	input clk;
	output pwm1, pwm2;
	
	reg[7:0] counter;
	reg pwm1;
	reg pwm2;
	
	always@(posedge clk)
	begin
	if(counter <= number)
		pwm1 = 1'b1;
	else
		pwm1 = 1'b0;
	
	if(counter <= 8'b11111111 - number)
		pwm2 = 1'b0;
	else
		pwm2 = 1'b1;	
	
	counter = counter + 8'b1;
	end
	
endmodule