import re
import emoji
from src.config import (
    URL_RE, SOCIAL_RE, REPEAT_PUNCT_RE, ELONGATED_RE, 
    TASHKEEL_RE, WHITESPACE_RE, WORD_REPETITION_RE, 
    EMOJI_RE, EMOJI_TO_ARABIC, ARABIC_STOP_WORDS
)

def normalize_arabic(text):
    """Normalize Arabic letters and remove Tashkeel for better text consistency."""
    if not isinstance(text, str):
        return ""
    text = re.sub(r"[إأآ]", "ا", text)
    text = re.sub(r"ى", "ي", text)
    text = re.sub(r"ة", "ه", text)
    text = TASHKEEL_RE.sub('', text)
    return text

def clean_non_arabic_but_keep_emojis(text):
    """Filter out non-Arabic text while keeping pure emoji or Arabic reviews."""
    if not isinstance(text, str):
        return ""
        
    text_without_emojis = EMOJI_RE.sub('', text)
    if re.search(r'[a-zA-Z]', text_without_emojis):
        return ""  
    has_arabic = bool(re.search('[\u0600-\u06FF]', text_without_emojis))
    has_only_emojis = (text_without_emojis.strip() == "" and bool(EMOJI_RE.search(text)))
    if has_arabic or has_only_emojis:
        return text  
    return ""

def clean_customer_review(text):
    """Full preprocessing pipeline: demojize emojis to Arabic terms, remove URLs/noise, normalize Arabic text, and drop stop words."""
    if not isinstance(text, str):
        return ""
    
    # 1. Convert emojis to English text codes (e.g., :red_heart:)
    text = emoji.demojize(text, language='en')
    
    # 2. Replace known emoji codes with Arabic descriptive words
    for eng_name, ar_name in EMOJI_TO_ARABIC.items():
        text = text.replace(f":{eng_name}:", f" {ar_name} ")
        
    # 3. Remove any remaining unmatched emoji tags or English symbols
    text = re.sub(r':[a-zA-Z_]+:', '', text)
    
    # 4. Convert text to lowercase
    text = text.lower()
    
    # 5. Remove URLs and social media handles
    text = URL_RE.sub('', text)
    text = SOCIAL_RE.sub('', text)
    
    # 6. Reduce elongated characters and repeated punctuations
    text = ELONGATED_RE.sub(r"\1\1", text)
    text = REPEAT_PUNCT_RE.sub(r"\1", text)
    
    # 7. Apply Arabic normalization
    text = normalize_arabic(text)
    
    # 8. Remove Arabic stop words and short meaningless tokens
    words = text.split()
    filtered_words = [w for w in words if w not in ARABIC_STOP_WORDS and len(w) > 1]
    text = " ".join(filtered_words)
    
    # 9. Remove consecutive redundant words
    text = WORD_REPETITION_RE.sub(r'\1', text)
    
    # 10. Clean up extra whitespaces
    text = WHITESPACE_RE.sub(' ', text).strip()
    
    return text