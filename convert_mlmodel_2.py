import coremltools
import numpy
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.utils import np_utils
from keras.models import load_model


def convert_model(model):
	print('converting...')
	coreml_model = coremltools.converters.keras.convert(model,input_names=['image'],image_input_names='image')
	coreml_model.author = 'Leonard Schwenk'
	coreml_model.license = 'MIT'
	coreml_model.short_description = 'classify 8 image categories'
	coreml_model.save('./models/modelv4.3_8.categories.h5')
	print('model converted')


import os.path
if os.path.isfile('my_mnist_keras_cnn_model.h5'): 
	model = load_model('my_mnist_keras_cnn_model.h5')
	convert_model(model)
else:
	print('no model found')
