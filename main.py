from typing import List
import os
import requests
import typer
from dotenv import load_dotenv

load_dotenv()

def main(year: List[int] = range(2015, 2025), day: List[int] = range(1,26), part: List[int] = range(1, 3)):
    for y in year:
        for d in day:
            data = requests.get(f"https://adventofcode.com/{y}/day/{d}/input",
                                cookies={"session": os.environ["SESSION_ID"]}).text
            for p in part:
                exec_file(y, d, p, data)

def exec_file(year, day, part, data):
    if os.path.isfile(f"./src/{year}-{day}-{part}.py"):
        exec(open(f"./src/{year}-{day}-{part}.py").read())

if __name__ == "__main__":
    typer.run(main)