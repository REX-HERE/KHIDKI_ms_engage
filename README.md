# KHIDKI_ms_engage

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
* Kids Mode
* Play the movie 
* file import , export feature in the database (see admin page and go to movie or dropdown)
* fetching poster via api (tmdb's api) or you can add posters, video in the database itself
* Secure login, logout
