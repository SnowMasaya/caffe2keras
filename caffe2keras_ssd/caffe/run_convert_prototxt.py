import convert
import argparse
from convert_proto_text import ConvertProtoText

""" 

    USAGE EXAMPLE
        python caffe2keras.py -load_path 'deploy.prototxt.bk'

"""

parser = argparse.ArgumentParser(description='Converts a Caffe model to Keras.')
parser.add_argument('-prototxt', type=str,
                    help='name of the .prototxt file')
parser.add_argument('-store_file', type=str, default='',
                    help='path to the folder where the Keras model will be stored (default: -load_path).')

args = parser.parse_args()


def main(args):

    proto_file = args.prototxt
    convert_proto_file = args.store_file
    convert_text = ConvertProtoText(prototxt_file=proto_file,
                                         write_convert_file=convert_proto_file)

    print("Converting file...")
    convert_text.convert()

main(args)

