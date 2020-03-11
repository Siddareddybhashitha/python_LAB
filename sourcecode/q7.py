#Read data from file
fh = open('input.txt')
text = fh.read()
fh.close()

import nltk
nltk.download('punkt')
nltk.download('wordnet')
#Tokenization
words = nltk.word_tokenize(text)
sentences = nltk.sent_tokenize(text)
#Apply lemmatization
from nltk.stem import WordNetLemmatizer
lm = WordNetLemmatizer()
lem_lst = []
for i in words:
    lem_lst.append(lm.lemmatize(i))
print('Tokenization and applied lemmatization')
print(lem_lst)
print()

#Remove all punctuations in word token
new_words = []
for i in words:
    if i not in ',.?=;:!()':
        new_words.append(i)
#Find trigrams
from nltk.util import ngrams
trigrams = list(ngrams(new_words, 3))
print('Trigrams')
print(trigrams)
print()
#Get the frequency of trigrams
import collections
freq = collections.Counter(trigrams)
print('Top 10 most frequent trigrams')
#Top 10 most frequency trigrams
most_freq = freq.most_common(10)
print(most_freq)
print()

#Find sentences contain most frequence trigrams
lst = []
for i in most_freq:
    #Join the trigrams tokens
    str = ' '.join(i[0])
    lst.append(str)
trigrams_sentences = ''
for i in sentences:
    for j in lst:
        if j in i:
            #Get the sentence contain the trigrams
            trigrams_sentences += i
            break
print('Sentences contain most frequency trigrams')
print(trigrams_sentences)
