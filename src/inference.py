import pickle
from src.preprocessing import clean_customer_review
from src.config import LOGISTIC_MODEL_PATH, TFIDF_VECTORIZER_PATH

class SentimentPredictor:
    def __init__(self, model_path=LOGISTIC_MODEL_PATH, vectorizer_path=TFIDF_VECTORIZER_PATH):
        # Load trained models from configured paths
        with open(model_path, 'rb') as f:
            self.model = pickle.load(f)
            
        with open(vectorizer_path, 'rb') as f:
            self.vectorizer = pickle.load(f)
            
    def predict(self, raw_text):
        # 1. Clean the raw text
        cleaned = clean_customer_review(raw_text)
        
        # 2. Vectorize the cleaned text
        vectorized = self.vectorizer.transform([cleaned])
        
        # 3. Predict sentiment
        prediction = self.model.predict(vectorized)[0]
        return prediction, cleaned