import streamlit as st
from startup_nlp_processing import process_idea
from startup_classifier import predict_sector, train_classifier
from startup_config import DATA_PATH, MODEL_PATH
import os

def main():
    st.title("Business Sector Classifier")
    st.write("Enter a business idea to predict its sector")
    st.write("أدخل فكرة عمل للتنبؤ بقطاعها \n")
    
    # Input form
    idea_text = st.text_area("Business Idea (فكرة عمل) ", placeholder="e.g., Online AI-tutoring platform")
    if st.button("Classify"):
        if idea_text:
            # Process input and predict sector
            keywords = process_idea(idea_text)
            sector = predict_sector(keywords)
            st.success(f"Predicted Sector: **{sector}**")
            st.write(f"Keywords extracted: {keywords}")
        else:
            st.error("Please enter a business idea.")

    # Train model if not exists
    if not os.path.exists(MODEL_PATH):
        st.info("Training classifier...")
        train_classifier()
        st.success("Classifier trained!")

if __name__ == "__main__":
    main()