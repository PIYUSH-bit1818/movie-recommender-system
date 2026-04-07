# 🎬 Movie Recommender System
A content-based movie recommender system built using **Machine Learning** and deployed with **Streamlit**, providing personalized movie suggestions along with posters.

## 🚀 Live Demo
👉 https://piyush-iitg-movie-recommender.streamlit.app/

## 📌 Features
* 🔍 Select a movie and get similar recommendations
* 🎯 Content-based filtering using cosine similarity
* 🖼️ Displays movie posters using TMDB API
* ⚡ Fast and interactive Streamlit web app

## 🧠 How It Works
* Movie data is processed into tags (overview, genres, keywords, cast, crew)
* Text data is vectorized using **CountVectorizer** (Bags of words)
* Similarity is computed using **cosine similarity**
* Top 5 similar movies are recommended

## 🛠️ Tech Stack
* Python
* Pandas
* Scikit-learn
* Streamlit
* TMDB API

## 📂 Project Structure

```
movie-recommender-system/
│
├── app.py
├── movie_dict.pkl
├── requirements.txt
├── .gitignore
```

## ⚙️ Installation & Setup
### 1. Clone the repository

```
git clone https://github.com/piyush-bit1818/movie-recommender-system.git
cd movie-recommender-system
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Run the app

```
streamlit run app.py
```
## 🔐 API Key Setup

This project uses the TMDB API.
Create a `.streamlit/secrets.toml` file and add:

```
API_KEY = "your_tmdb_api_key"
```

## 📊 Dataset

Dataset used: TMDB 5000 Movies Dataset
https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata

## 🙌 Acknowledgements

* TMDB API
* Kaggle Dataset

## ⭐ If you like this project

Give it a star ⭐ on GitHub!
