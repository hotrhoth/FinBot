from pypdf import PdfReader
import os

def savetofile(text, filepath):
    with open(filepath, "a", encoding="utf-8") as f:
        f.write(text)

outputname1 = "FinML"
outputname2 = "Trading"

def parse_pdfFinML(filename):
    reader = PdfReader(filename)
    print(f'Number of pages FinML: {len(reader.pages)}')
    for i in range(len(reader.pages)):
        textname = os.path.join("data/extractedPageFinML",f"{outputname1}.txt")
        savetofile(reader.pages[i].extract_text(), textname)

def parse_pdfTrading(filename):
    reader = PdfReader(filename)
    print(f'Number of pages Trading: {len(reader.pages)}')
    for i in range(len(reader.pages)):
        textname = os.path.join("data/extractedPageTrading",f"{outputname2}.txt")
        savetofile(reader.pages[i].extract_text(), textname)

if __name__ == '__main__':
    parse_pdfFinML('data/book/[Book]-Andriy-Burkov-The-Hundred-Page-Machine-Learning-Book-Andriy-Burkov-2019.pdf')
    parse_pdfTrading('data/book/[Book]-DaveyBuilding_Winning_Algorithmic_Tradingrasabourse.com.pdf')
    
    
    
