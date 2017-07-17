#!/usr/bin/python3
# -*- coding: utf-8 -*-
import re


class ConvertProtoText(object):
    """
    Prototxt convert to follwing format

    layer {
      name: "input"
      type: "Input"
      top: "data"
      input_param {
        # These dimensions are purely for sake of example;
        # see infer.py for how to reshape the net to the given input size.
        shape { dim: 1 dim: 3 dim: 500 dim: 500 }
      }
    }


    """

    def __init__(self, prototxt_file='', write_convert_file=''):
        """
        Setting file name
        :param prototxt_file(str): inpu proto file
        :param write_convert_file(str): write convert file 
        """
        self.prototxt_file = prototxt_file
        self.write_convert_file = write_convert_file
        self.template_input = ['layer {',
                               '  name: "input_1"',
                               '  type: "Input"',
                               '  top: "data"',
                               '  input_param {',
                               '    shape { dim: %d dim: %d dim: %d dim: %d }',
                               '}}']
        self.check_dim = '    shape { dim: %d dim: %d dim: %d dim: %d }'

    def convert(self):
        """
        Convert process for caffe to keras proto.txt format
        """
        with open(self.prototxt_file, "r") as f:
            read_data = f.read()

        split_line = read_data.split('\n')

        replace_line_number, dim_list = self.__replace_data(split_line)

        templeate_count = 0
        for i in range(len(split_line)):
            if i in replace_line_number:
                if self.check_dim == self.template_input[templeate_count]:
                    split_line[i] = '    shape { dim: %d dim: %d dim: %d dim: %d }' % (
                    dim_list[0], dim_list[1], dim_list[2], dim_list[3])  # noqa
                else:
                    split_line[i] = self.template_input[templeate_count]
                templeate_count += 1

        with open(self.write_convert_file, 'w') as f:
            for data in split_line:
                f.write(data)
                f.write('\n')

    def __replace_data(self, split_line):
        """
        Check replace point
        :param split_line(list): input proto.txt data 
        :return: replace number and dimension list 
        """
        replace_line_number = []
        dim_list = []
        input_flag = False
        for i in range(len(split_line)):
            if 'input: "data"' == split_line[i]:
                input_flag = True
            if input_flag == True:
                replace_line_number.append(i)
                if 'dim' in split_line[i]:
                    dim_list.append(int(split_line[i].replace('  dim: ', '')))
            if '}' == split_line[i] and input_flag == True:
                input_flag = False
        return replace_line_number, dim_list
