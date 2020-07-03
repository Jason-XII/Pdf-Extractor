# PDF Extractor
 PDF documents are very popular and widely used. Sometimes, we want to operate with the pdf files,  like turning them into another format like Word. There are many tools on line that can operate them, but often have page limits. If you want to extract the tables from a PDF and turn them into excel files, you can use this tool to extract the pages with the tables on them and turn them into excels using altopdf(An online tool that I recommend)

This is picture when the program runs:

<img src='screen shot.bmp'>



## How to use it?

First, click the select file button, and wait to see a file dialog pop up. **After** you have selected, choose the page to start extract and where to end. There are no page limits, so *remember* your index is right, or the program will exit because of an error. **Next**, click "Add Record“ to add the start index and end index to the list on the right. **Finally**, enter the filename with the ".pdf" suffix and click "Extract". If there is no error, a success dialog will pop up.

Tip: You can choose more than one pdf file to extract.

## Requirements

This program requires two PyPi packages, PyQt5 and PyPDF2. to install them, enter the following code into your command prompt:

```bash
pip install PyQt5
pip install PyPDF2
```

## Bugs

There are no certain bugs for now. But if you found a bug, please report it in the "Issue" section. I will do my  best to fix them. This package is only tested on python 3, so if you are using python 2 or lower, I don't know if this is going to work.