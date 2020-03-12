import re

raw_file_name = "R:\\TXT_training\\mod-8-pract-5.txt"
structured_file_name = "R:\\TXT_training\\mod-8-pract-5-STRUCTURED.txt"

time = re.compile(r"\d\d?:\d\d?:\d\d?")
train_number = re.compile(r"\d+")  # Использовать [0]
from_in = re.compile(r"[и][з]|[в]")  # использовать search
city = re.compile(r"[а-яА-Я]{3,}")  # Вызывать это в [-1]

# time.findall(lane)[0]
# train_number.findall(lane)[0]
# from_in.search(lane).group()
# city.findall(lane)[-1]

with open(structured_file_name, "a", encoding="utf-8") as structured_file:
    with open(raw_file_name, "r", encoding="utf-8") as raw_file:
        for lane in raw_file.readlines():
            if lane.startswith("Рейс"):
                structured_file.write(f"[{time.findall(lane)[0]}]: Поезд №{train_number.findall(lane)[0]} {from_in.search(lane).group()} {city.findall(lane)[-1]}" + "\n")