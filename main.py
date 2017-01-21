from memory import Memory
from debug import Debug
from cpu import Cpu
from rom import Rom
import sys

# configure gb at the startup
def init():
    # initialize the gb memory
    mem = Memory()

    #gb CPU
    cpugb = Cpu(mem)
    cpugb.debugRegs()

    # Debug
    debg = Debug()

    # reading bios
    with open("BIOS.gb", mode="rb") as bios:
        boot = bios.read()
    print("BIOS loaded!")

    #loading bios into gb memory ram (start at 0xC000)
    mem.load(boot, int("C000", 16))

init()

# verifying the argument
if (sys.argv[1]):
    # loading rom
    with open(sys.argv[1], mode="rb") as f:
        rom = Rom()

else:
    print("ERROR: No argument!")