import re

def stringMatcher():
    patron = re.compile('a*b')
    while True:
        s = input('Ingrese string:')
        if patron.fullmatch(s):
            print('si hace match')
        else:
            print('no hace match')


def stringMatcher2():
    #inicio ^ de un string
    #final $ de un string
    patron = re.compile('^\d+$')
    while True:
        s = input('Ingrese string:')
        if patron.fullmatch(s):
            print('si hace match')
        else:
            print('no hace match')

def stringSeacrh():
    patron = re.compile('[A-D]+')
    while True:
        s = input('Ingrese string:')
        if patron.search(s):
            print('si hace match')
        else:
            print('no hace match')

stringSeacrh()