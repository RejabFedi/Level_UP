from pytesseract import image_to_string
from PIL import Image
import string


def convertBook(FileName):
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        text =image_to_string(Image.open(FileName))

        with open('FileNameOut.txt', mode='w') as f:
            f.write(text)
            text.replace('\n\n','\n')
        return f.name


def readBookFile(fileName):
    l = []
    with open(fileName, 'r') as file:
        for line in file:
            for word in line.split():
                word = (''.join([x for x in word if x in string.ascii_letters + '\'- ']))
                l.append(word)
    for i in l:
        if i == '':
            l.remove(i)

    return l
readedList= readBookFile(convertBook('1.PNG'))

if __name__ == "__main__":
    print(readBookFile(convertBook('1.PNG')))
