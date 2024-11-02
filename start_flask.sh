#!/usr/bin/bash

file_name=$(basename $1 .py);
echo "file name : $file_name"

python3 -m web_flask.$file_name && \
curl 0.0.0.0:5000 ; echo "" | cat -e
