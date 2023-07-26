#!/bin/bash

LIBS=$(find lib -name libcublas*.so* -o -name libcuda*.so*)
KM=../../km-gpu

for l in $LIBS
do
	dir=$(dirname $l)
	name=$(basename $l)
	link=$(realpath --relative-to=$dir ${KM}/build/opt/kontain/lib/$name)

	ln -sf $link $l
	ls -lL $l
done


