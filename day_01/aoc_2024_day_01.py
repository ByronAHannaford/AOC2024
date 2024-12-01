# Advent of Code 2024
# Day 01
# Byron

import argparse
import logging
import sys

from pathlib import Path

PARENT_FOLDER = Path(__file__).parent
BASE_FILE_NAME = Path(__file__).stem
INPUT_FILE_NAME = f"{BASE_FILE_NAME}_input.txt"
SAMPLE_FILE_NAME = f"{BASE_FILE_NAME}_sample.txt"

INPUT_PATH = PARENT_FOLDER / INPUT_FILE_NAME
SAMPLE_PATH = PARENT_FOLDER / SAMPLE_FILE_NAME


logger = logging.getLogger("aoc_logger")
log_handler = logging.StreamHandler()
log_handler.setLevel("DEBUG")
logger.addHandler(log_handler)


# ---=== PROBLEM CODE BELOW ===---


from typing import Tuple

def parse_input(data_path: Path) -> Tuple[list, list]:
    """
    Reads and formats input.
    Should return the input data in a format where it is ready to be worked on.
    """

    listOne = []
    listTwo = []

    rawInput = []
    with open(data_path, "r") as raw_input:
        rawInput = [l.strip() for l in raw_input.readlines()]
    
    for line in rawInput:
        splitLine = line.split("   ")

        listOne.append(int(splitLine[0]))
        listTwo.append(int(splitLine[1]))

    return listOne, listTwo


def part_1(input_data: Tuple[list, list]):
    listOne, listTwo = input_data

    # - No need to sort
    # - abs ensures the value is not negative
    sum_diff = sum(abs(a - b) for a, b in zip(listOne, listTwo))
    
    """Solution code for Part 1. Should return the solution."""
    return sum_diff


def part_2(input_data: Tuple[list, list]):
    listOne, listTwo = input_data

    #Use a dict to reduce time complexity
    count_dict = {}
    for num in listTwo:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    similarity_score = sum(num * count_dict.get(num, 0) for num in listOne)
        
    """Solution code for Part 2. Should return the solution."""
    return similarity_score


def run_direct():
    """
    This function runs if this file is executed directly, rather than using the
    justfile interface. Useful for quick debugging and checking your work.
    """
    print(parse_input(SAMPLE_PATH))


# ---=== PROBLEM CODE ABOVE ===---


def problem_dispatch(mode: str, part: int, log_level: str = None):
    if log_level is not None:
        logger.setLevel(log_level.upper())
    parts = {1: part_1, 2: part_2}
    inputs = {"check": parse_input(SAMPLE_PATH), "solve": parse_input(INPUT_PATH)}
    return parts[part](inputs[mode])


def run_cli():
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", type=str, choices={"check", "solve"})
    parser.add_argument("part", type=int, choices={1, 2})
    parser.add_argument(
        "--log-level",
        type=str,
        required=False,
        choices={"CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG"},
    )
    args = parser.parse_args()
    print(problem_dispatch(args.mode, args.part, args.log_level))


if __name__ == "__main__":
    if len(sys.argv) == 1:
        raise SystemExit(run_direct())
    else:
        raise SystemExit(run_cli())
