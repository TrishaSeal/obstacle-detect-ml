# Helper script to split road_coco dataset
import os
import json
import shutil

rawImageDir = "../Dataset/road_coco/images"
trainImageDir = "../Dataset/road_coco/target/train"
validImageDir = "../Dataset/road_coco/target/valid"
testImageDir = "../Dataset/Testing Frames"
trainAnnotPath = "../Dataset/road_coco/annotations/train.json"
validAnnotPath = "../Dataset/road_coco/annotations/valid.json"
testAnnotPath = "../Dataset/Testing Frames/test.json"

def copyFilesOver(source, dest, fileList):
	file = open(fileList)
	parsedList = json.load(file)["images"]

	sourcePath = ''
	destPath = ''
	for f in parsedList:
		sourcePath = source + '/' + f["file_name"]
		destPath = dest + '/' + f["file_name"]
		shutil.copy(sourcePath, destPath)


#copyFilesOver(rawImageDir, trainImageDir, trainAnnotPath)
#copyFilesOver(rawImageDir, validImageDir, validAnnotPath)

trainRecordPath = '../Dataset/road_coco/records/train'
validRecordPath = '../Dataset/road_coco/records/valid'
testRecordPath = '../Dataset/road_coco/records/test'

def createRecord(imageDir, annotPath, recordPath):
	cmd = [
		"python3 -m official.vision.data.create_coco_tf_record ",
		"--logtostderr ",
		"--image_dir=\"" + imageDir + "\" ",
		"--object_annotations_file=\"" + annotPath + "\" ",
		"--output_file_prefix=\"" + recordPath + "\" ",
		"--num_shards=1"
	]
	fullcmd = ""
	for c in cmd:
		fullcmd += c
	os.system(fullcmd)

# createRecord(trainImageDir, trainAnnotPath, trainRecordPath)
# createRecord(validImageDir, validAnnotPath, validRecordPath)
createRecord(testImageDir, testAnnotPath, testRecordPath)