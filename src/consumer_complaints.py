#---------------------#
# Using bitbucket     #
# Author: Sayan Basak #
# Main file           #
#---------------------#

import sys
import parse_csv

def usage_help():
    input_file = 'input/complaints.csv'
    output_file = 'output/report.csv'
    col_sep = ','
    empty_cell = ''

    print("Usage:")
    print('python[3] src/consumer_complaints.py'+' -h                      : Usage help')
    print('                                    '+' -i <input_file[.csv]>   : file name with relative path. No input defaults to '+str(repr(input_file)))
    print('                                    '+' -o <output_file[.csv]>  : file name with relative path. No output defaults to '+str(repr(output_file)))
    
def main(argv, verbose=False):
    input_file = 'input/complaints.csv'
    output_file = 'output/report.csv'
    
    arguments = len(sys.argv) - 1
    if (verbose):
        arguments -= 1
    if (arguments%2):
        usage_help()
    else:
        for i in range(int((arguments)/2)):
            if (sys.argv[i*2+1] == '-i'):
                input_file = (sys.argv[i*2+2])
            elif (sys.argv[i*2+1] == '-o'):
                output_file = (sys.argv[i*2+2])
            else:
                usage_help()
                sys.exit()
        
        print('Input File: '+str(repr(input_file)))
        
        # Parse file to list
        # print(parse_csv.read_file())
        print('Parsing File...',end='')
        data_in = parse_csv.parse_file_to_list(file_loc=input_file)
        print('Done!')

        # Manipulate data
        ## Extract necessary columns to dictionary
        required_columns = ['Date received', 'Product', 'Company']
        print('Extracting required Columns...',end='')
        data_in = parse_csv.list_to_dict(data_in, required_columns)
        print('Done!')
        
        ## Extract Year Received from Date Received
        print('Extracting Year...',end='')
        data_in = parse_csv.split_date(data_in, date_type='Date received')
        print('Done!')
        
        print('Deleting "Date received"...',end='')
        del data_in['Date received']
        print('Done!')
        
        print('Data Manipution...',end='')
        data_out = parse_csv.unique_products(data_in)
        print('Done!')
        
        # Store in file
        parse_csv.write_file(output_file, data_out)
        print('Output File: '+str(repr(output_file)))


if __name__ == "__main__":
    if (sys.argv[-1] == '-v'):
        main(sys.argv[1:], verbose=True)
    else:
        main(sys.argv[1:])