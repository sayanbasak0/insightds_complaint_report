#---------------------#
# using bitbucket     #
# author: Sayan Basak #
# Helper file         #
#---------------------#

def read_file(filename="input/complaints.csv"):
    '''Read the given filename'''
    with open(filename,mode='r+') as f:
        data = f.read()
    return data

def parse_lines_to_list(input_str,delimiter=",",quotes='\"',empty_field=''):
    '''Make a list of list from the given filename, 
    splitting at delimiter and newlines which are not enclosed in quotes ("")'''

    l = ''
    for i,item in enumerate(input_str.split(quotes)):
        if (i%2):
            l = l+quotes+item+quotes
        else:
            l = l+('\"\n\"'.join(item.splitlines()))
    
    input_str = l
    input_str = input_str.split('\"\n\"')
    input_str = [l for l in input_str if(l!='')]
    data_ret = []
    
    for line in input_str:
        l = ''
        for i,item in enumerate(line.split(quotes)):
            if (i%2):
                l = l+quotes+item+quotes
            else:
                l = l+('\",\"'.join(item.split(delimiter)))
        data_ret.append(l.split('\",\"'))
    
    return data_ret

def list_to_dict(data_in, col_headers=''):
    '''Make a dictionary from the required data columns'''

    dict_out = {}
    if (len(col_headers)==0):
        col_headers = data_in[0]
    for label in col_headers:
        dict_out[label] = []
        
    for i in range(1,1+len(data_in[1:])):
        for j in range(len(data_in[i])):
            if (data_in[0][j] in col_headers):
                dict_out[data_in[0][j]].append(data_in[i][j])
    return dict_out

def parse_file_to_list(file_loc="input/complaints.csv",delimiter=",",quotes='\"',empty_field=''):
    '''Return data from the given input file'''

    data_in = read_file(file_loc)
    data_out = parse_lines_to_list(data_in,delimiter=delimiter,quotes=quotes,empty_field=empty_field)
    
    return data_out

def split_date(input_dict, date_type='Date received'):
    '''Splits date to extract year'''

    input_dict['Year-'+date_type] = []
    
    for date in input_dict[date_type]:
        DMY = date.split('-')
        for Y in DMY:
            if (len(Y)==4):
                input_dict['Year-'+date_type].append(Y)
    return input_dict

def write_file(filename="output/report.csv",data=[[]]):
    '''Write data of list of list into filename'''

    with open(filename,mode='w+') as f:
        for line in data:
            for item in line[:-1]:
                f.write(str(item)+',')
            f.write(str(line[-1])+'\n')

def unique_products(input_data):
    '''Count products by year,
    find maximum complaints filed against a single company,
    calculate (maximum complaints against a single company/total complaints).'''
    report_list = []
    temp_dict = {}
    for p,y,c in zip(input_data['Product'],input_data['Year-Date received'],input_data['Company']):
        try:
            temp_dict[p.lower()+','+y][0] += 1
        except:
            temp_dict[p.lower()+','+y] = [1,{}]
        try:
            temp_dict[p.lower()+','+y][1][c.lower()] += 1
        except:
            temp_dict[p.lower()+','+y][1][c.lower()] = 1
        
    for cols in temp_dict:
        temp = []
        temp.append(cols[:-5])
        temp.append(int(cols[-4:]))
        temp.append(temp_dict[cols][0])
        temp.append(0)
        temp.append(0)
#         temp.append('company')
        for company in temp_dict[cols][1]:
            if (temp_dict[cols][1][company] > temp[3]):
                temp[3] = temp_dict[cols][1][company]
#                 temp[5] = company
        temp[4] = int(round(100.0*temp[3]/temp[2]))
        report_list.append(temp)

#     report_list.sort()
    report_list = sorted( report_list, key=lambda x: x[1] )
    report_list = sorted( report_list, key=lambda x: x[0] )
    return report_list
