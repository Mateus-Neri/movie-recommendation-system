import pandas as pd

#Função que retorna os filmes que contem o que está sendo pesquisado
def search_movie(movie: str, movies_info):
    filmes = movies_info[movies_info['title'].str.contains(movie, case=False, na=False)].head(10)
    return filmes[['id', 'title', 'realese_year', 'poster_path']].to_dict(orient="records")