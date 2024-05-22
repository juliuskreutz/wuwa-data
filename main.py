import requests
import csv

text_map = requests.get(
    "https://raw.githubusercontent.com/Dimbreath/WutheringData/master/TextMap/en/MultiText.json"
).json()
achievements_data = requests.get(
    "https://raw.githubusercontent.com/Dimbreath/WutheringData/master/ConfigDB/Achievement.json"
).json()

# Define a sorting function to sort by GroupID first, then by ID
def sort_key(achievement):
    return int(achievement["GroupId"]), int(achievement["Id"])

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

    # Sort the achievements_data list using the sort_key function
    achievements_data.sort(key=sort_key)

    for achievement in achievements_data:
        writer.writerow(
            [
                text_map.get(achievement["Name"], ""),
                text_map.get(achievement["Desc"], ""),
                achievement["ID"],
                achievement["GroupID"],
                achievement["Level"],
                achievement["Hidden"],
                achievement["IconPath"],
                achievement["OverrideDropId"],
                achievement["NextLink"],
                achievement["ClientTrigger"],
            ]
        )
