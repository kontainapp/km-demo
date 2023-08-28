from src.generate import base
from pathlib import Path

def main():
    base.main(prompt="My name is ", 
              checkpoint_dir=Path("src/checkpoints/stabilityai/stablelm-base-alpha-3b"))

if __name__ == '__main__':
    main()
