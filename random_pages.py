""" BATCH FILE RANDOM PAGE PROCESSING """

# IMPORTS
import os
import tempfile
import random

from PyPDF2 import PdfFileReader
from tqdm import tqdm
from pdf2image import convert_from_path
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)

# LISTING ALL FILES IN THE SOURCE DIRECTORY
file_list = os.listdir("workspace/source/random")
file_count = 0

# PROVIDING THE ABSOLUTE PATH FOR POPPLER
abs_poppler_path = os.path.abspath("_internal/poppler-0.68.0/bin")

# ITTERATING THROUGH THE WHOLE LIST
if not file_list:
    print("\nNo files found")
    exit()
else:
    for i in file_list:
        file_count += 1
        print("\n\nFile", file_count, "out of", len(file_list))
        abs_pdf_path = os.path.abspath("workspace/source/random/"+i)

        # CHECKING PDF
        try:
            with open(abs_pdf_path, "rb") as filehandle:
                pdf = PdfFileReader(filehandle)
                page_count = pdf.getNumPages()
                print("\nProcessing: ", i, "(", page_count, "pages", ")")
        except:
            print("\nError in reading", i)
            print("Skipping . . .")
            continue
            print("Going down")


        # CREATING FOLDER
        if not os.path.exists("workspace/output/random/"+i):
            os.mkdir("workspace/output/random/"+i)
            abs_output_path = os.path.abspath("workspace/output/random/"+i+"/page")
        else:
            abs_output_path = os.path.abspath("workspace/output/random/"+i+"/page")

        # GENRATING THE LIST OF RANDOM PAGE NUMBERS
        number_of_pages_to_be_generated = round(page_count * 0.5)
        random_page_numbers = []
        if number_of_pages_to_be_generated >= 5:
            while len(random_page_numbers) < 5:
                random_page_numbers.clear()
                for p in range(0, 5):
                    n = random.randint(1, page_count)
                    if n in random_page_numbers:
                        continue
                    else:
                        random_page_numbers.append(n)
        else:
            while len(random_page_numbers) < number_of_pages_to_be_generated:
                random_page_numbers.clear()
                for p in range(0, number_of_pages_to_be_generated):
                    n = random.randint(1, page_count)
                    if n in random_page_numbers:
                        continue
                    else:
                        random_page_numbers.append(n)
        if len(random_page_numbers) == 0:
            random_page_numbers.append(1)
        print("\nSaving pages", random_page_numbers,"as images\n")     

        # EXTRACTING THE IMAGES
        for j in tqdm(random_page_numbers):
            try:
                with tempfile.TemporaryDirectory() as path:
                    pdf_images = convert_from_path(pdf_path=abs_pdf_path, poppler_path=abs_poppler_path, first_page=j, last_page=j, output_folder=path)
                    for page in pdf_images:
                        image_name = abs_output_path + str(j) + '.jpg'
                        page.save(image_name, 'JPEG')
            except: 
                print("Error in performing the required action")

"""
REQUIREMENTS:
    1. PyPDF2 -> pip install PyPDF2
    2. pdf2image -> pip install pdf2image
    3. tqdm -> pip install tqdm
"""