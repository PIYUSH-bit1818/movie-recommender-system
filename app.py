import streamlit as st
import pickle
import pandas as pd
import requests
import time
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Movie Recommender", layout="wide")

# ---------------- DARK UI ----------------
st.markdown("""
<style>
.stApp {
    background-color: #0E1117;
    color: white;
}
h1, h2, h3 {
    color: white;
}
label {
    color: white !important;
}
.stSelectbox div[data-baseweb="select"] {
    color: black !important;
}
div[role="listbox"] {
    background-color: white !important;
    color: black !important;
}
div[role="option"] {
    color: black !important;
}
.stButton button {
    background-color: #1f77ff;
    color: white;
    border-radius: 8px;
    padding: 8px 16px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# ---------------- LOAD DATA ----------------
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

# ---------------- COMPUTE SIMILARITY (FIXED) ----------------
@st.cache_data
def compute_similarity(movies):
    cv = CountVectorizer(max_features=5000, stop_words='english')
    vectors = cv.fit_transform(movies['tags']).toarray()
    return cosine_similarity(vectors)

similarity = compute_similarity(movies)

# ---------------- FETCH POSTER (API FIXED) ----------------
@st.cache_data
def fetch_poster(movie_id):
    api_key = st.secrets["API_KEY"]

    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    for attempt in range(3):
        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            data = response.json()

            if data.get('poster_path'):
                return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
            else:
                return "https://via.placeholder.com/500x750?text=No+Image"

        except requests.exceptions.RequestException:
            time.sleep(1)

    return "https://via.placeholder.com/500x750?text=Error"

# ---------------- RECOMMEND FUNCTION ----------------
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movie = []
    recommended_movies_posters = []

    for i in movies_list:
        recommended_movie.append(movies.iloc[i[0]].title)
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies_posters.append(fetch_poster(movie_id))

    return recommended_movie, recommended_movies_posters

# ---------------- UI ----------------
st.markdown(
    "<h1>🎬 Movie Recommender System</h1>",
    unsafe_allow_html=True
)

selected_movie_name = st.selectbox(
    "Choose a movie",
    movies['title'].values
)

if st.button("Recommend"):
    names, posters = recommend(selected_movie_name)

    cols = st.columns(5)

    for i in range(5):
        with cols[i]:
            st.markdown(
                f"<h5 style='text-align:center;'>{names[i]}</h5>",
                unsafe_allow_html=True
            )
            st.image(posters[i])