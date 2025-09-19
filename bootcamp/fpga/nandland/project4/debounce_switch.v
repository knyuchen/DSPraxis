module debounce_switch (
    input     i_Clk,
    input     i_Switch_1,
    output    o_LED_1
);

reg r_switch_1 = 1'b0;
reg r_LED_1 = 1'b0;
wire internal_switch;
debounce d1 (.i_Clk(i_Clk), .i_switch(i_Switch_1), .o_switch(internal_switch));

always @ (posedge i_Clk) begin
   r_switch_1 <= internal_switch;
   if (r_switch_1 == 1'b0 && internal_switch == 1'b1) begin
       r_LED_1 <= ~r_LED_1;
   end
end

assign o_LED_1 = r_LED_1;

endmodule