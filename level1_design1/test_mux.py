# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer
import random

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""
    for i in range(15):
        
            in0 = random.randint(0, 3)
            in1 = random.randint(0, 3)
            in2 = random.randint(0, 3)
            in3 = random.randint(0, 3)
            in4 = random.randint(0, 3)
            in5 = random.randint(0, 3)
            in6 = random.randint(0, 3)
            in7 = random.randint(0, 3)
            in8 = random.randint(0, 3)
            in9 = random.randint(0, 3)
            in10 = random.randint(0, 3)
            in11 = random.randint(0, 3)
            in12 = random.randint(0, 3)
            in13= random.randint(0, 3)
            in14= random.randint(0, 3)
            in15= random.randint(0, 3)
            

            input = [in0, in1, in2, in3, in4, in5, in6, in7, in8, 
            in9, in10, in11, in12, in13, in14, in15]

            dut.inp0.value = in0
            dut.inp1.value = in1
            dut.inp2.value = in2
            dut.inp3.value = in3
            dut.inp4.value = in4
            dut.inp5.value = in5
            dut.inp6.value = in6
            dut.inp7.value = in7
            dut.inp8.value = in8
            dut.inp9.value = in9
            dut.inp10.value = in10
            dut.inp11.value = in11
            dut.inp12.value = in12
            dut.inp13.value = in13
            dut.inp14.value = in14
            dut.inp15.value = in15
            
            dut.sel.value = i

            await Timer(2, units='ns')

            dut._log.info(f'Selection={dut.sel.value} model={(input[i])} DUT={(dut.out.value)}')
            #cocotb.log.info('##### CTB: Develop your test here ########')
            assert dut.out.value == input[i], f"Test failed with: Selction {dut.sel.value} and  output {dut.out.value} but required output should be {input[i]}"