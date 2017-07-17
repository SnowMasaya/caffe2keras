#!/usr/bin/python3
# -*- coding: utf-8 -*-
import re
import numpy as np
import subprocess
import os
import sys
import json


class File(object):
    """
    Common File Method
    """

    @classmethod
    def read_file_return_list(cls, datapath, dataset):
        """
        File read method
        :param file_name(str): setting the file name
        :return(list): return the data list:w
        """
        read_data = []
        try:
            with open(datapath + dataset, "r") as f:
                read_data = f.read().strip().split()
        except IOError as io:
            print(str(io))
        return read_data

    @classmethod
    def write_file(cls, datapath, dataset, write_data):
        """
        File read method
        :param file_name(str): setting the file name
        :return(list): return the data list:w
        """
        try:
            with open(datapath + dataset, 'w') as f:
                f.write(str(write_data))
        except IOError as io:
            print(str(io))

    @classmethod
    def remove_file(cls, filename):
        try:
            subprocess.call("rm -rf " + filename, shell=True)
        except subprocess.CalledProcessError as cpe:
            print(str(cpe))

    @classmethod
    def read_file_from_list(cls, data_path, feature_list_name):
        # Read the Feature list
        read_data = File.read_file_return_list(data_path,
                                               feature_list_name)
        tmp_list = []
        label = []
        for data in read_data:
            label.append(re.sub("^.*\/|\_[0-9]+|.npy", "", data))
            feature = np.loadtxt(data_path + data)
            tmp_list.append(feature)
        return np.array(tmp_list), np.array(label)

    @classmethod
    def check_file_exist(cls, file_name):
        """
        Check exist file
        :param file_name(str): setting the file name
        """
        if not os.path.exists(file_name):
            print("[!] File does not exist '{0}'".format(file_name))
            sys.exit(-1)

    @classmethod
    def read_form_json(cls, file_name):
        """
        Read json file
        :param file_name: 
        :return: 
        """
        json_data = []
        try:
            with open(file_name, "r", encoding='utf-8') as f:
                json_data = json.load(f, encoding='utf8')
        except IOError as io:
            print(str(io))
        return json_data
