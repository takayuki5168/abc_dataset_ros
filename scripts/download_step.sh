#!/bin/bash

SCRIPT_DIR=$(cd $(dirname $0); pwd)

mkdir -p $SCRIPT_DIR/../models
cd $SCRIPT_DIR/../models/

#curl -OL https://deep-geometry.github.io/abc-dataset/data/step_v00.txt
mkdir -p step
wget --no-check-certificate https://archive.nyu.edu/rest/bitstreams/88682/retrieve abc_0014_step_v00.7z -O step/abc_0014_step_v00.7z
cd step
7z x abc_0014_step_v00.7z

cd ..
mkdir -p step_test
cp -r step/0014000* step_test

