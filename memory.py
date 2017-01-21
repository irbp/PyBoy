class Memory:
    memory = bytearray(65536)

    # initializing gb memory
    def __init__(self):
        for i in range(0, 65536):
            self.memory[i] = 0

    # load bytes into the gb memory
    def load(self, data, offset):
        for i in range(0, len(data)):
            self.memory[int(i + offset)] = data[i]

    # show memory content (memory[addr] ~ memory[addr + offset])
    def show(self, addr, offset):
        for i in range(addr, offset + 1):
            print("memory[%s] = %s" %(hex(i), hex(self.memory[i])))