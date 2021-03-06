from highscore import scoreobject

class Highscore:

    def add_score(self, name, score):
        """ Fügt einen Score sortiert in die Score-Liste ein
        """
        if self.snake_scores == None :
            self.snake_scores = scoreobject.Scoreobject(name, score, None)
        elif self.snake_scores.score < score:
            self.snake_scores = scoreobject.Scoreobject(name, score, self.snake_scores)
        else:
            self.snake_scores.add_object(name, score)

    def load(self):
        file = open('highscore_snake.txt')
        scores = file.readlines()
        for line in scores:
            self.read_score(line)
        file.close

    def read_score(self, line):
        """ Liest die Informationen aus der Zeile der Textdatei
        und speichert sie in einer Score-Liste ab
        """
        info = []
        text = ''
        first = True
        for c in line:
            if first :
                first = False
                if c != '%':
                    return
                continue
            if c != '%':
                text = text + c
            else:
                info = info + [text]
                text = ''
        self.add_score(info[0],int(info[1]))

    def get_scores(self, amount):
        """ Gibt ein Array mit den ersten n(= amount) Plätzen der Score-Liste zurück 
        """
        arr = []
        if self.snake_scores != None:
            arr = self.snake_scores.get_scores(amount, 0, arr)
        return arr
        
    def update_score(self):
        """ Speichert die 20 besten Einträge der Score-Liste persistent in der Textdatei
        """
        file = open('highscore_snake.txt', 'w') # Bestehender Inhalt wird dabei gelöscht
        scores = self.get_scores(20)
        for s in scores:
            file.write('%' + s.name + '%' + str(s.score) + '% \n')
        file.close()

    def print_out(self):
        """ Nur zum Testen; gibt alle Scores der Score-Liste auf der Konsole zurück
        """
        if self.snake_scores != None:
            self.snake_scores.print_out()
        print('')

    def __init__(self):
        self.snake_scores = None # Die Score-Liste für die Snake-Scores
        self.load()

