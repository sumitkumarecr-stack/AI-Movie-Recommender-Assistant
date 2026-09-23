# AI Based Movie Recommender System

A movie recommendation web app built with Python and Streamlit. It suggests similar movies based on content similarity and also includes an AI movie assistant powered by Google Gemini.

## Features

- Movie recommendation engine using TF-IDF + cosine similarity
- Search and recommendation based on a selected movie
- Movie cards with poster, overview, budget, revenue, cast, and director details
- AI-powered chat assistant for movie-related questions
- Responsive Streamlit interface

## Project Structure

- [app.py](app.py): Streamlit app UI and logic
- [model.py](model.py): preprocessing, similarity calculation, and recommendation logic
- [tmdb_5000_movies.csv](tmdb_5000_movies.csv): movie metadata
- [tmdb_5000_credits.csv](tmdb_5000_credits.csv): cast and crew data

## Local Setup

1. Clone the repository:

```bash
git clone <your-repo-url>
cd AI_Based_MOVIE_RS
```

2. Create and activate a virtual environment:

```bash
python -m venv .venv
```

On Windows:

```powershell
.\.venv\Scripts\Activate.ps1
```

On macOS/Linux:

```bash
source .venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Set environment variables for the AI assistant and TMDB poster API:

```powershell
$env:GOOGLE_API_KEY="your_google_api_key"
$env:GEMINI_API_KEY="your_google_api_key"
$env:TMDB_API_KEY="your_tmdb_api_key"
```

Or create a `.env` file if you prefer, and use `python-dotenv` in future versions.

5. Run the app:

```bash
streamlit run app.py
```

## Deployment on Streamlit Community Cloud

1. Push the project to GitHub.
2. Go to: https://streamlit.io/cloud
3. Sign in with GitHub.
4. Click "New app".
5. Choose your GitHub repository.
6. Set:
   - Branch: `main` or `master`
   - File path: `app.py`
7. Add environment variables in Streamlit Cloud:
   - `GOOGLE_API_KEY`
   - `GEMINI_API_KEY` (optional if using the first one)
   - `TMDB_API_KEY` (optional for poster fetching)
8. Deploy.

After deployment, Streamlit gives you a public URL like:

```text
https://<your-app-name>.streamlit.app
```

## GitHub Upload Steps

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin <your-github-repo-url>
git push -u origin main
```

## Notes

- The AI chatbot works only when a valid Google Gemini API key is set.
- Posters are loaded from TMDB when a `TMDB_API_KEY` is configured; otherwise a placeholder image is shown.
- If the app is slow on first load, it is due to data preprocessing and similarity computation.

## License

This project is for educational/demo purposes.
