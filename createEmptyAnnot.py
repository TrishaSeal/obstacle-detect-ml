import json
from PIL import Image

annotContent = {}

imageList = []
image = Image.open("./static/files/test.jpg")
imInfo = {
	"file_name": "test.jpg",
	"height": image.size[1],
	"width": image.size[0],
	"id": 0
}
imageList.append(imInfo)

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
filePath = "./static/files/test.json"

with open(filePath, mode = "w") as file:
	file.write(fileContent)