import os

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

import pprint
import tempfile
import matplotlib
import numpy as np
import tensorflow as tf
import tensorflow_models as tfm
import matplotlib.pyplot as plt

from PIL import Image

from official.core import exp_factory
from official.core import config_definitions as cfg
from official.vision.serving import export_saved_model_lib
from official.vision.ops.preprocess_ops import normalize_image
from official.vision.ops.preprocess_ops import resize_and_crop_image
from official.vision.utils.object_detection import visualization_utils
from official.vision.dataloaders.tf_example_decoder import TfExampleDecoder

pp = pprint.PrettyPrinter(indent=4) # Set Pretty Print Indentation

exp_