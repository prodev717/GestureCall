from fastapi import FastAPI
from typing import List, Tuple
import csv

app = FastAPI()

data: List[Tuple[str, str, int]] = []

def read_csv():
    global data
    with open("clients.csv", mode="r") as file:
        reader = csv.reader(file)
        next(reader)
        data = [(row[0], row[1], int(row[2])) for row in reader]

@app.on_event("startup")
def startup_event():
    read_csv()

@app.get("/clients", response_model=List[Tuple[str, str, int]])
def get_data():
    return data
