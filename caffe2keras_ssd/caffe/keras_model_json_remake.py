#!/usr/bin/python3
# -*- coding: utf-8 -*-
import re
import json


class KerasModelJsonRemake(object):

    def __init__(self, prototxt='', json_file='', prior_pram_add_json_file=''):
        self.prototxt = prototxt
        self.json_file = json_file
        self.proto_parm_dict_list = []
        self.json_keras_model_param = []
        self.json_data = None
        self.prior_pram_add_json_file = prior_pram_add_json_file
        self.param_name_list = ["aspect_ratio", "clip", "variance", "flip", "min_size", "max_size"]

    def remake_json(self):
        self.__proto_text_process()
        self.__read_kearas_model_json()
        self.__join_parameter()

    def __proto_text_process(self):
        with open(self.prototxt, "r") as f:
             proto_data = f.read()
        proto_data_remove_extra = re.sub('\s+', ' ', proto_data).strip()
        proto_data_seperate = proto_data_remove_extra.split('layer {')
        proto_data_seperate = [x.strip() for x in proto_data_seperate]
        for each_proto_data in proto_data_seperate:
            if "PriorBox" in each_proto_data:
                 prior_param = re.sub('{ | }', '', each_proto_data.split('prior_box_param ')[1])
                 split_prior_param = re.compile(": ([a-z]+|[0-9]+\.[0-9]+|[0-9]+)").split(prior_param)
                 self.__make_make_parameter(split_prior_param)

    def __make_make_parameter(self,split_prior_param ):
        name = ''
        tmp_name = ''
        each_param = ''
        param_list = []
        proto_parm_dict = {}
        for i, param in enumerate(split_prior_param):
            if i % 2 == 0:
                name = param.replace(' ', '')
                continue
            else:
                each_param = param
            if name not in self.param_name_list:
                continue
            if (name == 'aspect_ratio' or name == 'variance') and each_param != '':
                if name == 'aspect_ratio':
                    name = 'aspect_ratios'
                if name == 'variance':
                    name = 'variances'
                param_list.append(float(each_param))
                tmp_name = name
            if name != '' and each_param != '':
                if tmp_name != name:
                    param_list = []
                    tmp_name = ''
                if len(param_list) == 0:
                    if each_param == 'true' or each_param == 'false':
                        each_param = bool(each_param)
                    else:
                        each_param = float(each_param)
                    proto_parm_dict.update({name: each_param})
                else:
                    proto_parm_dict.update({name: param_list})
                name = ''
                each_param = ''
        self.proto_parm_dict_list.append(proto_parm_dict)

    def __read_kearas_model_json(self):
        with open(self.json_file) as json_data:
            self.json_data = json.load(json_data)
        for each_layer in self.json_data['config']['layers']:
            if each_layer['class_name'] == "PriorBox":
                self.json_keras_model_param.append(each_layer['config'])

    def __join_parameter(self):
        param_new_list = []
        for index, param in enumerate(self.json_keras_model_param):
            param_new = param.copy()
            param_new.update(self.proto_parm_dict_list[index])
            param_new_list.append(param_new)

        renew_index = 0
        for index, each_layer in enumerate(self.json_data['config']['layers']):
            if each_layer['class_name'] == "PriorBox":
                self.json_data['config']['layers'][index]['config'] = param_new_list[renew_index]
                renew_index += 1

        with open(self.prior_pram_add_json_file, "w") as jsonFile:
            json.dump(self.json_data, jsonFile)
