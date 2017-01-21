class Debug:
    def __init__(self):
        pass

    def memDebug(self, mem, addr, offset):
        for i in range(addr, offset):
            print("memory[%s] = %s" %(hex(i), hex(mem.memory[i])))