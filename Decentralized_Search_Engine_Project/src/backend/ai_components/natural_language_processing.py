# NLP implementation

import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk import pos_tag

class NaturalLanguageProcessing:
    def __init__(self):
        # Initialize NLTK resources
        nltk.download('punkt')
        nltk.download('stopwords')
        nltk.download('wordnet')
        nltk.download('averaged_perceptron_tagger')
        self.stop_words = set(stopwords.words('english'))
        self.stemmer = PorterStemmer()
        self.lemmatizer = WordNetLemmatizer()

    def tokenize(self, text):
        """
        Tokenize the input text into words.
        """
        tokens = word_tokenize(text)
        return tokens

    def sentence_tokenize(self, text):
        """
        Tokenize the input text into sentences.
        """
        sentences = sent_tokenize(text)
        return sentences

    def remove_stopwords(self, tokens):
        """
        Remove stopwords from the list of tokens.
        """
        filtered_tokens = [token for token in tokens if token.lower() not in self.stop_words]
        return filtered_tokens

    def stem(self, tokens):
        """
        Perform stemming on the tokens.
        """
        stemmed_tokens = [self.stemmer.stem(token) for token in tokens]
        return stemmed_tokens

    def lemmatize(self, tokens):
        """
        Perform lemmatization on the tokens.
        """
        lemmatized_tokens = [self.lemmatizer.lemmatize(token) for token in tokens]
        return lemmatized_tokens

    def pos_tagging(self, tokens):
        """
        Perform Part-of-Speech (POS) tagging on the tokens.
        """
        tagged_tokens = pos_tag(tokens)
        return tagged_tokens

