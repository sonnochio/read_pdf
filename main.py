import pdfplumber
import json
import os
import sys
#extract text from a pdf and store each page as a list item
#/Volumes/Extreme SSD/Quest Labs/project_gmail/project_gmail/generated_cvs

def main():

    argv = sys.argv[1]
    
    print("Path of the PDF:", argv)
    if not dir:
        print('Nothing entered, converting all pdfs in the current directory into JSON')
        dir='.'
    all_pdfs=[(os.path.join(dir,file),file) for file in os.listdir(dir) if file[-3:]=='pdf']

    text=[]

    for file in all_pdfs:
        pdf = pdfplumber.open(file[0])
        for page in pdf.pages:
            text.append(page.extract_text(layout=False))

        filename = file[1].replace('.pdf','')

        print(f'\n   ----- file name is  {filename}\n')

        data=json.dumps({'filename': filename, 'text':text})

        with open(f'{filename}.json','wb') as f:
            f.write(data.encode('utf-8'))

        print(f'Successfully extracted {filename}')


    return data



if __name__ == '__main__':
    main()
