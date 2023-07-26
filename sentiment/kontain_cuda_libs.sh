#!/bin/bash

ln -sf ../../km-gpu/build/opt/kontain/lib/libcudart.so.11.0 ./lib/python3.11/site-packages/nvidia/cuda_runtime/lib/libcudart.so.11.0
ln -sf libcudart.so.11.0 ./lib/python3.11/site-packages/nvidia/cuda_runtime/lib/libcudart.so
ln -sf ../../km-gpu/build/opt/kontain/lib/libcublas.so.11 ./lib/python3.11/site-packages/nvidia/cublas/lib/libcublas.so.11
ln -sf ../../km-gpu/build/opt/kontain/lib/libcublasLt.so.11 ./lib/python3.11/site-packages/nvidia/cublas/lib/libcublasLt.so.11
ln -sf libcublas.so.11 ./lib/python3.11/site-packages/nvidia/cublas/lib/libcublas.so
ln -sf libcublasLt.so.11 ./lib/python3.11/site-packages/nvidia/cublas/lib/libcublasLt.so

