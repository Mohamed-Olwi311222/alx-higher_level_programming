#!/bin/bash

for file in $@
do
	echo "#!/usr/bin/python3" >> "$file"
done
