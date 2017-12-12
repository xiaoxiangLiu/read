# coding=utf-8
import struct



with open('E:/workspace/ali_3.py', 'rb') as f:
    r = f.read()
    st = str(r)
file = open('pytext.text', 'w')
file.write(st)
file.close()


