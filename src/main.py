import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
python_dir = os.path.join(current_dir, "python")

sys.path.append(python_dir)
os.chdir(python_dir)

if __name__ == "__main__":
    from python.cli import main_menu
    main_menu()
