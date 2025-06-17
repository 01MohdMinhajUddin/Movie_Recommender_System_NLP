# Movie Recommender System

Welcome to my content-based movie recommendation system! This project demonstrates how we can use natural language processing (NLP) and cosine similarity to suggest movies that are similar to the one a user selects. I built this project to strengthen my skills in feature engineering, text vectorization, and deploying models with Streamlit.

# Table of Contents

- [Project Overview]
- [How It Works]
- [Installation]
- [Usage]
- [Project Structure]
- [Credits]

---

# Project Overview

This application recommends similar movies based on content such as cast, crew, genres, keywords, and descriptions. When a user selects a movie, the app returns 5 similar movies with their posters using The Movie Database (TMDB) API.

This is an end-to-end project involving:
- Data Preprocessing
- Feature Extraction using NLP
- Vectorization using CountVectorizer
- Cosine Similarity Calculation
- Web App Deployment with Streamlit

---

# How It Works

- Combine metadata (genres, keywords, cast, crew, overview)
- Apply stemming and vectorization to create a 'tag'
- Use cosine similarity to find closest matches
- Display recommendations and posters using Streamlit UI and TMDB API

---

# Installation


# Create and activate a virtual environment 
python -m venv env
env\Scripts\activate  # On Windows

# Install dependencies
pip install -r requirements.txt

NOTE :- Due to GitHub file size limits, please download similarity.pkl from the above link and place it in the project directory.

https://drive.google.com/file/d/1p_OePFsgjfbqzakpDybnwIltKMwaTqr3/view?usp=drive_link
