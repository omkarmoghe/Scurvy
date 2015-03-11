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
            usedKeys = []
            for instruction in self.instructions:
                usedKeys.append(instruction.key_stroke)
            this_instruction.set_player(player_to_assign_to, usedKeys)
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
        if len(self.current_instructions) == 0:
            this_total = self.total_score
            self.total_score = 0
            return this_total
        # If there are instructions left loop through them and check to see for correct input.
        for (i, instruction) in enumerate(self.current_instructions):
            if instruction.check_key(key_pressed):
                self.total_score += self.current_instructions[i].calculate_score()
                self.current_instructions.remove(instruction)
                if not len(self.current_instructions):
                    this_total = self.total_score
                    self.total_score = 0
                    return this_total
        if left_keys.__contains__(key_pressed) or right_keys.__contains__(key_pressed):
            return -1
        return 0