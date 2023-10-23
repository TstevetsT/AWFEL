# Apple Workout Fitness Export Linker (AWFEL) -python script that takes pictures of your swim workout splits as an input, uses OCR to convert to text, exports to excel, and provides analysis on best swim intervals.
# This is a work in progress.  Have ideas how to make it work thanks to skills aquired in VetsInTech Python course.  Thank You to Brion!
# Initial plan
# -Use pytesseract to extract text from photos    https://www.educative.io/answers/how-to-extract-text-from-an-image-in-python
# pip install pytesseract
# pip install pillow
# Install tesseract engine from https://github.com/UB-Mannheim/tesseract/wiki
import pytesseract # Used to OCR images
import sys  # Used to read commandline arguments
from PIL import Image

# open the image file
# update this to take file inputs as command line arguments and process accordingly
# suggest it be run like this:  python .\awfel.py <first image num> <last image num>
# input_file_count=int(sys.argv[2])-int(sys.argv[1])+1
# print(sys.argv[1]+" "+sys.argv[2]+" "+str(input_file_count))
text=""
for i in range(int(sys.argv[1]),int(sys.argv[2])+1):
    in_filename="IMG-"+str(i)+".PNG"
    # Perform OCR using pytesseract after opening file
    text = text + pytesseract.image_to_string(Image.open(in_filename))
    
print(text)

#  This will remove all the undesired characters
text1=""
for char_val in text:
    text1=text1+char_val.strip("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklnopqrstuvwxyz.:[]/,=-")
text=text1.split("\n")



meters=25
row_left=0
row_right=0
table=[]
newline=""
text5=""
for i,line in enumerate(text,0):
    # This section of code will grab all the lines containing a line number and 
    # multiple of 25m and write them as the first two columns in a list of lists
    # called table
    # future work: detect the meter increments and process automagically
    if line.find(str(meters)+"m") != -1:
        line=line.split(" ")
        line_num=int(meters/25)
        total_meters=str(meters)+"m"
        line[0]=str(line_num)   # These three lines provide error correction
        line[1]=total_meters
        if (len(line) > 2):
            line.pop(2)
        table.append(line)
        meters += 25
        row_left += 1
    # This section of code grabs all the lines containing ' to get the time rows
    # Now I need to figure out how to parse out the extra rows and seperate the
    # minutes and seconds into seperate columns it is tricky because there is an 
    # unnecessary row above each set of meter rows and the ocr sometimes interprets
    # the second num break as "' OR '' OR "
    # maybe try to just grab the first two numbers seperated by ' and ignore the rest
    
    # Need to add handling to id and ignore repeated data from previous pictures
    # Idea:  In the if above check if input row number matches expected OR if input
    #        meters matches expected.  If this validation fails, decrement 
    
    elif line.find("\'") != -1:
        line = line[:1] +"\'"+line[2:] # This corrects OCR error where ' is read as a 1, but code will break if a lap takes more than 9 min
        line=line.split("\'")
        # The line below multiplies min by 60 and sums with seconds
        line=int(line[0])*60+int(line[1][0]+line[1][1])
        if (row_right < row_left):
            table[row_right].append(line)
            row_right += 1
print(table)


#   -Remove Extra/unnecessary Rows- can look for two \n in a row and delete one
#   -Format and save split number/total distance rows
#   -Format and save split times divided into a min and second column
# -Use Openpyxl to export data to worksheet for analysis
# -Add any other features that I come up with.