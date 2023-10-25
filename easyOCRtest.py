# From: https://pyimagesearch.com/2020/09/14/getting-started-with-easyocr-for-optical-character-recognition/
# import the necessary packages
import easyocr
import sys  # Used to read commandline arguments

reader = easyocr.Reader(['en'])
result=[]
for i in range(int(sys.argv[1]),int(sys.argv[2])+1):
    in_filename="IMG-"+str(i)+".PNG"
    # Perform OCR using pytesseract after opening file
    result = result + reader.readtext(in_filename, detail = 0)
    print(in_filename+" import complete")
print(result)

# Writing to file
out_file=sys.argv[1]+"out"
with open(out_file, "w") as file1:
    # Writing data to a file
    file1.writelines(result)