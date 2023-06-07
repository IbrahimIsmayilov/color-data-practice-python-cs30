# COLOR DATA PRACTICE

import json

# Load Color Data from JSON file
file = open("color-data.json", "r")
dataStr = file.read()
file.close()

color_data = json.loads(dataStr)


# 1
for i in range(len(color_data)):
    r = color_data[i]["r"]
    print(f"{r}")

# # 2
# for i in range(len(color_data)):
#     if color_data[i]["brightness"] > 200:
#         print("\n" + color_data[i]["name"])
#         print(color_data[i]["family"])

# # 3
# count = 0
# for i in range(len(color_data)):
#     if color_data[i]["family"] == "Red" or color_data[i]["family"] == "Pink":
#         count += 1
# print(f"\n{count}")

#4
# count = 0
# color_family_input = input("Please enter a color family: ")
# for i in range(len(color_data)):
#     if color_data[i]["family"].lower() == color_family_input.lower():
#         print("\n" + color_data[i]["name"])
#         print(color_data[i]["family"])
#         count += 1
# print("\n" + count)

# 5
color_letter_input = input("Please enter a letter: ")
count = 0
for i in range(len(color_data)):
    if color_data[i]["family"][0].lower() == color_letter_input.lower():
        print("\n" + color_data[i]["name"])
        print(color_data[i]["family"])
        count += 1

print("\n" + str(count))