# See LICENSE.vyoma for details

# SPDX-License-Identifier: CC0-1.0

import os
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge

@cocotb.test()
async def test_seq_bug1(dut):
    """Test for seq detection """

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)  
    dut.reset.value = 0
    await FallingEdge(dut.clk)

    dut.current_state=1

    dut.inp_bit.value=1
    await FallingEdge(dut.clk)

    dut._log.info(f"DUT current state :{dut.current_state.value} DUT Next state :{dut.next_state.value}")
    assert dut.current_state.value==dut.SEQ_1.value,f"Test fail with required current state={dut.SEQ_1.value} but abtained is{dut.current_state.value}"

    

@cocotb.test()
async def test_seq_bug2(dut):
    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)  
    dut.reset.value = 0
    await FallingEdge(dut.clk)

    dut.current_state=3

    dut.inp_bit.value=0
    await FallingEdge(dut.clk)

    dut._log.info(f"sequence seen={dut. seq_seen} DUT current state :{dut.current_state.value} DUT Next state :{dut.next_state.value}")
    assert dut.current_state.value==(dut.SEQ_10.value),f"Test fail with required current state={dut.SEQ_10.value} but abtained is{dut.current_state.value}"

