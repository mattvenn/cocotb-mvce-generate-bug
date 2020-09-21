import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge


@cocotb.test()
async def test(dut):
    clock = Clock(dut.clk, 10, units="us")
    cocotb.fork(clock.start())
    
    import ipdb; ipdb.set_trace() 
    # in the ipdb session type dut.genblk1, then press tab, then c to continue, the test will complete.
    # If don't press tab, will fail with message: 'AttributeError: top contains no object named genblk1'
    # tested with iverilog 10.3
    await RisingEdge(dut.clk)
    print(dut.genblk1[0].sub_inst.clk.value)
