from inspect import signature

class Memory(list):
    """
    Inherited list, extends size on demand
    """
    def __init__(self, listinput):
        self.list = listinput
        self.size = len(listinput)
        self.padding = 20

    def checksize(self, i):
        diff = (i + 1) - self.size
        if diff > 0:
            self.list.extend([0] * (diff + self.padding))
            self.size += diff + self.padding

    def __getitem__(self, i):
        self.checksize(i)
        return self.list[i]

    def __setitem__(self, i, v):
        self.checksize(i)
        self.list[i] = v

    def __len__(self):
        return self.size


class Computer:
    def __init__(self, memory, phase):
        self.memory = Memory(memory)
        self.inputs = [phase]
        self.outputs = list()
        self.func_table = self.get_func_table()
        self.index = 0
        self.running = True
        self.debug = False
        self.interactive = False
        self.offset = 0

    def set_input_func(self,func):
        self.interactive = True
        self.get_input = func

    def get_func_table(self):
        def add(a, b, c):
            self.memory[c] = self.memory[a] + self.memory[b]
        def mult(a, b, c):
            self.memory[c] = self.memory[a] * self.memory[b]
        def write(a):
            if self.interactive:
                cpu_input = self.get_input()
            else:
                cpu_input = self.inputs.pop(0)
            self.memory[a] = cpu_input
        def output(a):
            self.outputs.append(self.memory[a])
            return self.outputs[-1]
        def nonzero(a, b):
            if self.memory[a] != 0:
                self.index = self.memory[b]
        def iszero(a, b):
            if self.memory[a] == 0:
                self.index = self.memory[b]
        def lt(a, b, c):
            self.memory[c] = 1 if self.memory[a] < self.memory[b] else 0
        def equal(a, b, c):
            self.memory[c] = 1 if self.memory[a] == self.memory[b] else 0
        def offset(a):
            self.offset += self.memory[a]
        def ret():
            self.running = False

        return {1:  add,
                2:  mult,
                3:  write,
                4:  output,
                5:  nonzero,
                6:  iszero,
                7:  lt,
                8:  equal,
                9:  offset,
                99: ret}


    def get_args(self, arg_count):
        args = list()
        mode = self.memory[self.index] // 100

        for i in range(1,arg_count+1):
            current_mode = mode % 10
            current_index = self.index + i
            # Immediate Mode
            if current_mode == 1:
                args.append(current_index)
            #  Relative Mode
            elif current_mode == 2:
                args.append(self.memory[current_index] + self.offset)
            # Position Mode
            else:
                args.append(self.memory[current_index])
            mode //= 10

        return tuple(args)


    def call_func(self, instruction):
        opcode = instruction % 100
        func = self.func_table[opcode]
        num_args = len(signature(func).parameters)
        args = self.get_args(num_args)

        if num_args > 0:
            self.index += num_args + 1

        if self.debug:
            print(f"\ninstruction: {instruction}")
            print(str(func).split('.')[3].split(' ')[0],
                  args)
            for i in args:
                print('  arg ', i, 'value: ', self.memory[i])

        return func(*args)


    def run(self, stdin=None):
        if stdin is not None:
            self.inputs.append(stdin)

        while self.running:
            instruction = self.memory[self.index]
            result = self.call_func(instruction)
            if result is not None:
                return result
