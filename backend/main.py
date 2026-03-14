from fastapi import FastAPI
from backend.load_data import load_artifacts
from backend.download_data import get_data
from backend.recommender import recommendation, get_movies
from contextlib import asynccontextmanager
from backend.search import search_movie

app = FastAPI()




global cosine_sim, ids_tmdb, indices, movies_info
#Carrega os artefatos


cosine_sim, ids_tmdb, indices, movies_info = load_artifacts()


#Recomenda os filmes baseado no id do filme
@app.get("/recommend/{movie_id}")
async def recommend_movie(movie_id: int):
  tmdb_ids = recommendation(id = movie_id, 
                            cosine_sim= cosine_sim,
                            ids_tmdb= ids_tmdb,
                            indices= indices)

  movies = await get_movies(tmdb_ids)

  return movies

#Retorna os filmes com o título parecido durante a pesquisa
@app.get("/search")
def search(movie: str):
  return search_movie(movie, movies_info)