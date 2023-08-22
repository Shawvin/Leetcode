## 168. Excel Sheet Column Title

## Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.
import string

def convertToTitle(columnNumber):
    title=''
    while(columnNumber>0):
        remainder=(columnNumber-1)%26
        columnNumber=(columnNumber-1)//26
        title+=string.ascii_uppercase[remainder]
    return title[::-1]

if __name__=='__main__':
    columnNumber=701
    print(convertToTitle(columnNumber))