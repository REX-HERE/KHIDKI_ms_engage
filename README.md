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
                  
**KNN (K-Nearest Neighbor) using cosine similarity** - In physics we represent a point in an N-dimensional space using a vector. For example a seat at a Football stadium could be described by the distance relative from the center point of the stadium floor. If we add the time dimension, we would have a 4th dimension to represent the occupancy of that seat perhaps for different football games in a particular season. Similarly we can model our Set Similarity problem in an N dimensional space where each dimension represent an attribute in our dataset. Since N could be really large, we typically say this model is a High Dimensional Vector Space. Every single observation can be represented as a point (and therefore, a vector) in this space.
If we want to compare how similar two items are, we represent each object or entity as a vector in N dimensional space first, then we calculate the Cosine value of the angle between those two vectors. Fortunately, this cosine value can be easily computed as the dot product of the two vectors divided by the product of their magnitudes.

**Advantage of using cosine similarity**- I am fitting a k-nearest neighbors classifier using scikit learn and noticed that the fitting is faster, often by an order of magnitude or more, when using the cosine similarity between two vectors compared to when using the Euclidean similarity.  cosine similarity is fast, simple, and gets slightly better accuracy than other distance metrics.

**BOW (Bag of words)** - The bag-of-words model is a simplifying representation used in natural language processing. In this model, a text (such as a sentence or a document) is represented as the multiset of its words, disregarding grammar (that’s why I cleaned the data in pre-processing) and even word order but keeping frequencies of the words. well defined fixed-length inputs and by using the Bag-of-Words technique we can convert variable-length texts into a fixed-length vector.
                 
(Some other Algorithms i have implemented to compare performance of my hybrid, you can find that in colab notebook)-

**Collaborative filtering using Matrix factorisation with SVD and with gradient descent**
Singular Value Decomposition (SVD)-

SVD decomposes any matrix into singular vectors and singular values. Simply put, SVD is equivalent to Principal Component Analysis (PCA) after mean centering, i.e. shifting all data points so that their mean is on the origin.
Formally, SVD is decomposition of a matrix R into the product of three matrices: Rm∗n=Um∗mDm∗nVtn∗nRm∗n=Um∗mDm∗nVn∗nt.
Where Rm∗nRm∗n denotes the utility matrix with n equal to the number of e.g. users and m number exposed items (movies). Um∗mUm∗m is a left singular orthogonal matrix, representing the relationship between users and latent factors. Dm∗nDm∗n is a diagonal matrix (with positive real values) describing the strength of each latent factor. Vtn∗nVn∗nt (transpose) is a right singular orthogonal matrix, indicating the similarity between items and latent factors.
The general goal of SVD (and other matrix factorization methods) is to decompose the matrix R with all missing rijrij and multiply its components Um∗mDm∗nVtn∗nUm∗mDm∗nVn∗nt once again. As a result, there are no missing values rijrij and it is possible to recommend each user movies (items) they have not seen or purchased yet with the help of these predicted ratings.

