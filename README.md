# 🎬 Movie Recommendation System - Backend

API de recomendação de filmes baseada em **Content-Based Filtering**.

O sistema utiliza informações dos filmes (como título, gêneros e sinopse) para calcular similaridade entre eles e sugerir filmes parecidos a partir de um título informado.

A aplicação é construída com **FastAPI**, permitindo acesso às recomendações através de uma API.

---

## 🚀 Tecnologias utilizadas

- **Python**
- **FastAPI**
- **Pandas**
- **NumPy**
- **Scikit-learn**
- **TF-IDF**
- **Cosine Similarity**

Arquivos utilizados pelo sistema de recomendação:

- `cosine_sim.npy` → matriz de similaridade entre filmes  
- `ids_tmdb.pkl` → IDs dos filmes utilizados  
- `indices.pkl` → índice para busca rápida  
- `movies_info.parquet` → informações dos filmes

## 📋 Pré-requisitos

Antes de começar, você precisará ter instalado em sua máquina:
* [Python](https://www.python.org/downloads/) (versão 3.8 ou superior recomendada)
* [Git](https://git-scm.com/)

---

## 🔧 Instalação e Execução

Siga os passos abaixo para configurar o ambiente localmente:

### 1. Clonar o Repositório
Abra o seu terminal e execute:
```bash
git clone [https://github.com/Mateus-Neri/movie-recommendation-system.git](https://github.com/Mateus-Neri/movie-recommendation-system.git)
cd movie-recommendation-system
```
### 2. Criar um Ambiente Virtual (Recomendado)
Isso mantém as dependências do projeto isoladas.
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux/MacOS
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar Dependências
Com o ambiente virtual ativado, instale as bibliotecas necessárias:
```bash
pip install -r requirements.txt
```

### 4. Executar a Aplicação
```bash
python -m uvicorn backend.main:app --reload
```
A aplicação ficará disponível em:
```bash
http://127.0.0.1:8000
```
