import os.path


# HIGH SCORES FORMAT IS AS FOLLOWS:
#     Player1:Player2:score
# ex. Bart:Lisa:400
class HighScoreManager():

    def __init__(self, filename):
        self.filename = filename
        self.highscores = self.load_high_scores()
        self.sort_high_scores()

    def load_high_scores(self):
        if not os.path.isfile(self.filename):
            f_out = open(self.filename, 'w')
            f_out.close()

        high_scores = []

        f_in = open(self.filename, 'r')
        for line in f_in:
            set = line.split(':')  # split the line at the colon
            high_scores.append((set[0], set[1], int(set[2])))  # first half is name, second half is score

        f_in.close()

        return high_scores

    def save_high_scores(self):
        self.sort_high_scores()

        f_out = open(self.filename, 'w')

        for pair in self.highscores:
            f_out.write(pair[0] + ':' + pair[1] + ':' + str(pair[2]) + '\n')

        f_out.close()

    def sort_high_scores(self):
        self.highscores.sort(key=lambda tup: tup[2])
        self.highscores.reverse()

    # set is a tuple (Player1, Player2, score)
    def add_high_score(self, set):
        if len(self.highscores) < 10:
            self.sort_high_scores()
            self.highscores.append(set)
            self.sort_high_scores()
        elif len(self.highscores) == 10:
            self.highscores.append(set)
            self.sort_high_scores()
            del self.highscores[-1]
            self.save_high_scores()
        else:
            assert False  # should never be the case

# FOR TESTING ONLY
# hsm = HighScoreManager("highscores.txt")
# print hsm.highscores
# hsm.save_high_scores()
# hsm.add_high_score(("Harold", "Kumar", 420))