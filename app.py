import pickle
import pandas as pd
import streamlit as st
import random
import requests
import time

# Load data
df = pickle.load(open('movie_dict.pkl', 'rb'))
df = pd.DataFrame(df)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Fetch poster with error handling and rate limiting
def fetch_poster(movie_id, max_retries=3):

    api_key = '999e55444a851f26147d1748d91f21f6'
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36'
    }

    for attempt in range(max_retries):
        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            data = response.json()
            poster_path = data.get('poster_path')

            if poster_path:
                return f"https://image.tmdb.org/t/p/w500{poster_path}"
            else:
                return "https://via.placeholder.com/500x750?text=No+Image"
        
        except Exception as e:
            print(f"[Attempt {attempt + 1}] Failed for movie_id {movie_id}: {e}")
            time.sleep(0.3 * (2 ** attempt) + random.uniform(0, 0.2))

    return "https://via.placeholder.com/500x750?text=Error"


# Recommendation logic
def recommend(movie):
    recommended_movies = []
    movie_index = int(df[df['title'] == movie].index[0])
    distance = similarity[movie_index]
    movie_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]
    
    for i in movie_list:
        recommended_movies.append(df.iloc[i[0]].title)
    return recommended_movies

# Streamlit UI
st.title(":blue[Movie Recommendation System]")
selected_movie = st.selectbox("Choose a Movie : ", list(df['title'].values))

btn = st.button("Recommend")

if btn:
    movies_list = recommend(selected_movie)

    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.text(movies_list[i])
            movie_id = df[df['title'] == movies_list[i]].id.values[0]
            time.sleep(random.uniform(0.2, 0.5))  # delay to avoid TMDB rate limit
            poster = fetch_poster(movie_id)
            st.image(poster, width=200)
