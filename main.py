from typing import Optional
import os
import requests
import typer
from dotenv import load_dotenv

load_dotenv()

def main(year: Optional[int] = None, day: Optional[int] = None, part: Optional[int] = None):
    if year is not None:
        if day is not None:
            data = requests.get(f"https://adventofcode.com/{year}/day/{day}/input", cookies={"session": os.environ["SESSION_ID"]}).text
            if part is not None:
                exec_file(year, day, part, data)
            else:
                for i in range(1, 3):
                    exec_file(year, day, i, data)
        else:
            for j in range(1, 26):
                for i in range(1, 3):
                    data = requests.get(f"https://adventofcode.com/{year}/day/{j}/input",
                                        cookies={"session": os.environ["SESSION_ID"]}).text
                    exec_file(year, j, i, data)
    else:
        for k in range(2015, 2025):
            for j in range(1, 26):
                for i in range(1, 3):
                    data = requests.get(f"https://adventofcode.com/{k}/day/{j}/input",
                                        cookies={"session": os.environ["SESSION_ID"]}).text
                    exec_file(k, j, i, data)

def exec_file(year, day, part, data):
    if os.path.isfile(f"./src/{year}-{day}-{part}.py"):
        exec(open(f"./src/{year}-{day}-{part}.py").read())

if __name__ == "__main__":
    typer.run(main)