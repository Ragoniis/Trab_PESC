#!/bin/bash
for i in ~/Desktop/curriculos/*.zip;
do
	echo "$i"
	xbase=${i##*/}
	xpref=${xbase%.*}
	echo "$xpref"
	unzip -p $i curriculo.xml > $xpref.xml

done
