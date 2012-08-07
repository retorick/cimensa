import random
from models import Word

class Words:

    def __init__(self):
        self.page_title = 'Games'
        words = self._rand_words()
        correct = random.randrange(0,5)
        self.correct = correct
        self.words = words


    def _rand_words(self):
        reclist = []
        records = Word.objects.raw("SELECT id, word, part_of_speech, definition FROM cimensa_words ORDER BY RAND() LIMIT 6")
        for record in records:
            reclist.append(record)
        return reclist
