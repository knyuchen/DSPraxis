module Switches_LUT (
    input  i_Switch_1, i_Switch_2, i_Switch_3, i_Switch_4,
    output o_LED_1,   o_LED_2,   o_LED_3,   o_LED_4
);
    assign o_LED_1 = i_Switch_1 | i_Switch_2;
    assign o_LED_2 = i_Switch_2 & i_Switch_3;
    assign o_LED_3 = i_Switch_3 & ~i_Switch_1;
    assign o_LED_4 = i_Switch_4;
endmodule