class Cpu:
    AF = 0  # AF register
    F = 0   # F register
    BC = 0  # BC register
    DE = 0  # DE register
    HL = 0  # HL register
    SP = 0  # Stack Pointer
    PC = 0  # Program Counter
    
    def __init__(self, mem):
        # Initializing the registers with some default values
        self.AF = 0x01
        self.F = 0xB0
        self.BC = 0x13
        self.DE = 0xD8
        self.HL = 0x14D
        self.SP = 0xFFFE
        self.PC = 0x00

        # Initializing some address with default values
        mem.memory[0xFF05] = 0x00
        mem.memory[0xFF06] = 0x00
        mem.memory[0xFF07] = 0x00
        mem.memory[0xFF10] = 0x80
        mem.memory[0xFF11] = 0xBF
        mem.memory[0xFF12] = 0xF3
        mem.memory[0xFF14] = 0xBF
        mem.memory[0xFF16] = 0x3F
        mem.memory[0xFF17] = 0x00
        mem.memory[0xFF19] = 0xBF
        mem.memory[0xFF1A] = 0x7F
        mem.memory[0xFF1B] = 0xFF
        mem.memory[0xFF1C] = 0x9F
        mem.memory[0xFF1E] = 0xBF
        mem.memory[0xFF20] = 0xFF
        mem.memory[0xFF21] = 0x00
        mem.memory[0xFF22] = 0x00
        mem.memory[0xFF23] = 0xBF
        mem.memory[0xFF24] = 0x77
        mem.memory[0xFF25] = 0xF3
        mem.memory[0xFF26] = 0xF1
        mem.memory[0xFF40] = 0x91
        mem.memory[0xFF42] = 0x00
        mem.memory[0xFF43] = 0x00
        mem.memory[0xFF45] = 0x00
        mem.memory[0xFF47] = 0xFC
        mem.memory[0xFF48] = 0xFF
        mem.memory[0xFF49] = 0xFF
        mem.memory[0xFF4A] = 0x00
        mem.memory[0xFF4B] = 0x00
        mem.memory[0xFFFF] = 0x00

        print ("GameBoy reseted")

    def debugRegs(self):
        print("AF ---> %s" %hex(self.AF))
        print("F  ---> %s" %hex(self.F))
        print("BC ---> %s" %hex(self.BC))
        print("DE ---> %s" %hex(self.DE))
        print("HL ---> %s" %hex(self.HL))
        print("SP ---> %s" %hex(self.SP))
        print("PC ---> %s" %hex(self.PC))