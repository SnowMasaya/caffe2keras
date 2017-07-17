#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
from convert_proto_text import ConvertProtoText
from util import File
from os import path
import filecmp
APP_ROOT = path.dirname(path.abspath("__file__"))
DATA_PATH='/home/caffe2keras/caffe2keras_ssd/caffe/tests'


class Test_Convert(unittest.TestCase):

    def setUp(self):
        self.proto_file = DATA_PATH + '/test_deploy.prototxt'
        self.convert_proto_file = DATA_PATH + '/convert_proto.txt'
        self.answer_convert_proto_file = DATA_PATH + '/answer_convert.prototxt'
        self.convert_text = ConvertProtoText(prototxt_file=self.proto_file,
                                              write_convert_file=self.convert_proto_file)

    def test_convert(self):
        self.convert_text.convert()
        self.assertEqual(True, filecmp.cmp(self.answer_convert_proto_file,
                                           self.convert_proto_file))

    def tearDown(self):
        File.remove_file(self.convert_proto_file)


if __name__ == '__main__':
    unittest.main()
