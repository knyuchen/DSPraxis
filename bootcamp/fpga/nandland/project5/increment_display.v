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

// Instantiate first display unit (switches 1&2)
increment_display_unit unit1 (
    .i_Clk(i_Clk),
    .i_Switch_Increment(i_Switch_1),
    .i_Switch_Reset(i_Switch_2),
    .o_Segment_A(o_Segment1_A),
    .o_Segment_B(o_Segment1_B),
    .o_Segment_C(o_Segment1_C),
    .o_Segment_D(o_Segment1_D),
    .o_Segment_E(o_Segment1_E),
    .o_Segment_F(o_Segment1_F),
    .o_Segment_G(o_Segment1_G)
);

// Instantiate second display unit (switches 3&4)
increment_display_unit unit2 (
    .i_Clk(i_Clk),
    .i_Switch_Increment(i_Switch_3),
    .i_Switch_Reset(i_Switch_4),
    .o_Segment_A(o_Segment2_A),
    .o_Segment_B(o_Segment2_B),
    .o_Segment_C(o_Segment2_C),
    .o_Segment_D(o_Segment2_D),
    .o_Segment_E(o_Segment2_E),
    .o_Segment_F(o_Segment2_F),
    .o_Segment_G(o_Segment2_G)
);
endmodule