# -*- coding: utf-8 -*-
import csv
import re

def readBase(csvFile = str):
    base = []
    with open(csvFile) as csvfile:

        import codecs
        ifile = open(csvFile, "rb")
        read = csv.reader(codecs.iterdecode(ifile, 'utf-8'))

        for row in read:
            try:
                #se for pegar classe 0 ou 1
                if(float(row[1])>=0.5):
                    temp2 = 1
                else:
                    temp2 = 0

                #Se for pegar o valor float
                #temp2 = float(row[1])
                temp1 = row[2].lower()
                temp1 = re.sub('[^A-Za-z]+', ' ', temp1)

                base.append(tuple([temp1, temp2]))
            except IndexError:
                pass
        return base


def readBaseOnlyTexts(csvFile = str):
    base = []
    with open(csvFile) as csvfile:
        import codecs
        ifile = open(csvFile, "rb")
        read = csv.reader(codecs.iterdecode(ifile, 'utf-8'))

        for row in read:
            try:
                temp1 = row[2].lower()
                temp1 = re.sub('[^A-Za-z]+', ' ', temp1)
                base.append(temp1)
            except IndexError:
                pass
        return base