from tododone.domain import todo_list
from tododone.domain.todo_list import TodoList
from tododone.interfaces.IDoneTodosExporter import IDoneTodosExporter
from tododone.utils.todo_list_util import filter_done_todos, sort_todos


class DoneTodosExporter(IDoneTodosExporter):
    def __init__(self):
        pass

    def export_done_todos(self, todo_list: TodoList, filename='report.md'):
        # Filter the list to get only the completed todos
        done_todos = filter_done_todos(todo_list)

        # Sort todos by creation date, descending
        done_todos = sort_todos(done_todos, descending=True)

        # Create the content of the report
        content = "# Report\n## Tasks done:\n\n"
        content += "\n".join(f"- {todo.description} ({todo.creation_date.strftime('%Y-%m-%d')})" for todo in done_todos)

        # Write the content to a markdown file
        with open(filename, 'w') as file:
            file.write(content)
        print(f"Report generated: {filename}")