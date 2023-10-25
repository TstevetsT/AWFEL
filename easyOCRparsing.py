# This code is designed to parse the output of easyOCRtest and output a list with a list containing each row of data run the code by typing python easyOCRparsing.py <inputfilename>
import re
import sys  # Used to read commandline arguments

# edit the code here to read input from a file
 
# Reading from file
with open(sys.argv[1], "r+") as file1:
    # Reading form a file
    print(file1.read()) 
in_list=file1.read()
#in_list = ['Verizon', 'LTE', '1:38 AM', '57%/', 'Splits', 'h100 M', '150 M', '125 M', 'Pace/Strokes', '0\'35"/11', 'Distance', 'Pace', '25m', "0'26'/6", '2', '50m', '0\'25"/9', '3', '75m', '0\'22"/11', '100m', "0'28'/11", '5', '125m', "0'26'/11", '150m', '0\'31"/12', '175m', '0\'24"/10', '8', '200m', '0\'29"/12', '225m', "0'26'/11", '10', '250m', '0\'31"/12', '11', '275m', "0'26'/11", 'Avg-', 'Verizon', 'LTE', '1:38 AM', '57%/', 'Splits', 'h100 M', '150 M', '125 M', 'Pace/Strokes', '0\'35"/11', 'Distance', 'Pace', '12', '300m', '0\'31"/12', '13', '325m', '0\'31"/11', '14', '350m', "0'28'/11", '15', '375m', "0'29'/11", '16', '400m', '0\'31"/13', '17', '425m', '0\'28"/10', '18', '450m', '0\'33"/12', '19', '475m', "0'30'/10", '20', '500m', '0\'28"/10', '21', '525m', "0'29'/11", '22', '550m', "0'29'/11", 'Avg-', 'Verizon', 'LTE', '1:38 AM', '57%/', 'Splits', 'h100 M', '150 M', '125 M', 'Pace/Strokes', '0\'35"/11', 'Distance', 'Pace', '23', '575m', "0'30'/11", '24', '60m', '0\'30"/12', '25', '625m', '0\'28"/11', '26', '650m', '0\'33"/12', '27', '675m', '0\'23"/9', '28', '700m', '0\'39"/18', '29', '725m', "1'06'/8", '30', '750m', '0\'43"/15', '31', '775m', '0\'21"/8', '32', '800m', '0\'39"/16', '33', '825m', '0\'24"/7', 'Avg-', 'Verizon', 'LTE', '1:39 AM', '57%/', 'Splits', 'h100 M', '150 M', '125 M', 'Pace/Strokes', '0\'35"/11', 'Distance', 'Pace', '34', '850m', '0\'44"/18', '35', '875m', '0\'23"/9', '36', '90m', '0\'41"/18', '37', '925m', '0\'27"/7', '38', '950m', '0\'49"/20', '39', '975m', '0\'20"/8', '40', '1,000m', '0\'27"/11', '41', '1,025m', '0\'44"/17', '42', '1,050m', '0\'22"/8', '43', '1,075m', '0\'46"/18', '44', '1,100m', '0\'38"/15', 'Avg-', 'Verizon', 'LTE', '1:39 AM', '56%', 'Splits', 'h100 M', '150 M', '125 M', 'Pace/Strokes', '0\'35"/11', 'Distance', 'Pace', '45', '1,125m', '0\'44"/18', '46', '1,150m', '0\'23"/10', '47', '1,175m', '0\'27"/11', '48', '1,200m', '0\'48"/19', '49', '1,225m', '0\'21"\'/6', '50', '1,250m', '0\'45"/19', '51', '1,275m', '0\'23"/9', '52', '1,300m', '0\'21"/9', '53', '1,325m', '1\'37"\'/18', '54', '1,350m', '0\'42"/16', '55', '1,375m', '0\'26"/7', 'Avg-', 'Verizon', 'LTE', '1:39 AM', '56%', 'Splits', 'h100 M', '150 M', '125 M', 'Pace/Strokes', '0\'35"/11', 'Distance', 'Pace', '56', '1,400m', '0\'45"/18', '57', '1,425m', '0\'22"/10', '58', '1,450m', '0\'23"/10', '59', '1,475m', '0\'46"/18', '60', '1,500m', '0\'25"/7', '61', '1,525m', '0\'41"/17', '62', '1,550m', '0\'22"/10', '63', '1,575m', "0'26'/11", '64', '1,600m', '0\'43"/19', '65', '1,625m', '0\'25"/7', '66', '1,650m', '1\'40"/16', 'Avg-', 'Verizon', 'LTE', '1:39 AM', '56%', 'Splits', 'h100 M', '150 M', '125 M', 'Pace/Strokes', '0\'35"/11', 'Distance', 'Pace', '67', '1,675m', '0\'21"/8', '68', '1,700m', '0\'21"/10', '69', '1,725m', '0\'41"/18', '70', '1,750m', '0\'41"/16', '71', '1,775m', '0\'35"/15', '72', '1,800m', '0\'48"/18', '73', '1,825m', '0\'39"/15', '74', '1,850m', '0\'41"/16', '75', '1,875m', '0\'23"/9', '76', '1,900m', '0\'23"/10', '77', '1,925m', '0\'28"/11', 'Avg-', 'Verizon', 'LTE', '1:39 AM', '56%', 'Splits', 'h100 M', '150 M', '125 M', 'Pace/Strokes', '0\'35"/11', 'Distance', 'Pace', '78', '1,950m', '0\'24"/9', '79', '1,975m', '0\'25"/13', '80', '2,000m', '0\'33"/12', '81', '2,025m', '0\'24"/10', '82', '2,050m', "0'26'/12", '83', '2,075m', '0\'29"/12', '84', '2,100m', '0\'30"/11', '85', '2,125m', '0\'25"/10', '86', '2,150m', '0\'37"/12', '87', '2,175m', '0\'25"/9', '88', '2,200m', '0\'33"/11', 'Avg-', 'Verizon', 'LTE', '1.40 AM', '56%', 'Splits', 'h100 M', '150 M', '125 M', 'Pace/Strokes', '0\'35"/11', 'Distance', 'Pace', '89', '2,225m', '0\'22"/8', '90', '2,250m', '0\'26"/12', '91', '2,275m', "0'30'/11", '92', '2,300m', '0\'28"/11', '93', '2,325m', '0\'29"/10', '94', '2,350m', '0\'23"/10', '95', '2,375m', '0\'29"/12', '96', '2,400m', "0'29'/12", '97', '2,425m', "0'26'/11", '98', '2,450m', '0\'27"/11', '99', '2,475m', '0\'30"/12', 'Avg-', 'Verizon', 'LTE', '1.40 AM', '56%', 'Splits', 'h100 M', '150 M', '125 M', 'Pace/Strokes', '0\'35"/11', 'Distance', 'Pace', '91', '2,275m', '0\'30"/11', '92', '2,300m', '0\'28"/11', '93', '2,325m', '0\'29"/10', '94', '2,350m', '0\'23"/10', '95', '2,375m', '0\'29"/12', '96', '2,400m', '0\'29"/12', '97', '2,425m', "0'26'/11", '98', '2,450m', '0\'27"/11', '99', '2,475m', '0\'30"/12', '100', '2,500m', '3\'41"/11', '101', '2,525m', '1\'09"/9', 'Avg-']
out_list = []
meters=25
split=1
pattern = r'(\d+)\D+(\d+)\D+(\d+)'
for i in range(0, len(in_list)-2, 1):
    first = in_list[i]
    second = in_list[i+1]
    # need to remove the comma from the meters once over 999
    temp_second=""
    for char_val in second:
        temp_second=temp_second+char_val.strip(",")
    second=temp_second  
    
    third = in_list[i+2]
    print("checking:"+first+" "+second+" "+third)
    match = re.search(pattern, third)
    if (first.isdigit()) and (second.find(str(meters)+"m") != -1) and (match):
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
            meters += 25
    elif (second.find(str(meters)+"m") != -1) and (match):
        out_row = []
        first=split
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
            meters += 25
    elif (first.isdigit()) and (match):
        out_row = []
        out_row.append(first)
        second=str(meters)+"m"
        out_row.append(second)
        numbers = match.groups()  # Get the three matched numbers
        out_row.append(numbers[0])
        out_row.append(numbers[1])
        out_row.append(numbers[2])
        if (int(first) == split):
            print(out_row)
            out_list.append(out_row)
            split += 1
            meters += 25
    # Will probably need to edit this to do error correction if the split time formatting is so mangled that it won't match the regular expression
    # elif (first.isdigit()) and (second.find(str(meters)+"m") != -1):
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
    #         meters += 25
           
print(out_list)

# Writing to file
out_file=sys.argv[1]+"parsed_out"
with open(out_file, "w") as file1:
    # Writing data to a file
    file1.writelines(out_list)