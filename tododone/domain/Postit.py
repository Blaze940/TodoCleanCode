class PostIt:
    def __init__(self, id, description, creation_date):
        self.id = id
        self.description = description
        self.creation_date = creation_date
        self.is_done = False
