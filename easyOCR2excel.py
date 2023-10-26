# This code is designed to take easyOCR parsed file with a list of 5 element lists (Lap number, total distance in meters, minutes, seconds, strokes/split(lap) and writes them into an excel workbook that analyzes the output of easyOCRtest and output a list with a list containing each row of data run the code by typing python easyOCR2excel.py <inputfilename> 
#  python easyOCR2excel.py 1960outparsed_out 
import re
import sys  # Used to read commandline arguments

# Reading from file
in_file=sys.argv[1]

# Initialize an empty list to store the read lines
in_list = []

# Open the file for reading
with open(in_file, 'r') as file:
    for line in file:
        # Remove trailing newline characters and add the line to the list
        print(line)
        in_list.append(line.strip())      
        
print(in_list)