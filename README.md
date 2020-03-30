# Consumer Complaints (Insights Data-Science Challenge question)

## Table of Contents
1. [Problem Statement](README.md#problem_statement)
1. [Usage Instructions](README.md#usage_instructions)
1. [Complaints](README.md#complaints)

## Problem Statement
[Here](https://github.com/InsightDataScience/consumer_complaints/blob/master/README.md#consumer-complaints) is the full description of the problem.

This repository contains some basic functionality of reading a '.csv' file to a list/dictionary. 

Constructing the required report after processing the input data with column names:
 
| Product | Year | Total | Max('company') | (Max/Total)% |
| ------- | ---- | ----- | -------------- | ------------ |

*Output does not contain these column headers.*

## Usage Instructions

`bash run.sh <path_to_input_output_folder>` [path required]

* <path_to_input_output_folder> - directory should contain 'input/complaints.csv', this will create output and store report.csv insideit

#### OR

`python3 src/consumer_complaints.py [ (optional) -i '<input_file_name_with_path>' -o '<output_file_name_with_path>' ]`

* `<input_file_name_with_path>` - file name with relative path in linux style. No input defaults to './input/complaints.csv'.
* `<output_file_name_with_path>` - file name with relative path in linux style. No input defaults to './output/report.csv'.

## Complaints
Email: [basak@purdue.edu](mailto:basak@purdue.edu)

### Disclaimer
Use at your own risk!