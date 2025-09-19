module test_counter;

// Testbench signals
reg clk;
reg rst_n;
reg enable;
wire [7:0] count;

// Instantiate the counter module
counter dut (
    .clk(clk),
    .rst_n(rst_n),
    .enable(enable),
    .count(count)
);

// Clock generation
initial begin
    clk = 0;
    forever #5 clk = ~clk; // 10ns period (100MHz)
end

// Test stimulus
initial begin
    // Initialize signals
    rst_n = 0;
    enable = 0;
    
    // Apply reset
    #20 rst_n = 1;
    
    // Test with enable off (counter should not increment)
    #50;
    
    // Enable counter
    enable = 1;
    #100;
    
    // Disable counter
    enable = 0;
    #50;
    
    // Re-enable counter
    enable = 1;
    #50;
    
    // Test reset again
    rst_n = 0;
    #20 rst_n = 1;
    enable = 1;
    
    // Run for a bit more
    #100;
    
    $finish;
end

// VCD dump for GTKWave
initial begin
    $dumpfile("counter.vcd");
    $dumpvars(0, test_counter);
end

// Monitor output
initial begin
    $monitor("Time: %0t, rst_n: %b, enable: %b, count: %d", $time, rst_n, enable, count);
end


endmodule
