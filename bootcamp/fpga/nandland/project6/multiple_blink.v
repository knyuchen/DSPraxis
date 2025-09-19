module multiple_blink (
    input i_Clk,
    input i_Switch_1,
    input i_Switch_2,
    input i_Switch_3,
    input i_Switch_4,
    output reg o_LED_1,
    output reg o_LED_2,
    output reg o_LED_3,
    output reg o_LED_4
);
single_blink  #(.DELAY_TIME(4000000)) bl1 (.i_Clk(i_Clk), .i_Switch(i_Switch_1), .o_LED(o_LED_1));
single_blink #(.DELAY_TIME(8000000)) bl2 (.i_Clk(i_Clk), .i_Switch(i_Switch_2), .o_LED(o_LED_2));
single_blink #(.DELAY_TIME(2000000)) bl3 (.i_Clk(i_Clk), .i_Switch(i_Switch_3), .o_LED(o_LED_3));
single_blink #(.DELAY_TIME(16000000)) bl4 (.i_Clk(i_Clk), .i_Switch(i_Switch_4), .o_LED(o_LED_4));
endmodule