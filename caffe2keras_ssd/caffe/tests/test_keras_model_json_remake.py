#!/usr/bin/python3
# -*- coding: utf-8 -*-
import unittest
from keras_model_json_remake import KerasModelJsonRemake
from keras.models import model_from_json
from ssd_layers import PriorBox
from util import File
from os import path
import filecmp
APP_ROOT = path.dirname(path.abspath("__file__"))
DATA_PATH='/home/caffe2keras/caffe2keras_ssd/caffe/tests/'


class Test_Convert(unittest.TestCase):

    def setUp(self):
        self.proto_file = DATA_PATH + '/test_deploy.prototxt'
        self.json_file = DATA_PATH + '/test_Keras_model_structure.json'
        self.prior_pram_add_json_file = DATA_PATH + '/test_Keras_model_structure_renew.json'
        self.answer_prior_pram_add_json_file = DATA_PATH + '/answer_Keras_model_structure_renew.json'
        self.keras_model_json_remake = KerasModelJsonRemake(
            prototxt=self.proto_file,
            json_file=self.json_file,
            prior_pram_add_json_file=self.prior_pram_add_json_file
        )

    def test_remake_json(self):
        self.keras_model_json_remake.remake_json()
        model_data = open(self.prior_pram_add_json_file).read()
        # Load model structure
        model = model_from_json(model_data, custom_objects={'PriorBox':PriorBox})
        model.summary()

        self.assertEqual(True, filecmp.cmp(self.prior_pram_add_json_file,
                                           self.answer_prior_pram_add_json_file))

    def tearDown(self):
        File.remove_file(self.prior_pram_add_json_file)


if __name__ == '__main__':
    unittest.main()