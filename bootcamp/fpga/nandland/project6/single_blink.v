module single_blink #(parameter DELAY_TIME = 1000000) (
    input i_Clk,
    input i_Switch,
    output  o_LED
);
wire debounced_set, debounced_switch;
reg debounced_switch_r = 0;

debounce debounce_button_inst(.i_Clk(i_Clk), .i_switch(i_Switch), .o_switch(debounced_switch));
always @(posedge i_Clk) begin
    debounced_switch_r <= debounced_switch;
end
assign debounced_set = debounced_switch_r == 0 && debounced_switch == 1;
reg [31:0] delay_time = 0;
reg led_reg = 0;
reg on = 0;
always @(posedge i_Clk) begin
    if (on) begin
        if (debounced_set) begin
            on <= 0;
        end
        else begin
            if (delay_time < DELAY_TIME) begin
                delay_time <= delay_time + 1;
            end
            else begin
                led_reg <= ~led_reg;
                delay_time <= 0;
            end
        end
        
    end
    else begin
        led_reg <= 0;
        delay_time <= 0;
        if (debounced_set) begin
            on <= 1;
        end
    end
end
assign o_LED = led_reg;
endmodule