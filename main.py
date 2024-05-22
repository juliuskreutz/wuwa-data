import requests
import csv

text_map = requests.get(
    "https://raw.githubusercontent.com/Dimbreath/WutheringData/master/TextMap/en/MultiText.json"
).json()
achievements_data = requests.get(
    "https://raw.githubusercontent.com/Dimbreath/WutheringData/master/ConfigDB/Achievement.json"
).json()

with open("achievements.csv", "w", newline="") as f:
    writer = csv.writer(f)

    writer.writerow(
        [
            "Name",
            "Desc",
            "ID",
            "GroupID",
            "Level",
            "Hidden",
            "IconPath",
            "OverrideDropId",
            "NextLink",
            "ClientTrigger",
        ]
    )

    for achievement in achievements_data:
        writer.writerow(
            [
                text_map.get(achievement["Name"], ""),
                text_map.get(achievement["Desc"], ""),
                achievement["Id"],
                achievement["GroupId"],
                achievement["Level"],
                achievement["Hidden"],
                achievement["IconPath"],
                achievement["OverrideDropId"],
                achievement["NextLink"],
                achievement["ClientTrigger"],
            ]
        )
