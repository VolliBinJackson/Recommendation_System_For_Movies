import streamlit as st
from hybrid_model import recommend_hybrid_model

st.title("Movie-Recommendation System")

user_id_input = st.number_input("User-ID", min_value=1, max_value=1000)
movie_id_input = st.number_input("Movie-ID", min_value=1, max_value=10000)

if user_id_input and movie_id_input:
    recommendations = recommend_hybrid_model(user_id_input, movie_id_input)
    st.write("Recommended movies:", recommendations)