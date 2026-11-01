import streamlit as st
import pandas as pd
import pickle
from src.inference import SentimentPredictor
from src.config import COMPANIES_TOPICS_PATH

def run_prediction_page():
    st.title("💬 Real-Time Customer Sentiment Analysis")
    st.write("Enter a customer review below to test the trained Logistic Regression model.")
    
    predictor = SentimentPredictor()
    user_review = st.text_area("Enter customer review here:", placeholder="Example: الخدمة كانت ممتازة جداً ❤️")
    
    if st.button("Analyze Review"):
        if user_review.strip() == "":
            st.warning("Please enter some text first!")
        else:
            prediction, cleaned_text = predictor.predict(user_review)
            st.markdown("---")
            st.subheader("Analysis Result:")
            if prediction == 1 or prediction == "positive":
                st.success("🎉 The review is **Positive** 😊")
            else:
                st.error("⚠️ The review is **Negative** 😞")
            st.write(f"**Processed Text:** `{cleaned_text}`")

def run_insights_page():
    st.title("📈 Company Analytics & BERTopic Insights")
    st.write("Explore semantic topics and key customer pain points extracted for each company.")
    
    try:
        # Using configured path
        with open(COMPANIES_TOPICS_PATH, 'rb') as f:
            all_companies_topics = pickle.load(f)
            
        companies_list = list(all_companies_topics.keys())
        
        if not companies_list:
            st.warning("No company topics found in the saved data.")
            return
            
        selected_company = st.selectbox("Select Company:", companies_list)
        topic_info = all_companies_topics[selected_company]
        
        st.info(f"📊 Topic Modeling Insights for: **{selected_company}**")
        st.subheader("💡 Key Extracted Topics Overview")
        
        valid_topics = topic_info[topic_info['Topic'] != -1]
        
        for index, row in valid_topics.iterrows():
            topic_id = row['Topic']
            raw_name = row['Name']
            count = row['Count']
            
            clean_name = " ".join([w for w in raw_name.split("_") if not w.isdigit() and len(w) > 2])
            
            with st.expander(f"📌 Topic {topic_id} | Reviews: {count} | Keywords: {clean_name[:40]}..."):
                st.write("**Top Words for this Topic:**")
                st.info(clean_name)
                st.progress(min(count / 150, 1.0), text=f"Topic Volume: {count} reviews")
                
        with st.expander("📊 View Full Detailed Table"):
            st.dataframe(topic_info, use_container_width=True)
            
    except FileNotFoundError:
        st.error(f"⚠️ File not found at: `{COMPANIES_TOPICS_PATH}`. Please run the notebook saving cell first.")