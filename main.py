import pdfplumber
import sys
import json
import os
#extract text from a pdf and store each page as a list item

def main():
    file=input('input the pdf directory \n')
    text=[]
    pdf = pdfplumber.open(file)
    for page in pdf.pages:
        text.append(page.extract_text(layout=False))

    filename = pdf.stream.name
    data=json.dumps({'filename': filename, 'text':text})

    with open(f'pdf.json','wb') as f:
        f.write(data.encode('utf-8'))

    print(f'Successfully extracted pdf and saved as a json file')


    return data



if __name__ == '__main__':
    main()
