# KHIDKI_ms_engage 

A hybrid (Google's Bert + Contant based via bag of words, and then KNN (K-Nearest Neighbor) using cosine similarity) movie recommendation web application
using DJANGO for backend, UI is inspired by NETFLIX.

**Deployed at** => http://35.202.149.148:8000

**IMPORTANT**
Due to being big git lfs is used to add file in Github repo but lfs creates some error in pickle file so kindly replace files of datasets with files in: https://drive.google.com/drive/folders/1g1ZUfKdcMLLiEZY3Eley7jp-cqxxJH8M?usp=sharing

**Requirements**- python version >= 3.9, sklearn. 

## Installation in windows-

Download this repository and cd in the folder

Create a virtual environment

```bash
python -m venv .\venv
venv\scripts\activate
```
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install dependencies of this project

```bash
pip install -r requirements.txt
```
## Usage

To run the website on the local host
```bash
python manage.py runserver
```
Now open your web browser and paste the url appears in the terminal

## Features-
* Multiple profile support
* Kids Mode (not many movies in the dataset for them :( )
* Play the movie (not showing original movie :) )
* file import , export feature in the database (see admin page and go to movie or dropdown)
* fetching poster via api (tmdb's api) or you can add posters, video in the database itself
* supports both single movie and movie with multiple episodes (*search: four rooms* that too have 1 episode only, not many in dataset are seasonal :( ) 
* Secure login, logout

## Algorithms used and comparison-
**Google's BERT** - 
                  a neural network-based technique for natural language processing (NLP) pre-training called Bidirectional Encoder Representations from Transformers, or as we call it- [BERT](https://ai.googleblog.com/2018/11/open-sourcing-bert-state-of-art-pre.html), for short. 
This breakthrough was the result of Google research on [transformers](https://ai.googleblog.com/2017/08/transformer-novel-neural-network.html): **models that process words in relation to all the other words in a sentence**, rather than one-by-one in order. BERT models can therefore consider the full context of a word by *looking at the words that come before and after it*—particularly useful for understanding the intent behind search queries, here for understanding movie’s overview and description.
                  
                 
