import pygame
from random import randint

max_difficulty = 3  # starts from 0

left_keys = [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_q, pygame.K_w, pygame.K_e, pygame.K_r,
             pygame.K_t, pygame.K_a, pygame.K_s, pygame.K_d, pygame.K_f, pygame.K_g, pygame.K_z, pygame.K_x, pygame.K_c,
             pygame.K_v, pygame.K_b]
right_keys = [pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9, pygame.K_0, pygame.K_y, pygame.K_u, pygame.K_i,
              pygame.K_o, pygame.K_p, pygame.K_h, pygame.K_j, pygame.K_k, pygame.K_l, pygame.K_SEMICOLON, pygame.K_n,
              pygame.K_m, pygame.K_COMMA, pygame.K_PERIOD, pygame.K_SLASH]


class Instruction ():
    def __init__(self, message, complexity, key_stroke):
        self.message = message
        self.complexity = complexity
        self.key_stroke = key_stroke

    def check_key(self, key):
        return self.key_stroke == key


# returns a 2D list of Instructions from a text file
def get_instructions(file_name):
    instructions_2d = []
    for i in range(0, 4):
        instructions_2d.append([])

    infile = open(file_name, 'r')

    for line in infile:
        pair = line.split(':')
        message = pair[0]
        complexity = int(pair[1])

        if randint(0, 1):  # left_keys are 0, right_keys are 1
            instr = Instruction(message, complexity, right_keys[randint(0, 19)])
        else:
            instr = Instruction(message, complexity, right_keys[randint(0, 19)])

        instructions_2d[complexity].append(instr)

    infile.close()

    return instructions_2d


# returns a random instruction of the specified complexity level
def get_instruction(file_name, complexity):
    instructions_2d = get_instructions(file_name)
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