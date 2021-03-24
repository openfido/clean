#!/bin/bash
VERSION=0
set -u
set -e
set -x
python3 src/clean.py -i ${OPENFIDO_INPUT} -o ${OPENFIDO_OUTPUT} -c ${OPENFIDO_INPUT/config.csv}
