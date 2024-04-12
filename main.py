import sys

from tododone.services.CommandProcessor import CommandProcessor
from tododone.services.export_done_todos import DoneTodosExporter
from tododone.utils.json_loader import JsonLoader
from tododone.utils.json_writer import JsonWriter


def main():
  if len(sys.argv) < 2:
    print("Usage: <script_name> <action> [option]")
    sys.exit(1)

  action = sys.argv[1]
  option = sys.argv[2] if len(sys.argv) > 2 else ""

  commandProcessor = CommandProcessor(JsonLoader(), JsonWriter(), DoneTodosExporter())
  commandProcessor.process(action, option)

if __name__ == "__main__":
  main()