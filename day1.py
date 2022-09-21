"""
PYTHON PROGRAMMING DAY ONE TUTORIA
"""
print('Hello World')
#Variables
NUM =15
NUM2 =15.5
FIRSTNAME = 'Taiwo'
X = True
#Escape Character
WORD = 'we\'re brothers from the other side of the town'
print(WORD)
WORD2 = "we're brothers from the other side of the town"
print(WORD2)
# New Line
WORD3 = 'python is a programming language\npython is easy\nand python is fun'
print(WORD3)
print('\n')
#Multiline String
WORD4 = '''python is a programming language
python is easy
and python is fun
'''
print(WORD4)
#String Concentenation
print('hello' + ' '+'world')# joining of string and string
print('my name is'+' '+FIRSTNAME)#joining of string and variable also holding a string value
SURNAME  = 'Paul'
print(SURNAME + ' '+ FIRSTNAME)#joining of variable and variable also holding a string value
#string formatting
PRICE1 = 25000
PRICE2 = 15000
PRICE3 = 45000
REPORT = 'I sold a pair of shoe for {}, 3 shirts for {} and a suit for {}'
print(REPORT.format(PRICE1,PRICE2,PRICE3))
print(f'I sold a pair of shoe for {PRICE2}, 3 shirts for {PRICE1} and a suit for {PRICE3}')
#String Method
WORD5 = 'python'
WORD6 = 'PYTHON'
WORD7 = 'python is fun'
WORD8 = '  info'
print(WORD5.upper())
print(WORD6.lower())
print(WORD7.title())
print(WORD7.capitalize())
print(WORD7.split())
print(WORD8.strip())