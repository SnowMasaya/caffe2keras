from keras.models import Sequential, model_from_json
from keras.optimizers import SGD
from ssd_layers import PriorBox

from scipy import misc
import numpy as np
import copy
from os import path
APP_ROOT = path.dirname(path.abspath("__file__"))
DATA_PATH='/home/caffe2keras/caffe2keras_ssd/caffe/'


if __name__ == "__main__":

    out_layer_names = ['predictions']

    print "Preparing test image."
    # Read image
    im = misc.imread(DATA_PATH + 'models/cat.jpg')

    # Resize
    im = misc.imresize(im, (300, 300)).astype(np.float32)

    # Change RGB to BGR
    aux = copy.copy(im)
    im[:, :, 0] = aux[:, :, 2]
    im[:, :, 2] = aux[:, :, 0]

    # Remove train image mean
    im[:, :, 0] -= 104.006
    im[:, :, 1] -= 116.669
    im[:, :, 2] -= 122.679

    # Transpose image dimensions (Keras' uses the channels as the 1st dimension)
    # im = np.transpose(im, (0, 1, 2))

    # Insert a new dimension for the batch_size
    im = np.expand_dims(im, axis=0)

    # Load the converted model
    print
    "Loading model."
    model_data = open(DATA_PATH + 'models/Keras_model_structure_renew.json').read()
    # Load model structure
    model = model_from_json(model_data, custom_objects={'PriorBox': PriorBox})
    # Load model weights
    model.load_weights(DATA_PATH + 'models/Keras_model_weights.h5')

    # Compile converted model
    print "Compiling model."
    sgd = SGD(lr=0.1, decay=1e-6, momentum=0.9, nesterov=True)
    loss = dict()
    for out in out_layer_names:
        loss[out] = 'categorical_crossentropy'
        last_out = out
    model.compile(optimizer=sgd, loss=loss)

    # Predict image output
    print "Applying prediction."
    in_data = dict()
    for input in ['input_1']:
        in_data[input] = im
    out = model.predict(in_data)

    # Load ImageNet classes file
    classes = []
    with open(DATA_PATH + 'models/classes.txt', 'r') as list_:
        for line in list_:
            classes.append(line.rstrip('\n'))

    model.summary()