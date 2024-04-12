from tododone.domain.Postit import PostIt


class Todo:
    def __init__(self, todos: list[PostIt]):
        self.todos = todos

    def add(self, postit):
        self.todos.append(postit)

    def remove(self, postit):
        self.todos.remove(postit)

    def get_all_todos(self):
        return self.todos

    def get_one_todo(self, id):
        for postit in self.todos:
            if postit.id == id:
                return postit

    def mark_as_done(self, postit):
        postit = self.get_one_todo(postit)
        postit.is_done = True
