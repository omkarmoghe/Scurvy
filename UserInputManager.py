from Instruction import *


class UserInputManager:
    def __init__(self):
        self.instructions_2d = get_instructions("instructions.txt")  # Save the 2D array of instructions
        self.instructions = []


        self.current_instructions = []
        # TODO: Add a random instruction


    def append_instruction(self, instruction):
        self.instructions.append(instruction)

    def check_inputs(self, key_pressed):
        for instruction in self.current_instructions:
            if instruction.check_key(key_pressed):
                assert False
                # TODO: Add code for instruction received
