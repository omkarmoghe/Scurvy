import os.path


class HighScoreManager():

    def __init__(self, filename):
        self.filename = filename
        self.highscores = self.load_high_scores(self.filename)

    def load_high_scores(self, filename):
        if not os.path.isfile(filename):
            f_out = open(filename, 'w')
            f_out.close()

        high_scores = []

        f_in = open(filename, 'r')
        for line in f_in:
            pair = line.split(':')  # split the line at the colon
            high_scores.append((pair[0], int(pair[1])))  # the second part is the complexity

        high_scores.sort(key=lambda tup: tup[1])
        high_scores.reverse()
        return high_scores

    def save_high_scores(self):
        f_out = open(self.filename, 'w')

