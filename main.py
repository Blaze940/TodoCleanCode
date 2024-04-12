import sys

from setup import process_command


def main():
  if len(sys.argv) < 2:
    print("Usage: <script_name> <action> [option]")
    sys.exit(1)

  action = sys.argv[1]
  option = sys.argv[2] if len(sys.argv) > 2 else ""

  process_command(action, option)

if __name__ == "__main__":
  main()