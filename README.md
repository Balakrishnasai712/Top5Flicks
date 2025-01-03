# 🎥 Top5Flicks - Movie Recommendation System

Top5Flicks is a movie recommendation system that suggests the **top 5 movies** similar to a selected movie. Built using **Python**, **Streamlit**, and **The Movie Database (TMDb) API**, this project combines machine learning and an interactive UI to help users explore new and exciting films.

## 🔧 Features
- Provides personalized movie recommendations.
- Displays movie posters along with recommendations.
- User-friendly interface powered by **Streamlit**.
- Utilizes **cosine similarity** to calculate the most relevant movies.

## 🚀 How It Works
1. Select a movie from the dropdown menu.
2. Get recommendations for the **top 5 similar movies**.
3. View movie posters fetched dynamically from **TMDb API**.

## 🛠️ Technologies Used
- **Python**: Backend logic and data processing.
- **Streamlit**: Interactive and visually appealing UI.
- **Pickle**: For storing precomputed data.
- **TMDb API**: To fetch movie details and posters.
- **Pandas**: Data manipulation.

## 📂 Project Structure
- `app.py`: Main Streamlit application file.
- `movie_dict.pkl`: Serialized dictionary of movie titles and IDs.
- `similarity.pkl`: Precomputed similarity matrix for recommendations.

## 🌐 Demo
Run the application locally or deploy it using Streamlit Cloud. Once deployed, select a movie to see your recommendations instantly.

## 📝 How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/Top5Flicks.git
