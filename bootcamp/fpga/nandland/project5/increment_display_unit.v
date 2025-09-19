module increment_display_unit (
    input     i_Clk,
    input     i_Switch_Increment,
    input     i_Switch_Reset,
    output    o_Segment_A,
    output    o_Segment_B,
    output    o_Segment_C,
    output    o_Segment_D,
    output    o_Segment_E,
    output    o_Segment_F,
    output    o_Segment_G
);

// Internal signals
reg r_switch_increment = 1'b0;
reg r_switch_reset = 1'b0;
wire internal_switch_increment, internal_switch_reset;
reg [3:0] r_count = 4'b0000;
reg [6:0] r_seg;

// Instantiate debounce modules
debounce d_increment (.i_Clk(i_Clk), .i_switch(i_Switch_Increment), .o_switch(internal_switch_increment));
debounce d_reset (.i_Clk(i_Clk), .i_switch(i_Switch_Reset), .o_switch(internal_switch_reset));

// Instantiate display decoder
display_decode display (.i_hex(r_count), .o_seg(r_seg));

// Counter logic
always @ (posedge i_Clk) begin
    r_switch_increment <= internal_switch_increment;
    r_switch_reset <= internal_switch_reset;
    
    if (r_switch_reset == 1'b0 && internal_switch_reset == 1'b1) begin
        r_count <= 4'b0000;
    end
    else begin 
        if (r_switch_increment == 1'b0 && internal_switch_increment == 1'b1) begin
            if (r_count == 4'hF) begin
                r_count <= 4'b0000;
            end else begin
                r_count <= r_count + 1;
            end
        end
    end
end

// Output assignments (inverted for common cathode display)
assign o_Segment_A = ~r_seg[6];
assign o_Segment_B = ~r_seg[5];
assign o_Segment_C = ~r_seg[4];
assign o_Segment_D = ~r_seg[3];
assign o_Segment_E = ~r_seg[2];
assign o_Segment_F = ~r_seg[1];
assign o_Segment_G = ~r_seg[0];

endmodule
