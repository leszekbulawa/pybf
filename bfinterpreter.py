import sys

class Interpreter(object):
    def __init__(self, file_path):
        self.tape = [0] * 30000
        self.data_pointer = 0
        self.instr_pointer = 0
        self.jump_table = []

        with open(file_path) as file:
            self.program = file.read()

    def move_pointer_right(self):
        self.data_pointer += 1

    def move_pointer_left(self):
        self.data_pointer += 1

    def increment_cell(self):
        self.tape[self.data_pointer] += 1

    def decrement_cell(self):
        self.tape[self.data_pointer] -= 1

    def out_cell(self):
        sys.stdout.write(chr(self.tape[self.data_pointer]))

    def in_cell(self):
        self.tape[self.data_pointer] = sys.stdin.read(1)

    # def jump_if_zero(self):


    def print_program(self):
        print(self.program)

    def run_step(self):
        instr = self.program[self.instr_pointer]
        if instr == '>':
            self.move_pointer_right()
        if instr == '<':
            self.move_pointer_left()
        if instr == '+':
            self.increment_cell()
        if instr == '-':
            self.decrement_cell()
        if instr == '.':
            self.out_cell()
        if instr == ',':
            self.in_cell()
        self.instr_pointer += 1
    
    def run(self):
        for _ in range(len(self.program)):
            self.run_step()

interpreter = Interpreter('test.bf')
interpreter.run()