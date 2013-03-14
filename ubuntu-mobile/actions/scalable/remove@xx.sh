#!/bin/bash
for file in $(ls *.svg)
do
	mv $file ${file%%@*}.svg
done
