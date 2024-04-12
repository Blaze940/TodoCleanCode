from datetime import datetime


class Todo:
    def __init__(self, id, description, creation_date, is_done=False):
        self.id = id
        self.description = description
        self.creation_date = creation_date
        self.is_done = is_done

    def time_elapsed(self):
        now = datetime.now()
        diff = now - self.creation_date
        if diff.days >= 365:
            years = diff.days // 365
            return f"{years} year{'s' if years > 1 else ''}"
        elif diff.days >= 30:
            months = diff.days // 30
            return f"{months} month{'s' if months > 1 else ''}"
        elif diff.days > 0:
            return f"{diff.days} day{'s' if diff.days > 1 else ''}"
        elif diff.seconds >= 3600:
            hours = diff.seconds // 3600
            return f"{hours} hour{'s' if hours > 1 else ''}"
        elif diff.seconds >= 60:
            minutes = diff.seconds // 60
            return f"{minutes} min"
        else:
            return "Just now"

    def to_dict(self):
        return {
            'id': self.id,
            'description': self.description,
            'creation_date': self.creation_date.strftime('%Y-%m-%dT%H:%M:%S'),
            'is_done': self.is_done
        }

    def __str__(self):
        done_symbol = "X" if self.is_done else " "
        elapsed = self.time_elapsed()
        return f"[{self.id:02}][{done_symbol}] {self.description} ({elapsed})"
