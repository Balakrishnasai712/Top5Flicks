import pickle
import streamlit as st
import requests
import pandas as pd

def fetch_poster(movie_id):
    response = requests.get("https://api.themoviedb.org/3/movie/{}?language=en-US&api_key=b69f3fc0a0d3d98546c0845ee4f3b26a".format(movie_id))
    data = response.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500" + poster_path
    return full_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances:
        # fetch the movie poster
        recommended_movie_names.append(movies.iloc[i[0]].title)
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        # st.write(movies.iloc[i[0]].title)
    return recommended_movie_names,recommended_movie_posters

# st.header('Top5Flicks)
# Title of the app
st.markdown(
    """
    <div style="background-color:#2F4F4F;padding:10px;border-radius:10px">
        <h1 style="color:white;text-align:center;">🎥 Top5Flicks</h1>
    </div>
    """,
    unsafe_allow_html=True
)

# Brief description with styled text
st.markdown(
    """
    <p style="text-align:center;font-size:18px;color:gray;">
        Welcome to <b>Top5Flicks</b>, your personalized movie recommender!  
        Select a movie from the dropdown below, and we'll recommend the 
        <span style="color:#FFA500;">best 5 movies</span> that match your choice.  
        <i>Explore new favorites and rediscover classics!</i>
    </p>
    """,
    unsafe_allow_html=True
)
movies = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies)
movies_list = pd.DataFrame(movies)
similarity = pickle.load(open('similarity.pkl','rb'))

# movie_list = movies['title'].values
selected_movie = st.selectbox("Type or select a movie from the dropdown",movies_list["title"].values)
# st.write("Selected Movie:", selected_movie)
if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])




