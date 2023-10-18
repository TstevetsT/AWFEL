# Apple Workout Fitness Export Linker (AWFEL) -python script that takes pictures of your swim workout splits as an input, uses OCR to convert to text, exports to excel, and provides analysis on best swim intervals.
# This is a work in progress.  Have ideas how to make it work thanks to skills aquired in VetsInTech Python course.  Thank You to Brion!
# Initial plan
# -Use pytesseract to extract text from photos    https://www.educative.io/answers/how-to-extract-text-from-an-image-in-python
# pip install pytesseract
# pip install pillow
# Install tesseract engine from https://github.com/UB-Mannheim/tesseract/wiki
import pytesseract
from PIL import Image

# open the image file
i0 = Image.open('IMG-1908.PNG')
i1 = Image.open('IMG-1909.PNG')
i2 = Image.open('IMG-1910.PNG')
i3 = Image.open('IMG-1911.PNG')
i4 = Image.open('IMG-1912.PNG')
i5 = Image.open('IMG-1913.PNG')
i6 = Image.open('IMG-1914.PNG')

# Perform OCR using pytesseract
# Need to edit this to auto import all files in folder
text = pytesseract.image_to_string(i0) + pytesseract.image_to_string(i1) + pytesseract.image_to_string(i2) + pytesseract.image_to_string(i3) + pytesseract.image_to_string(i4) + pytesseract.image_to_string(i5) + pytesseract.image_to_string(i6)

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
        line[0]=str(meters/25)   # These three lines provide error correction
        line[1]=str(meters)+"m"
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
    elif line.find("\'") != -1:
        line = line[:1] +"\'"+line[2:] # This corrects OCR error where ' is read as a 1, but code will break if a lap takes more than 9 min
        print(line)
        line=line.split("\'")
        # The line below multiplies min by 60 and sums with seconds
        line=int(line[0])*60+int(line[1][0]+line[1][1])
        if (row_right < row_left):
            table[row_right].append(line)
            # table[row_right].append(line[0])
            # table[row_right].append(line[1][0]+line[1][1])  # Ensures only first 2 chars 
            row_right += 1
print(table)


#   -Remove Extra/unnecessary Rows- can look for two \n in a row and delete one
#   -Format and save split number/total distance rows
#   -Format and save split times divided into a min and second column
# -Use Openpyxl to export data to worksheet for analysis
# -Add any other features that I come up with.