## PDF-to-Image  
Convert PDF documents into images with single, batch or random pages processing.

![PDF to Image.png](https://i.postimg.cc/nhVpdyZ1/PDF-to-Image.png)

### Options
Effortlessly convert PDF onto images with a single execution of, 

`1. Convert Single File.exe`  
`2. Convert Batch File.exe`   
`3. Convert Random Pages.exe`  

### Download
[Windows 10](https://github.com/gokulmanohar/PDF-to-Image/releases)

### Organised
Every single execution format has its own output directory inside, where the script stores the output images. Also a Progress bar indicates the progress of the conversion.

### Usage
[_Note for contributors: Here the instructions are for [downloadable](#Download) .exe files. But the instructions are same while using .bat or .exe files_]

`1. Convert Single File.exe` Simple & straight-forward, run and pick a file.  

`2. Convert Batch File.exe` Place all the PDF documents in the *`workspace/source/batch`* directory, Run the bat file.  

`3. Convert Random Pages.exe`  Place all the PDF documents in the *`workspace/source/random`* directory, Run the bat file. Random pages within the documents will be saved.

### REQUIREMENTS [For contributers]  
[PyPDF2](https://pypi.org/project/PyPDF2/)
```
pip install PyPDF2
```
[pdf2image](https://pypi.org/project/pdf2image/)
```
pip install pdf2image
```
[tqdm](https://pypi.org/project/tqdm/)
```
pip install tqdm
```
