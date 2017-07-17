# Caffe ssd model convert to keras

Caffe model convert to keras for ssd model

## Description

Caffe ssd model convert to keras model weight

***DEMO:***


## Requirement

You prepare the caffe model

You will get the pretrain model following

https://github.com/weiliu89/caffe/tree/ssd

You provide the prototxt and caffe model

```
deploy.prototxt
*.caffemodel
```

## Usage

1. Convert to prototxt

```
python run_convert_prototxt.py -prototxt models/deploy.prototxt.bk -store_file models/deploy.prototxt
```

2. Convert to Caffe model to keras model

```
python caffe2keras.py -load_path models -prototxt deploy.prototxt -caffemodel VGG_VOC0712_SSD_300x300_iter_120000.caffemodel
```

## Installation

    $ git clone
    $ cd docker
    $ make build

## Anything Else


## Author

[@SnowGushiGit](https://twitter.com/SnowGushiGit)

## REFERENCE

[MarcBS/keras](https://github.com/MarcBS/keras/tree/master/keras/caffe)

## License

MIT

```

```

