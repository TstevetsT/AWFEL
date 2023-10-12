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
image = Image.open('IMG-1809.PNG')

# Perform OCR using pytesseract
text = pytesseract.image_to_string(image)
print(text)

# -Use string/text to format the data
# -Use Openpyxl to export data to worksheet for analysis
# -Add any other features that I come up with.