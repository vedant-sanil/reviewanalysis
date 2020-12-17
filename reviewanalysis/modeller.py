import re
import nltk 
import plotly
import spacy
import plotly.graph_objects as go
from goose3 import Goose 
import pandas as pd 
from nltk.tokenize import sent_tokenize
from sklearn.manifold import TSNE
from sklearn.cluster import KMeans 
from spacy.lang.en.stop_words import STOP_WORDS
from sentence_transformers import SentenceTransformer

class TopicModeller():
    def __init__(self, sentence_df, min_char_len=50):
        sents = ''
        nlp = spacy.load('en_core_web_sm')
        embedder = SentenceTransformer('bert-base-nli-stsb-mean-tokens')
        
        for idx, sent in enumerate(sentence_df['sentence']):
            sent = sent.strip()
            if sent[-1] != '.':
                sent+='.'
            sents += sent
            sents += ' '

        dfs = sent_tokenize(sents)
        df1 = dfs
        df_len = ', '.join(df1)
        df_len = len(df_len)
        dfs=[re.sub(r'[[^()]*]', '', i) for i in dfs]
        dfs=[re.sub('^n', '', i) for i in dfs]
        dfs=[re.sub('^n', '', i) for i in dfs]
        dfs=[re.sub('• ', '', i) for i in dfs]
        dfs=[ i for i in df1 if len(i) >= min_char_len ]

        self.corpus_embeddings = embedder.encode(dfs)