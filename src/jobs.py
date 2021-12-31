from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path, mode="r") as file:
        dict = csv.DictReader(file)
        return [row for row in dict]
