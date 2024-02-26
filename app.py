import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
  response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=1a0c92656d95b4b00f89d342ce06a56c'.format(movie_id))
  data = response.json()
#   st.text(data)

  api_key = '1a0c92656d95b4b00f89d342ce06a56c'


  # Construct the API URL
  api_url = 'https://api.themoviedb.org/3/movie/{}?api_key={}'.format(movie_id, api_key)

  # Display the API URL
#   st.text(api_url)

#    st.text(https://api.themoviedb.org/3/movie/{}?api_key=1a0c92656d95b4b00f89d342ce06a56c'.format(movie_id))
  return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
  movie_index = movies[movies['title'] == movie].index[0]
  distances = similarity[movie_index]

  movies_list = sorted(list(enumerate(distances)), reverse = True, key = lambda x:x[1])[1:6]
  
  recommend_movies = []
  recommend_movies_posters = []
  for i in movies_list:
    movie_id = movies.iloc[i[0]].movie_id
    
    recommend_movies.append(movies.iloc[i[0]].title)
    # #fetch poster from api
    recommend_movies_posters.append(fetch_poster(movie_id))
  
  return recommend_movies, recommend_movies_posters

movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'Select Movie',
    movies['title'].values
)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)
    
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
       st.header(names[0])
       st.image(posters[0])
    with col2:
       st.header(names[1])
       st.image(posters[1])
    with col3:
       st.header(names[2])
       st.image(posters[2])
    with col4:
       st.header(names[3])
       st.image(posters[3])
    with col5:
       st.header(names[4])
       st.image(posters[4])
    
# if st.button('Recommend'):
#     names, posters = recommend(selected_movie_name)
    
#     col1, col2, col3, col4, col5 = st.columns(5)

#     for i in range(5):
#         try:
#             with col1 if i == 0 else col2 if i == 1 else col3 if i == 2 else col4 if i == 3 else col5:
#                 st.header(names[i])
#                 image = fetch_image_from_url(posters[i])
#                 st.image(image, caption=names[i], use_column_width=True, format='JPEG')  # Specify the format
#         except Exception as e:
#             st.error(f"Error loading image {i + 1}: {e}")
