import requests
import json

text_map = requests.get(
    "https://raw.githubusercontent.com/Dimbreath/WutheringData/master/TextMap/en/MultiText.json"
).json()
achievements_data = requests.get(
    "https://raw.githubusercontent.com/Dimbreath/WutheringData/master/ConfigDB/Achievement.json"
).json()

achievements = []
for achievement in achievements_data:
    achievements.append(
        {
            "name": text_map.get(achievement["Name"], ""),
            "description": text_map.get(achievement["Desc"], ""),
            "id": achievement["Id"],
            "group_id": achievement["GroupId"],
            "level": achievement["Level"],
            "hidden": achievement["Hidden"],
            "icon_path": achievement["IconPath"],
            "override_drop_id": achievement["OverrideDropId"],
            "next_link": achievement["NextLink"],
            "client_trigger": achievement["ClientTrigger"],
        }
    )

with open("achievements.json", "w") as f:
    json.dump(achievements, f)
