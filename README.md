# Caffe ssd model convert to keras

Caffe model convert to keras for ssd model

## Description

Caffe ssd model convert to keras model weight

![caffe to keras](https://d26dzxoao6i3hh.cloudfront.net/items/0v2j2c402o0e3J3r0x0B/Screenshot%20from%202017-07-18%2008%3A47%3A54.png)

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

1. Move to model and prottxt

```
mv {Your download folder}/deploy.prototxt caffe2keras/caffe2keras_ssd/caffe/models/
mv {Your download folder}/*.caffemodel caffe2keras/caffe2keras_ssd/caffe/models/
```

2. access to docker images

```
cd caffe2keras/docker
make bash
```

3. Convert to prototxt

```
python run_convert_prototxt.py -prototxt models/deploy.prototxt.bk -store_file models/deploy.prototxt
```

4. Convert to Caffe model to keras model

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

