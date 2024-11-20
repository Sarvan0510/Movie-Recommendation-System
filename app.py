import pickle
import streamlit as st
import pandas as pd
def recommend(movie):
    m_index = movies[movies['title'] == movie].index[0]
    distances = similarity[m_index]
    movie_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    recommended_movie_names = []
    for i in movie_list:

        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names


st.header('Movie Recommender System')
movies_d = pickle.load(open('movie_list.pkl', 'rb'))
movies = pd.DataFrame(movies_d)
similarity = pickle.load(open('similarity.pkl','rb'))

#movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movies['title'].values)

if st.button('Show Recommendation'):
    recommends = recommend(selected_movie)
    for i in recommends:
        st.write(i)
