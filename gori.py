#!/usr/bin/env python
# -*- coding:UTF-8 -*-
import random

def gori():
    s=u""
    sep=False
    beg=True
    while len(s)<120:
        if beg:
            s+=u"ウ"
            s+=[u"ホ",u"ホッ"][random.randrange(2)]
            beg=False
        if sep:
            s+=u"、"
            sep=False
            beg=True
        else:
            if random.randrange(10)==0:
                sep=True
            else:
                s+=[u"ホ",u"ホッ"][random.randrange(2)]
                if random.randrange(5)==0:
                    beg=True
    return s.encode('utf-8')

if __name__=="__main__":
    print gori()
