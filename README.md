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

5. Remake keras model json

```
python run_keras_model_json_remake.py -load_json models/Keras_model_structure.json -load_prototxt models/deploy.prototxt -write_json models/Keras_model_structure_renew.json
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
The MIT License (MIT)

Copyright (c) 2015 Masaya Ogushi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
```

