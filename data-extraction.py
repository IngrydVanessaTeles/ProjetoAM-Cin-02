# -*- coding: utf-8 -*-
from Util import readBase
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.naive_bayes import MultinomialNB,BernoulliNB
from sklearn.linear_model import LogisticRegression,SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC
import nltk
import random
import nltk.corpus
import sklearn
import numpy
import csv
from sklearn import metrics
import sys
from nltk.stem.snowball import SnowballStemmer

nomeBase = "data/train.csv"
base = readBase(nomeBase)

tamBase = len(base)
print("Tamanho da base: "+str(tamBase))

#tokenização
i=0
documents = []
while (i<tamBase):
    conteudoLista = (base[i][0].split(),base[i][1])
    documents.append(conteudoLista)
    i += 1

#Misturando a base
random.shuffle(documents)

#inicializando stemmer
stemmer = SnowballStemmer("english", ignore_stopwords=True) #se não ignorar os stopwords, não vai remover eles depois

#Construindo bag of words
all_words = []
k=0
l=len(documents)
while (k<l):
    m=len(documents[k][0])
    n=0
    while(n<m):
        #stemmer
        documents[k][0][n] = stemmer.stem(documents[k][0][n])
        all_words.append(documents[k][0][n])
        n+=1
    k += 1

#inicializando bag de stopwords
stopwords = nltk.corpus.stopwords.words('english')

print("Palavras total da base (com repetições): "+str(len(all_words)))
#remove Itens repetidos - verifica palavras unicas
all_words_unique = sorted(set(all_words))
print("Palavras únicas: "+str(len(all_words_unique)))

#stopWords e Suavização
#all_words = nltk.LidstoneProbDist(nltk.FreqDist(w.lower() for w in all_words if w not in stopwords), 0.1)
#word_features = list(all_words.samples())

#apenas stopwords
all_words = nltk.FreqDist(nltk.FreqDist(w.lower() for w in all_words if w not in stopwords))
word_features = list(all_words.keys())

#apenas suavização
#all_words = nltk.LidstoneProbDist(nltk.FreqDist(all_words), 0.1)
#word_features = list(all_words.samples())

print("Palavras restantes após pre-processamento: "+str(len(word_features)))

