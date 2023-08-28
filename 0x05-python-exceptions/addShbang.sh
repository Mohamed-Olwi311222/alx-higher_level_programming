#!/bin/bash

for file in $@
do
	echo "#!/usr/bin/ptyhon3" >> "$file"
done
