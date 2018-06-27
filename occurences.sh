#!/bin/bash

for i in $(ls data_downloaded/); do
    echo $i ' \t ' $(wc -l data_downloaded/$i | cut -d" " -f1)
  done
