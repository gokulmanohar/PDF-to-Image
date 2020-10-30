""" SINGLE FILE PROCESSING """

# IMPORTS
import os
import tempfile

from tkinter import Tk
from tkinter.filedialog import askopenfilename
from tqdm import tqdm
from pdf2image import convert_from_path


# OPENING THE GUI FILE PICKER
Tk().withdraw()
abs_pdf_path = askopenfilename(filetypes=[('PDF Documents', '*.pdf')])
file_name = str(abs_pdf_path).split('/')[-1]

# PRINTING SELECTED FILE NAME
if not file_name:
    print("\nError in opening the file")
    exit()
else:
    print("\nSelected file:", file_name)
    print("\nProcessing . . .")

# PROVIDING THE ABSOLUTE PATH FOR POPPLER
abs_poppler_path = os.path.abspath("_internal/poppler/bin")

# CREATING FOLDER
if not os.path.exists("workspace/output/single/"+file_name):
    os.mkdir("workspace/output/single/"+file_name)
    abs_output_path = os.path.abspath("workspace/output/single/"+file_name+"/page")
else:
    abs_output_path = os.path.abspath("workspace/output/single/"+file_name+"/page")

# EXTRACTING THE IMAGES
page_number = 1
try:
    with tempfile.TemporaryDirectory() as path:
        pdf_images = convert_from_path(pdf_path=abs_pdf_path, poppler_path=abs_poppler_path, output_folder=path)
        print("\nTotal number of pages =", len(pdf_images),"\n")
        for page in tqdm(pdf_images):
            image_name = abs_output_path + str(page_number) + '.jpg'
            page.save(image_name, 'JPEG')
            page_number += 1
except: 
    print("Error in performing the required action")

"""
REQUIREMENTS:
    1. pdf2image -> pip install pdf2image
    2. tqdm -> pip install tqdm
"""
