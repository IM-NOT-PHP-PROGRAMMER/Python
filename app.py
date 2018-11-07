#!/usr/bin/python
import time

if __name__ == '__main__':
    while True:
        try:
            file = open('notemptyfile.txt')
            print(file.read())
            file.close()
        except Exception:
            print('smth gone wrong')
        time.sleep(5)
