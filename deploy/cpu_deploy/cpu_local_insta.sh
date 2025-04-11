#!/bin/bash
python3 -m pip install paddlepaddle==3.0.0rc0 -i https://www.paddlepaddle.org.cn/packages/stable/cpu/
pip3 install paddlex==3.0rc0
git clone https://github.com/PaddlePaddle/PaddleX.git
cd PaddleX
pip3 install -e .
