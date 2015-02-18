from Instruction import *


class UserInputManager:
    def __init__(self):
        self.instructions_2d = get_instructions("instructions.txt")  # Save the 2D array of instructions
        self.instructions = []
        self.current_instructions = []
        self.total_score = 0
        # TODO: Add a random instruction

    def populate_random_panel_instructions(self, number_of_instructions, mean_complexity):
        player_to_assign_to = 0
        for i in range(0, number_of_instructions, 1):
            # TODO : Calculate complexity based on a normal distribution or something fancy
            complexity = mean_complexity
            this_instruction = get_instruction(self.instructions_2d, complexity)
            if i >= number_of_instructions / 2:
                player_to_assign_to = 1
            this_instruction .set_player(player_to_assign_to)
            self.instructions.append(this_instruction)

    def set_player_instructions(self):
        self.total_score = 0
        self.current_instructions = []
        player_0_instruction = DisplayInstruction(self.instructions[randint(0, len(self.instructions) - 1)], 0)
        player_1_instruction = DisplayInstruction(self.instructions[randint(0, len(self.instructions) - 1)], 1)
        self.current_instructions.append(player_0_instruction)
        self.current_instructions.append(player_1_instruction)

    def check_inputs(self, key_pressed):
        if ~len(self.current_instructions):
            this_total = self.total_score
            self.total_score = 0
            return this_total

        for (i, instruction) in enumerate(self.current_instructions):
            if instruction.check_key(key_pressed):
                self.total_score += self.current_instructions[i].calculate_score
                self.current_instructions.remove(i)
                if ~len(self.current_instructions):
                    this_total = self.total_score
                    self.total_score = 0
                    return this_total
                return 0