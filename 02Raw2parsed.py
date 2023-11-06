# This code is designed to parse the output of easyOCRtest and output a list with a list containing each row of data run the code by typing python 02Raw2parsed.py <inputfilename>
import re
import sys  # Used to read commandline arguments

# Reading from file
in_file=sys.argv[1]

# Initialize an empty list to store the read lines
in_list = []

# Open the file for reading
with open(in_file, 'r') as file:
    for line in file:
        temp=line.strip()      # Remove trailing newline characters and add the line to the list
        in_list.append(re.sub("O", "0", temp))  #corrects error where OCR put O instead of zero
        
count = 0
value = []
for i in in_list:
    if 'm' in i:
        i=i.replace(',', '')
        value.append(int(i.strip('m')))
        count += 1
if value[1]-25 == 25:
    split_distance = 25
elif value[2]-value[1] == 25:
    split_distance =25
elif value[1]-50 == 50:
    split_distance = 50
elif value[2]-value[1] == 50:
    split_distance = 50
print("split distance detected as "+str(split_distance)+" meters")

out_list = []

total_distance = split_distance    
split=1
pattern = r'(\d+)\D+(\d+)\D+(\d+)'
for i in range(0, len(in_list)-2, 1):
    first = in_list[i]
    second = in_list[i+1]
    # need to remove the comma from the distance once over 999
    temp_second=""
    for char_val in second:
        temp_second=temp_second+char_val.strip(",")
    second=temp_second  
    
    third = in_list[i+2]
    print("checking:"+first+" "+second+" "+third)
    match = re.search(pattern, third)
    if (first.isdigit()) and (second.find(str(total_distance)+"m") != -1) and (match):
        out_row = []
        out_row.append(first)
        out_row.append(second)
        numbers = match.groups()  # Get the three matched numbers
        out_row.append(numbers[0])
        out_row.append(numbers[1])
        out_row.append(numbers[2])
        if (int(first) == split):
            print(out_row)
            out_list.append(out_row)
            split += 1
            total_distance += split_distance
    elif (second.find(str(total_distance)+"m") != -1) and (match):
        out_row = []
        first=str(split)
        out_row.append(first)
        out_row.append(second)
        numbers = match.groups()  # Get the three matched numbers
        out_row.append(numbers[0])
        out_row.append(numbers[1])
        out_row.append(numbers[2])
        if (int(first) == split):
            print(out_row)
            out_list.append(out_row)
            split += 1
            total_distance += split_distance
    elif (first.isdigit()) and (match):
        out_row = []
        out_row.append(first)
        second=str(total_distance)+"m"
        out_row.append(second)
        numbers = match.groups()  # Get the three matched numbers
        out_row.append(numbers[0])
        out_row.append(numbers[1])
        out_row.append(numbers[2])
        if (int(first) == split):
            print(out_row)
            out_list.append(out_row)
            split += 1
            total_distance += split_distance
    # Will probably need to edit this to do error correction if the split time formatting is so mangled that it won't match the regular expression
    # elif (first.isdigit()) and (second.find(str(total_distance)+"m") != -1):
    #     out_row = []
    #     out_row.append(first)
    #     out_row.append(second)
    #     numbers = match.groups()  # Get the three matched numbers
    #     out_row.append(numbers[0])
    #     out_row.append(numbers[1])
    #     out_row.append(numbers[2])
    #     if (int(first) == split):
    #         print(out_row)
    #         out_list.append(out_row)
    #         split += 1
    #         meters += split_distance
           
print(out_list)
    
# Writing to file

out_file=re.sub("\D", "", sys.argv[1])+"_parsed"  
with open(out_file, 'w') as f:
    for line in out_list:
        f.write(f"{line}\n")