def add(description: str):
  print("postit added!")

def remove(postIt_id: str):
  print(f"postit [{postIt_id}] removed!")

def show():
  print(f"Here are the current tasks postits!")

def export():
  print("postits exported!")

def process_command(action, option=""):
  if action == "add":
    description = option
    add(description)
  elif action == "remove":
    postIt_id = option
    remove(postIt_id)
  elif action == "show":
    show()
  elif action == "export":
    export()