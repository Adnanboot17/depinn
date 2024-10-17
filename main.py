from src.launcher import main
from src.deeplchain import clear, log, mrh

if __name__ == "__main__":
    clear()
    while True:
        try:
            main()
        except KeyboardInterrupt:
            log(mrh + f"Process interrupted by user.")
            exit(0)