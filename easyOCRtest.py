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