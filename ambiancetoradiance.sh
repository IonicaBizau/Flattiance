#!/bin/bash
# change colors in svg icon themes
# in the theme dir

for file in */*/*.svg; do
    mv $file $file.bak
	sed 's/'#dfdbd2'/'#3c3c3c'/g' $file.bak > $file	# main color
	echo 'file '$file' processed'
    rm $file.bak
done

for file in */*/*.svg; do
    mv $file $file.bak
	sed 's/'#000000'/'#ffffff'/g' $file.bak > $file	# highlight/shadow color 
	echo 'file '$file' processed'
    rm $file.bak
done
