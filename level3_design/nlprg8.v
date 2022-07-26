module DIG_D_FF_AS_1bit
#(
    parameter Default = 0
)
(
   input Set,
   input D,
   input C,
   input Clr,
   output Q,
   output \~Q
);
    reg state;

    assign Q = state;
    assign \~Q  = ~state;

    always @ (posedge C or posedge Clr or posedge Set)
    begin
        if (Set)
            state <= 1'b1;
        else if (Clr)
            state <= 'h0;
        else
            state <= D;
    end

    initial begin
        state = Default;
    end
endmodule

module nlprg3 (
  input clk,
  input rst,
  output [2:0] o
);
  wire o1;
  wire s0;
  wire o0;
  wire o2;
  wire s1;
  DIG_D_FF_AS_1bit #(
    .Default(0)
  )
  DIG_D_FF_AS_1bit_i0 (
    .Set( 1'b0 ),
    .D( s0 ),
    .C( clk ),
    .Clr( rst ),
    .Q( o0 )
  );
  DIG_D_FF_AS_1bit #(
    .Default(0)
  )
  DIG_D_FF_AS_1bit_i1 (
    .Set( 1'b0 ),
    .D( o1 ),
    .C( clk ),
    .Clr( rst ),
    .Q( o2 )
  );
  DIG_D_FF_AS_1bit #(
    .Default(0)
  )
  DIG_D_FF_AS_1bit_i2 (
    .Set( 1'b0 ),
    .D( s1 ),
    .C( clk ),
    .Clr( rst ),
    .Q( o1 )
  );
  assign s0 = ~ ((o1 ^ o2) ^ o1);
  assign s1 = (~ (o1 ^ o0) ^ ~ (o2 | o1));
  assign o[0] = o1;
  assign o[1] = o1;
  assign o[2] = o2;
endmodule
