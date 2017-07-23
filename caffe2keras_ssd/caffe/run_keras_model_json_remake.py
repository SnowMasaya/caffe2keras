#!/usr/bin/python3
# -*- coding: utf-8 -*-
import argparse
from keras_model_json_remake import KerasModelJsonRemake
from keras.models import model_from_json
from ssd_layers import PriorBox

""" 

    USAGE EXAMPLE
        python run_keras_model_json_remake.py -load_json 'Keras_model_structure.json' -write_json 'Keras_model_structure_renew.json -load_prototxt 'deploy.prototxt' '

"""


parser = argparse.ArgumentParser(
    description='Renew Keras model json.')
parser.add_argument('-load_json', type=str,
                    help='path load keras model json')
parser.add_argument('-load_prototxt', type=str,
                    help='path load prototxt')
parser.add_argument('-write_json', type=str,
                    help='path write keras model json')

args = parser.parse_args()


def main(args):

    print("Renewal Json...")
    keras_model_json_remake = KerasModelJsonRemake(
        prototxt=args.load_prototxt,
        json_file=args.load_json,
        prior_pram_add_json_file=args.write_json
    )

    keras_model_json_remake.remake_json()
    pre_train_model_data = open(args.write_json).read()

    pre_train_model = model_from_json(pre_train_model_data,
                                      custom_objects={'PriorBox': PriorBox})
    pre_train_model.summary()


main(args)

