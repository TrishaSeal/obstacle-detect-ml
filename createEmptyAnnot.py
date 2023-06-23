import os
import json

annotContent = {}

imageList = []
imagePath = "../Dataset/Testing Frames/"
i = 0
for root, folders, im in os.walk(imagePath):
	for image in im:
		imInfo = {
			"file_name": image,
			"height": 1080,
			"width": 1920,
			"id": i
		}
		imageList.append(imInfo.copy())
		i += 1

print(imageList)

annotContent["images"] = imageList
annotContent["type"] = "instances"
annotContent["annotations"] = []
annotContent["categories"] = [\
	{
		"supercategory": "none",
		"id": 1,
		"name": "speedlimit"
	},
	{
		"supercategory": "none",
		"id": 2,
		"name": "crosswalk"
	},
	{
		"supercategory": "none",
		"id": 3,
		"name": "trafficlight"
	},
	{
		"supercategory": "none",
		"id": 4,
		"name": "stop"
	}
]

enc = json.encoder.JSONEncoder()
fileContent = enc.encode(annotContent)
filePath = "../Dataset/Testing Frames/test.json"

with open(filePath, mode = "w") as file:
	file.write(fileContent)