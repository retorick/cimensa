import random
from cimensa.models import Words

class Homegame:
    def __init__(self):
        self.page_title = 'Games'
        words = Words.objects.raw("SELECT id, word, part_of_speech, definition FROM cimensa_words ORDER BY RAND() LIMIT 6")
        rnd = random.random()
        self.correct = 1+int(6 * rnd)
        self.words = words
