from Instruction import *


class UserInputManager:
    def __init__(self):
        self.instructions = []
        self.instructions_2d = get_instructions("instructions.txt")  # Save the 2D array of instructions

    def append_instruction(self, instruction):
        self.instructions.append(instruction)

    def check_inputs(self, key_pressed):
        for instruction in self.instructions:
            if instruction.check_key(key_pressed):
                assert False
                # TODO: Add code for instruction received

#