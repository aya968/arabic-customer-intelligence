import os
import re

# 1. Project directories configuration
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODELS_DIR = os.path.join(BASE_DIR, 'models')

# 2. Model and Pickle paths
LOGISTIC_MODEL_PATH = os.path.join(MODELS_DIR, 'logistic_model.pkl')
TFIDF_VECTORIZER_PATH = os.path.join(MODELS_DIR, 'tfidf_vectorizer.pkl')
COMPANIES_TOPICS_PATH = os.path.join(MODELS_DIR, 'companies_topics.pkl')

# 3. Global Regex Patterns for text cleaning and noise reduction
URL_RE             = re.compile(r'http\S+|www\S+|https\S+', flags=re.MULTILINE)
SOCIAL_RE          = re.compile(r'@\w+|#\w+')
REPEAT_PUNCT_RE    = re.compile(r"([!?. ,;:]){2,}")
ELONGATED_RE       = re.compile(r"(.)(?:\s*\1){2,}")
TASHKEEL_RE        = re.compile(r'[\u0617-\u061A\u064B-\u0652]')
WHITESPACE_RE      = re.compile(r'\s+')
WORD_REPETITION_RE = re.compile(r'\b(\w+)(?:\s+\1\b)+', re.IGNORECASE)

# Regex to detect standard emojis across different unicode ranges
EMOJI_RE = re.compile(
    "["
    "\U0001F600-\U0001F64F"  
    "\U0001F300-\U0001F5FF"  
    "\U0001F680-\U0001F6FF"  
    "\U0001F1E0-\U0001F1FF"  
    "\u2702-\u27B0"
    "\u24C2-\u24FF"
    "]+", flags=re.UNICODE
)

# 4. Dictionary mapping English emoji codes to meaningful Arabic words for Topic Modeling
EMOJI_TO_ARABIC = {
    "red_heart": "حب",
    "smiling_face_with_heart_eyes": "اعجاب",
    "thumbs_up": "ممتاز",
    "thumbs_down": "سيء",
    "fire": "رائع",
    "clapping_hands": "ممتاز",
    "crying_face": "زعلان",
    "angry_face": "غاضب",
    "enraged_face": "غاضب جداً",
    "face_with_tears_of_joy": "ضحك",
    "smiling_face": "سعيد",
    "broken_heart": "سيء",
    "cloud": "سحاب"
}

ARABIC_STOP_WORDS = {
    "في", "من", "على", "عن", "إلى", "البدء", "مع", "هذا", "هذه", "ذلك", 
    "التي", "الذي", "لان", "أن", "إن", "هو", "هي", "كان", "كانت", "ولا", 
    "وما", "به", "بها", "ففي", "وما", "منه", "لها", "فيه", "ال"
}
