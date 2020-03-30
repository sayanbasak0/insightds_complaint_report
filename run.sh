#!/bin/bash

# python3 src/consumer_complaints.py -i 'input/complaints.csv' -o 'output/report.csv'
# python3 src/consumer_complaints.py -i 'insight_testsuite/tests/test_1/input/complaints.csv' -o 'insight_testsuite/tests/test_1/output/report.csv'
# python3 src/consumer_complaints.py -i 'insight_testsuite/tests/my_test/input/complaints.csv' -o 'insight_testsuite/tests/my_test/output/report.csv'

if [ $# -eq 0 ]; then
    echo "Syntax: bash run.sh 'path_to_input_directory'"
    exit 0
fi

home_pwd=`pwd`
cd $1
cd input
input_pwd=`pwd`
cd ../
mkdir -p "output"
cd output
output_pwd=`pwd`
cd $home_pwd

python3 src/consumer_complaints.py -i "${input_pwd}/complaints.csv" -o "${output_pwd}/report.csv"
