from models import Calendar

class Events:
    def __init__(self):
        self.events = Calendar.objects.all()

