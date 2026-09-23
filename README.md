# AI Movie Recommender & Assistant

An AI-powered movie recommendation application built with Python and Streamlit. The app recommends movies similar to a selected title and provides an AI assistant for movie-related questions.

## Live Demo

[Open the live Streamlit app](https://ai-movie-recommender-assistant-fpzombf4aeo97fknc8hvqd.streamlit.app/)

## Features

- Select a movie and get five similar recommendations
- Content-based recommendations using TF-IDF and cosine similarity
- Movie details including rating, director, cast, overview, budget, and revenue
- TMDB poster images with a fallback placeholder
- Gemini-powered movie chatbot for recommendations, actors, plots, and movie questions
- Streamlit interface with separate recommendation and chatbot sections

## How It Works

The application combines movie metadata, genres, keywords, cast, and overview text into searchable tags. TF-IDF converts these tags into numerical vectors, and cosine similarity identifies movies with the most similar content.

The chatbot uses the Google Gemini API to answer movie-related questions using the conversation history.

## Tech Stack

- Python
- Streamlit
- Pandas and NumPy
- Scikit-learn
- Google Gemini API
- TMDB API

## Project Files

- [app.py](app.py): Streamlit interface, movie details, posters, and AI chatbot
- [model.py](model.py): Data preprocessing, TF-IDF vectorization, similarity calculation, and recommendations
- [tmdb_5000_movies.csv](tmdb_5000_movies.csv): Movie metadata
- [tmdb_5000_credits.csv](tmdb_5000_credits.csv): Cast and crew data
- [requirements.txt](requirements.txt): Python dependencies

## Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

The chatbot requires a Gemini API key. TMDB poster images require a TMDB API key. Configure both keys through environment variables or Streamlit Secrets.

```toml
GEMINI_API_KEY = "your_gemini_api_key"
TMDB_API_KEY = "your_tmdb_api_key"
```

## Data Source

The recommendation dataset contains movie information, credits, genres, keywords, cast, crew, ratings, budget, and revenue data from the TMDB 5000 Movies dataset.
