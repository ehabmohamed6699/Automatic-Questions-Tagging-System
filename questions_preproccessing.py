from ast import Lambda
from html.parser import HTMLParser
from pickle import TRUE
from tkinter.messagebox import QUESTION
from winreg import QueryInfoKey
import pandas as pd
import html_parser as htmlParser
import re as re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk import pos_tag
import nltk


data = pd.read_csv('Answers.csv',  chunksize=1000)

data = data.get_chunk(100)

listOfQuestions = []


for index, row in data.iterrows():
    question = row['Body']*1
    listOfQuestions.append(question)

listOfParsedQuestions = []

parser = htmlParser.Parser()

for question in listOfQuestions:
    parser.feed(question)
    listOfParsedQuestions.append(htmlParser.text_data) 

print("data:", listOfParsedQuestions)
#-------------------------------------------------------------------------------------
#----------------importing data and dropping closed date--------
QuestionData=pd.read_csv('Questions.csv',chunksize=1000)
QuestionData = QuestionData.get_chunk(1000)
QuestionData.drop('ClosedDate',inplace=True,axis=1)
pd.options.display.max_colwidth = 10000
print("data:",QuestionData['Body'].loc[[0]],None)
#----------------------Removing HTML tags (Regex)------------------
def remove_tags(string):
    result = re.sub('<.*?>','',string)
    return result
QuestionData['Body']=QuestionData['Body'].apply(lambda cw : remove_tags(cw))
print("data:",QuestionData['Body'].loc[[0]],None)
#-----------Removing stop words------------------
stopWords = set(stopwords.words("english"))
QuestionData['Body'] = QuestionData['Body'] . apply(lambda x:' '.join([word for word in x.split() if word not in (stopWords)]))
print(QuestionData.head())
#--------------------Tokenizing----------------------
QuestionData['Body'] =  QuestionData['Body'].apply(lambda x:word_tokenize(x))
#--------------------POS Tagging----------------------
Tags=  QuestionData['Body'].apply(lambda x:pos_tag(x))
QuestionData['POSTags'] =  Tags
print(QuestionData.head())
def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN
#-------------------- Lemmatizing----------------------
lemmatizer = WordNetLemmatizer()
QuestionData['Body'] = QuestionData['Body'].apply(lambda x:[lemmatizer.lemmatize(y) for y in x ])
print(QuestionData.head())

#------------------------------------------------------------------------------------

