import sys
import os

class Interpreter(object):
    def __init__(self, file_path, DEBUG=False):
        self.tape = [0] * 30000
        self.data_pointer = 0
        self.program_pointer = 0
        self.DEBUG = DEBUG

        with open(file_path) as file:
            self.program = file.read()

    def move_pointer_right(self):
        self.data_pointer += 1

    def move_pointer_left(self):
        self.data_pointer -= 1

    def increment_cell(self):
        self.tape[self.data_pointer] += 1

    def decrement_cell(self):
        self.tape[self.data_pointer] -= 1

    def out_cell(self):
        sys.stdout.write(chr(self.tape[self.data_pointer]))

    def in_cell(self):
        self.tape[self.data_pointer] = sys.stdin.read(1)

    def jump_forward(self):
        """Jumps to instruction after ] if current cell == 0"""
        if self.tape[self.data_pointer] == 0:
            while self.program[self.program_pointer] != ']':
                self.program_pointer += 1

    def jump_backwards(self):
        """Jumps to ["""
        while self.program[self.program_pointer] != '[':
            self.program_pointer -= 1
        self.program_pointer -= 1

    def print_program(self):
        print(self.program)

    def run_step(self):
        try:
            instr = self.program[self.program_pointer]
        except IndexError:
            if self.DEBUG:
                print('tape[0:100]:')
                print(self.tape[:100])
                print('End of program')
            exit(0)
        if self.DEBUG:
            _ = input('Press ENTER for next step')
            print('Cell number: {}, cell value: {}'.format(self.data_pointer, self.tape[self.data_pointer]))
            print('Instruciton: {}, instruction ptr: {}'.format(self.program[self.program_pointer], self.program_pointer))
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
        if instr == '[':
            self.jump_forward()
        if instr == ']':
            self.jump_backwards()
        self.program_pointer += 1
    
    def run(self):
        while True:
            self.run_step()


DEBUG = os.environ.get('DEBUG', 0)
interpreter = Interpreter(sys.argv[1], DEBUG)
interpreter.run()