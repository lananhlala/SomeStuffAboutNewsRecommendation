import string
import re
from pyvi import ViTokenizer

def remove_punctuation(text):
    text = text.lower()
    text = text.replace('\n', ' ')
    text = text.translate(str.maketrans(' ', ' ', string.punctuation))
    # scan deeper
    text = re.sub(r'[^\w\s]', ' ', text, re.UNICODE)
    # remove number
    text = re.sub('\d', ' ', text)
    return text

def tokenize_vietnamese(text):
    return ViTokenizer.tokenize(text)

def remove_stop_words(text): 
    # load list stopword
    stopwords = []
    with open(r'E:\NewsRSTopic\Data\PTIT\vietnamese-stopwords-dash.txt', 'r', encoding='utf-8') as f:
        all_ = f.read()
        for line in all_.splitlines():
            stopwords.append(line.rstrip())
    
    token_without_stopword = [word for word in text.split() if not word in stopwords and len(word)>2]
    return " ".join(token_without_stopword)

def preprocess_text(text):
    text = remove_punctuation(text)
    text = tokenize_vietnamese(text)
    text = remove_stop_words(text)
    return text

import pandas as pd
if __name__ == "__main__":
    data = pd.read_csv(r'E:\NewsRSTopic\Article-Classification\30k_article\30k_article.tsv', \
         header=None, names=['title','summarize','content','created','url','category','tag','source'], sep='\t')
    # data['content'] = data['content'].apply(lambda x: preprocess_text(str(x)))
    # data.to_csv('clean_data.csv')
    print(data.loc[6, 'content'])