module debounce (
    input     i_Clk,
    input     i_switch,
    output    o_switch
);
parameter LIMIT = 250000;
reg [17:0] r_count = 0;
reg r_debounced = 1'b0;


always @ (posedge i_Clk) begin
    if (r_debounced != i_switch && r_count != LIMIT) begin
        r_count <= r_count + 1;
    end else if (r_count == LIMIT) begin
        r_debounced <= i_switch;
        r_count <= 0;
    end else begin
        r_count <= 0;
    end
end

assign o_switch = r_debounced;

endmodule