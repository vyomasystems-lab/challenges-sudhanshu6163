import os
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge

@cocotb.test()
async def test_nlprg3(dut):

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.rst.value = 1
    await FallingEdge(dut.clk)  
    dut.rst.value = 0
    await FallingEdge(dut.clk)
    dut.rst.value = 1
    await FallingEdge(dut.clk)  
    dut.rst.value = 0
    await FallingEdge(dut.clk)

    # for i in range(2):

        
    o0 = 0b0
    o1 = 0b0
    o2 = 0b0
    
    s0=~ ((o1 ^ o2) ^ o1)
    s1= (~ (o1 ^ o0) ^ ~ (o2 | o1))
    await RisingEdge(dut.clk)

    
    dut._log.info(f' DUT={dut.o.value} s0={dut.s0.value} s1={dut.s1.value} o2={dut.o2.value} o1={dut.o1.value} o0={dut.o0.value}')
    assert dut.o.value==0b001,f'test fail with {dut.o.value} but it should be {0b001}'
   
        

