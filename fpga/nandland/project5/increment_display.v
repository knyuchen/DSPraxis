module increment_display (
    input     i_Clk,
    input     i_Switch_1,
    input     i_Switch_2,
    input     i_Switch_3,
    input     i_Switch_4,
    output    o_Segment1_A,
    output    o_Segment1_B,
    output    o_Segment1_C,
    output    o_Segment1_D,
    output    o_Segment1_E,
    output    o_Segment1_F,
    output    o_Segment1_G,
    output    o_Segment2_A,
    output    o_Segment2_B,
    output    o_Segment2_C,
    output    o_Segment2_D,
    output    o_Segment2_E,
    output    o_Segment2_F,
    output    o_Segment2_G
);

reg r_switch_1 = 1'b0;
reg r_switch_2 = 1'b0;
reg r_switch_3 = 1'b0;
reg r_switch_4 = 1'b0;
wire internal_switch_1, internal_switch_2;
wire internal_switch_3, internal_switch_4;
reg [3:0] r_count_1 = 4'b0000;
reg [3:0] r_count_2 = 4'b0000;

reg [6:0] r_seg_1;
reg [6:0] r_seg_2;
debounce d1 (.i_Clk(i_Clk), .i_switch(i_Switch_1), .o_switch(internal_switch_1));
debounce d2 (.i_Clk(i_Clk), .i_switch(i_Switch_2), .o_switch(internal_switch_2));
display_decode display1 (.i_hex(r_count_1), .o_seg(r_seg_1));
debounce d3 (.i_Clk(i_Clk), .i_switch(i_Switch_3), .o_switch(internal_switch_3));
debounce d4 (.i_Clk(i_Clk), .i_switch(i_Switch_4), .o_switch(internal_switch_4));
display_decode display2 (.i_hex(r_count_2), .o_seg(r_seg_2));
always @ (posedge i_Clk) begin
   r_switch_1 <= internal_switch_1;
   r_switch_2 <= internal_switch_2;
   if (r_switch_2 == 1'b0 && internal_switch_2 == 1'b1) begin
    r_count_1 <= 4'b0000;
   end
   else begin 
   if (r_switch_1 == 1'b0 && internal_switch_1 == 1'b1) begin
    if (r_count_1 == 4'hF) begin
       r_count_1 <= 4'b0000;
    end else begin
       r_count_1 <= r_count_1 + 1;
    end
   end
end
end
always @ (posedge i_Clk) begin
   r_switch_3 <= internal_switch_3;
   r_switch_4 <= internal_switch_4;
   if (r_switch_4 == 1'b0 && internal_switch_4 == 1'b1) begin
    r_count_2 <= 4'b0000;
   end
   else begin 
   if (r_switch_3 == 1'b0 && internal_switch_3 == 1'b1) begin
    if (r_count_2 == 4'hF) begin
       r_count_2 <= 4'b0000;
    end else begin
       r_count_2 <= r_count_2 + 1;
    end
   end
end
end

assign o_Segment1_A = ~r_seg_1[6];
assign o_Segment1_B = ~r_seg_1[5];
assign o_Segment1_C = ~r_seg_1[4];
assign o_Segment1_D = ~r_seg_1[3];
assign o_Segment1_E = ~r_seg_1[2];
assign o_Segment1_F = ~r_seg_1[1];
assign o_Segment1_G = ~r_seg_1[0];
assign o_Segment2_A = ~r_seg_2[6];
assign o_Segment2_B = ~r_seg_2[5];
assign o_Segment2_C = ~r_seg_2[4];
assign o_Segment2_D = ~r_seg_2[3];
assign o_Segment2_E = ~r_seg_2[2];
assign o_Segment2_F = ~r_seg_2[1];
assign o_Segment2_G = ~r_seg_2[0];
endmodule