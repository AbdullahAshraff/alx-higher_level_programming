#!/usr/bin/python3
def uppercase(str: str):
    newone = ''
    for letter in str:
        newone += chr(ord(letter)-32) if 97 <= ord(letter) <= 122 else letter
    return newone
