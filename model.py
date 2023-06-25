import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

# Import model
import tensorflow as tf
imported = tf.saved_model.load('./export-model/')
model_fn = imported.signatures['serving_default']

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