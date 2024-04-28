#!/bin/bash

echo "Enter the path of the file of which you want to see the size"

read path

size=$(du -sh $path)

echo "The size of the file $path is: $size"




