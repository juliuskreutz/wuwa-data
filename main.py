import requests
import csv

text_map = requests.get(
    "https://raw.githubusercontent.com/Dimbreath/WutheringData/master/TextMap/en/MultiText.json"
).json()
achievements_data = requests.get(
    "https://raw.githubusercontent.com/Dimbreath/WutheringData/master/ConfigDB/Achievement.json"
).json()

# Define mappings for GroupId to AchievementCategory and AchievementGroup keys
category_map = {
    (1001, 1002, 1004): 'AchievementCategory_1_Name',
    (2001, 2002, 2003, 2004): 'AchievementCategory_2_Name',
    (3001, 3002, 3003, 3004, 3005): 'AchievementCategory_3_Name',
    (4001, 4002): 'AchievementCategory_4_Name',
}

group_map = {
    1001: 'AchievementGroup_1001_Name',
    1002: 'AchievementGroup_1002_Name',
    1004: 'AchievementGroup_1004_Name',
    2001: 'AchievementGroup_2001_Name',
    2002: 'AchievementGroup_2002_Name',
    2003: 'AchievementGroup_2003_Name',
    2004: 'AchievementGroup_2004_Name',
    3001: 'AchievementGroup_3001_Name',
    3005: 'AchievementGroup_3005_Name',
    3002: 'AchievementGroup_3002_Name',
    3003: 'AchievementGroup_3003_Name',
    3004: 'AchievementGroup_3004_Name',
    4001: 'AchievementGroup_4001_Name',
    4002: 'AchievementGroup_4002_Name',
}

# Function to determine category based on GroupId
def get_category(group_id):
    for key_tuple, category_key in category_map.items():
        if group_id in key_tuple:
            return text_map.get(category_key, "")
    return ""

# Function to determine group based on GroupId
def get_group(group_id):
    group_key = group_map.get(group_id)
    if group_key:
        return text_map.get(group_key, "")
    return ""

# Define a sorting function to sort by GroupID first, then by ID
def sort_key(achievement):
    return int(achievement["GroupId"]), int(achievement["Id"])

with open("achievements.csv", "w", newline="") as f:
    writer = csv.writer(f)

    writer.writerow(
        [
            "Category",
            "Group",
            "Name",
            "Desc",
            "ID",
            "GroupID",
            "Level",
            "Hidden",
            "NextLink",
        ]
    )

    # Sort the achievements_data list using the sort_key function
    achievements_data.sort(key=sort_key)

    for achievement in achievements_data:
        group_id = achievement.get("GroupId")
        if group_id is None:
            category = ""
            group = ""
        else:
            group_id = int(group_id)
            category = get_category(group_id)
            group = get_group(group_id)
        
        next_link = achievement["NextLink"]
        if next_link == -1:
            next_link = ""

        writer.writerow(
            [
                category,
                group,
                text_map.get(achievement["Name"], ""),
                text_map.get(achievement["Desc"], ""),
                achievement["Id"],
                achievement["GroupId"],
                achievement["Level"],
                achievement["Hidden"],
                next_link,
            ]
        )
