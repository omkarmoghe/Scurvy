import pygame
from random import randint


max_difficulty = 3  # starts at 0

# list of left player keys
left_keys = [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_q, pygame.K_w, pygame.K_e, pygame.K_r,
             pygame.K_t, pygame.K_a, pygame.K_s, pygame.K_d, pygame.K_f, pygame.K_g, pygame.K_z, pygame.K_x, pygame.K_c,
             pygame.K_v, pygame.K_b]
# list of right player keys
right_keys = [pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9, pygame.K_0, pygame.K_y, pygame.K_u, pygame.K_i,
              pygame.K_o, pygame.K_p, pygame.K_h, pygame.K_j, pygame.K_k, pygame.K_l, pygame.K_SEMICOLON, pygame.K_n,
              pygame.K_m, pygame.K_COMMA, pygame.K_PERIOD, pygame.K_SLASH]


class Instruction ():
    def __init__(self, message, complexity):
        self.message = message
        self.complexity = complexity
        self.key_stroke = pygame.K_0
        self.player_number = 1

    def set_player(self, player_number):
        self.player_number = player_number
        if player_number == 0:
            self.key_stroke = left_keys[randint(0, len(left_keys) - 1)]
        elif player_number == 1:
            self.key_stroke = right_keys[randint(0, len(right_keys) - 1)]
        else:
            assert False
        self.player_number = player_number

    def check_key(self, key):
        return self.key_stroke == key

    def get_message(self):
        return "Press " + pygame.key.name(self.key_stroke) + " to " + self.message


class DisplayInstruction(Instruction):
    def __init__(self, instruction, player_displayed):
        self.message = instruction.message
        self.complexity = instruction.complexity
        self.key_stroke = instruction.key_stroke
        self.player_number = instruction.player_number
        self.player_displayed = player_displayed

    def calculate_score(self):
        return self.complexity + 1
        # TODO: Some awesome algorithm to calculate the score

    def draw(self, screen, screen_size):
        x_coord = screen_size.x / 4
        if self.player_displayed == 1:
            x_coord = 3 * screen_size.x / 4
        y_coord = screen_size.y + 50
        instruction_label = pygame.font.Font("Resources/font.otf", 15).render('{0}'.format(self.message),
                                                                                        True, (255, 255, 255))
        instruction_label_rect = instruction_label.get_rect()
        instruction_label_rect.centerx = x_coord
        instruction_label_rect.top = y_coord
        screen.blit(instruction_label, instruction_label_rect)


# returns a 2D list of Instructions from a text file
def get_instructions(file_name):
    # creates an empty 2d array
    instructions_2d = []
    for i in range(0, 4):
        instructions_2d.append([])

    infile = open(file_name, 'r')  # open the text file for reading

    # get each line in the text file of instructions
    for line in infile:
        pair = line.split(':')  # split the line at the colon
        message = pair[0]  # the first part is the message
        complexity = int(pair[1])  # the second part is the complexity

        # pick between either left player or right player to assign the instruction to
        if randint(0, 1):  # left_keys are 0, right_keys are 1
            instr = Instruction(message, complexity)
        else:
            instr = Instruction(message, complexity)  # right_keys[randint(0, 19)]

        instructions_2d[complexity].append(instr)  # add the instruction to the 2d list at the right row (complexity)

    infile.close()  # close file

    return instructions_2d  # return the 2d array


# returns a random instruction of the specified complexity level
def get_instruction(instructions_2d, complexity):
    # get a random instruction from the given complexity (row)
    return instructions_2d[complexity][randint(0, len(instructions_2d[complexity]) - 1)]

# FOR TESTING
# task = get_instructions("instructions.txt")
# for t in task:
#     for i in t:
#         print i.message
#         print i.complexity
# task = get_instruction("instructions.txt", 0)
# print task.message
# print task.complexity


