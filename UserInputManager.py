from Instruction import *
import random
import math


class UserInputManager:
    def __init__(self):
        self.instructions_2d = get_instructions("instructions.txt")  # Save the 2D array of instructions
        self.instructions = []
        self.current_instructions = []
        self.total_score = 0
        # TODO: Add a random instruction

    def populate_random_panel_instructions(self, number_of_instructions, score):
        player_to_assign_to = 0
        max_complexity = len(self.instructions_2d) - 1
        min_complexity = 0
        mean_complexity = (max_complexity / 3) * math.log10(score + 1)
        for i in range(number_of_instructions):
            # TODO : Calculate complexity based on a normal distribution or something fancy
            unique = False
            while not unique:
                complexity = random.gauss(mean_complexity, 0.3 * (1 + mean_complexity))
                complexity = min(max(complexity, min_complexity), max_complexity)
                if complexity - math.floor(complexity) >= 0.5:
                    complexity = math.ceil(complexity)
                else:
                    complexity = math.floor(complexity)
                this_instruction = get_instruction(self.instructions_2d, complexity)
                unique = True
                for instruction in self.instructions:
                    if instruction.message == this_instruction.message:
                        unique = False
                        break
            if i >= number_of_instructions / 2:
                    player_to_assign_to = 1
            used_keys = []
            for instruction in self.instructions:
                used_keys.append(instruction.key_stroke)
            this_instruction.set_player(player_to_assign_to, used_keys)
            self.instructions.append(this_instruction)

    def set_player_instructions(self):
        self.total_score = 0
        self.current_instructions = []
        player_0_instruction = DisplayInstruction(self.instructions[randint(0, len(self.instructions) - 1)], 0)
        player_1_instruction = DisplayInstruction(self.instructions[randint(0, len(self.instructions) - 1)], 1)
        self.current_instructions.append(player_0_instruction)
        self.current_instructions.append(player_1_instruction)

    def check_inputs(self, key_pressed):
        # If there are no more instructions left return the total score accumulated for this round.
        if not len(self.current_instructions):
            this_total = self.total_score
            self.total_score = 0
            return this_total
        # input_found = False  # To make sure that when an input is entered we do not incorrectly return -1
        instructions_to_remove = []  # Store the instructions we should remove.
        # If there are instructions left loop through them and check to see for correct input.
        for instruction in self.current_instructions:
            if instruction.check_key(key_pressed):
                instructions_to_remove.append(instruction)
        # If there are no instructions to remove decide whether to return 0 or -1 depending on whether or not the key is
        # a valid command.
        if not len(instructions_to_remove):
            if left_keys.__contains__(key_pressed) or right_keys.__contains__(key_pressed):
                return -1
            return 0
        # Go through all instructions to remove and add the scores. Also remove them from the array.
        for instruction in instructions_to_remove:
            self.total_score += instruction.calculate_score()  # Add the score of the instruction
            self.current_instructions.remove(instruction)  # Remove the instruction
        if not len(self.current_instructions):  # If no more instructions remain, return total score.
            this_total = self.total_score
            self.total_score = 0
            return this_total
        return 0  # If we reached all this way without returning anything we must have entered only one correct input