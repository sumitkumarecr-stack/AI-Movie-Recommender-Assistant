import ast
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

BASE_DIR = Path(__file__).resolve().parent
MOVIES_PATH = BASE_DIR / "tmdb_5000_movies.csv"
CREDITS_PATH = BASE_DIR / "tmdb_5000_credits.csv"


def load_and_preprocess():
    if not MOVIES_PATH.exists() or not CREDITS_PATH.exists():
        raise FileNotFoundError(
            f"Movie data files not found. Expected: {MOVIES_PATH} and {CREDITS_PATH}"
        )

    movies = pd.read_csv(MOVIES_PATH)
    credits = pd.read_csv(CREDITS_PATH)

    movies = movies.merge(credits, on='title')

    data = movies[['movie_id', 'title', 'overview', 'genres', 'keywords', 'cast', 'crew', 'budget', 'revenue', 'vote_average']].copy()
    data.dropna(subset=['overview'], inplace=True)

    def convert(obj):
        try:
            return [i['name'] for i in ast.literal_eval(obj)]
        except (ValueError, TypeError, SyntaxError):
            return []

    def get_director(obj):
        try:
            for i in ast.literal_eval(obj):
                if i.get('job') == 'Director':
                    return i.get('name', 'Unknown')
        except (ValueError, TypeError, SyntaxError):
            return 'Unknown'
        return 'Unknown'

    def convert_cast(obj):
        try:
            cast = ast.literal_eval(obj)
            return [i['name'] for i in cast[:3]]
        except (ValueError, TypeError, SyntaxError):
            return []

    data['director'] = data['crew'].apply(get_director)
    data['genres_list'] = data['genres'].apply(convert)
    data['keywords_list'] = data['keywords'].apply(convert)
    data['cast_list'] = data['cast'].apply(convert_cast)

    data['overview_list'] = data['overview'].apply(lambda x: str(x).split())
    data['tags'] = data['overview_list'] + data['genres_list'] + data['keywords_list'] + data['cast_list']
    data['tags'] = data['tags'].apply(lambda x: ' '.join(x).lower())

    return data


def compute_similarity(df):
    tfidf = TfidfVectorizer(max_features=5000, stop_words='english')
    vectors = tfidf.fit_transform(df['tags']).toarray()
    similarity = cosine_similarity(vectors)
    return similarity


def recommend(movie_title, df, similarity):
    if movie_title not in df['title'].values:
        return []

    index = df[df['title'] == movie_title].index[0]
    distances = similarity[index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommendations = []
    for i in movies_list:
        movie_data = df.iloc[i[0]]
        recommendations.append({
            'movie_id': movie_data['movie_id'],
            'title': movie_data['title'],
            'cast': ', '.join(movie_data['cast_list']),
            'director': movie_data['director'],
            'budget': movie_data['budget'],
            'revenue': movie_data['revenue'],
            'rating': movie_data['vote_average'],
            'overview': movie_data['overview']
        })
    return recommendations