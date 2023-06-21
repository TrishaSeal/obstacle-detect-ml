# Helper script to split road_coco dataset
import os
import json
import shutil

rawImageDir = "../Dataset/road_coco/images"
trainImageDir = "../Dataset/road_coco/target/train"
validImageDir = "../Dataset/road_coco/target/valid"
trainAnnotPath = "../Dataset/road_coco/annotations/train.json"
validAnnotPath = "../Dataset/road_coco/annotations/valid.json"

def copyFilesOver(source, dest, fileList):
	file = open(fileList)
	parsedList = json.load(file)["images"]

	sourcePath = ''
	destPath = ''
	for f in parsedList:
		sourcePath = source + '/' + f["file_name"]
		destPath = dest + '/' + f["file_name"]
		shutil.copy(sourcePath, destPath)


copyFilesOver(rawImageDir, trainImageDir, trainAnnotPath)
copyFilesOver(rawImageDir, validImageDir, validAnnotPath)
