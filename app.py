import streamlit as st
import pickle
import pandas as pd
import requests

with open("MovieRecommendProjectDict.pkl", "rb") as f:
    movie_dict = pickle.load(f)

movies=pd.DataFrame(movie_dict)

with open ("similarity.pkl","rb") as g:
    similarity=pickle.load(g)

#Creating a function to show the Top 5 recommended movies
def recommend(movie):
    movie_index = movies[movies["title"] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_name=[]
    recommended_poster=[]
    for i in movies_list:
        movie_id = movies["movie_id"].iloc[i[0]]

        recommended_name.append(movies["title"].iloc[i[0]])
        recommended_poster.append(fetch_poster(movie_id))
    return recommended_name,recommended_poster


api_key = "8265bd1679663a7ea12ac168da84d2e8"
def fetch_poster(movie_id):
    url=f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}"

    response=requests.get(url)
    data=response.json()
    return f"https://image.tmdb.org/t/p/w500"+data["poster_path"]


st.title("Movie Recommender System")

selected_movie_name=st.selectbox(
    "Select Movies",
    movies["title"].values
)


if st.button("Recommend"):
    recommended_name,recommended_poster = recommend(selected_movie_name)

    col1,col2,col3,col4,col5 = st.columns(5)

    with col1:
        st.text(recommended_name[0])
        st.image(recommended_poster[0])
    with col2:
        st.text(recommended_name[1])
        st.image(recommended_poster[1])
    with col3:
        st.text(recommended_name[2])
        st.image(recommended_poster[2])
    with col4:
        st.text(recommended_name[3])
        st.image(recommended_poster[3])
    with col5:
        st.text(recommended_name[4])
        st.image(recommended_poster[4])