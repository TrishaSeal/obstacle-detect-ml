# Handling Tensorflow Verbosity intensity
import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

# Integrating exported model into web app
# @~Trisha: This section will need to be commented out, just uncomment the lines with triple set of double quotes to comment it out
#"""
import numpy as np
from PIL import Image
import tensorflow as tf

from official.vision.ops.preprocess_ops import resize_and_crop_image
from official.vision.utils.object_detection import visualization_utils
from official.vision.dataloaders.tf_example_decoder import TfExampleDecoder


model = tf.saved_model.load('./export-model/')
modelFn = model.signatures['serving_default']
tfExDecoder = TfExampleDecoder()

categoryIndex = {
	0: {
		'id': 0,
		'name': "speedlimit"
	},
	1: {
		'id': 1,
		'name': "crosswalk"
	},
	2: {
		'id': 2,
		'name': "trafficlight"
	},
	3: {
		'id': 3,
		'name': "stop"
	}
}


def build_inputs_for_object_detection(image, input_image_size):
	image, _ = resize_and_crop_image(
		image,
		input_image_size,
		padded_size=input_image_size,
		aug_scale_min=1.0,
		aug_scale_max=1.0)
	return image

def make_prediction():
	testDs = tf.data.TFRecordDataset('./static/files/test-00000-of-00001.tfrecord')
	inputImageSize = (256, 256)
	minScore = 0.3

	for _, image in enumerate(testDs):
		decoded = tfExDecoder.decode(image)
		image = build_inputs_for_object_detection(decoded['image'], inputImageSize)
		image = tf.expand_dims(image, axis = 0)
		image = tf.cast(image, dtype = tf.uint8)
		pred = modelFn(image)

		output = visualization_utils.visualize_boxes_and_labels_on_image_array(
			image[0].numpy(),
			pred['detection_boxes'][0].numpy(),
			pred['detection_classes'][0].numpy().astype(int),
			pred['detection_scores'][0].numpy(),
      		category_index=categoryIndex,
      		use_normalized_coordinates=False,
      		max_boxes_to_draw=200,
      		min_score_thresh=minScore,
      		agnostic_mode=False,
      		instance_masks=None,
      		line_thickness=4
		)

		outputFile = Image.fromarray(output)
		outputFile.save('./static/files/output.png')

#"""

# Initiating web app
from flask import Flask, render_template
from flask_wtf import FlaskForm
from werkzeug.utils import secure_filename
from wtforms import FileField, SubmitField
from wtforms.validators import InputRequired
from datasetManage import createRecord


app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = 'static/files'

class UploadFileForm(FlaskForm):
	file = FileField("File", validators=[InputRequired()])
	submit = SubmitField("Upload File")

@app.route('/', methods=['GET',"POST"])
@app.route('/home', methods=['GET',"POST"])
def home():
	form = UploadFileForm()
	if form.validate_on_submit():
		file = form.file.data 
		fileExt = file.filename.split('.')[1]
		file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],'test' + "." + fileExt))
		createRecord('./static/files/', './static/files/test.json', './static/files/test')
		os.system("python createEmptyAnnot.py")
	return render_template('mainpage.html', form=form)

if __name__ == '__main__':
	app.run(debug=True)