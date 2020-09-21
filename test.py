import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge


@cocotb.test()
async def test(dut):
    clock = Clock(dut.clk, 10, units="us")
    cocotb.fork(clock.start())
    
    # test fails with this error:
    # AttributeError: top contains no object named genblk1
    # change False to True below to make the test pass
    if False:
        for thing in dut:
            pass

    await RisingEdge(dut.clk)
    print(dut.genblk1[0].sub_inst.clk.value)
