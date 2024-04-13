import spacy

class SemanticUnderstanding:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")

    def analyze_text(self, text):
        """
        Analyze the input text to extract semantic information.
        """
        doc = self.nlp(text)
        return doc

    def extract_entities(self, doc):
        """
        Extract named entities from the analyzed text.
        """
        entities = [(ent.text, ent.label_) for ent in doc.ents]
        return entities

    def extract_keywords(self, doc):
        """
        Extract keywords or important terms from the analyzed text.
        """
        keywords = [token.text for token in doc if not token.is_stop and token.pos_ in ('NOUN', 'VERB', 'ADJ')]
        return keywords

    def analyze_sentiment(self, text):
        """
        Analyze the sentiment of the input text.
        """
        # Placeholder for sentiment analysis implementation
        return "Positive"  # Dummy result

    def classify_intent(self, text):
        """
        Classify the intent of the input text (e.g., question, request, statement).
        """
        # Placeholder for intent classification implementation
        return "Question"  # Dummy result
