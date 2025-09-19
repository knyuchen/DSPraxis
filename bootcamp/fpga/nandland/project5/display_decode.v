module display_decode (
    input  wire [3:0] i_hex,
    output reg [6:0] o_seg
);

always @ (*) begin
    case (i_hex)
        4'h0: o_seg = 7'h7E;
        4'h1: o_seg = 7'h30;
        4'h2: o_seg = 7'h6D;
        4'h3: o_seg = 7'h79;
        4'h4: o_seg = 7'h33;
        4'h5: o_seg = 7'h5B;
        4'h6: o_seg = 7'h5F;
        4'h7: o_seg = 7'h70;
        4'h8: o_seg = 7'h7F;
        4'h9: o_seg = 7'h7B;
        4'hA: o_seg = 7'h77;
        4'hB: o_seg = 7'h1F;
        4'hC: o_seg = 7'h4E;
        4'hD: o_seg = 7'h3D;
        4'hE: o_seg = 7'h4F;
        4'hF: o_seg = 7'h47;
    endcase
end
endmodule