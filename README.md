# Книжный онлайн-магазин

[Презентация](https://docs.google.com/presentation/d/1CAkLSnS6ZJqOW6UFBXdKXF1jAFh4Hi8Rj4zAuh3BW9M/edit?usp=sharing)

## Description
This is the repository containing the API of an online bookstore. The project as a whole consists of a website, a mobile app, and this API. The user should be able to "buy" a book, search for a book using various criteria, save the book for later, preorder, subscribe to publisher news, register.

## Installation
### Simple local installation
Just clone this repo and run in its root directory:
```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```
That would run this API locally. You can access it via http://localhost:5000/api. See wiki for the list of currently implemented requests.
### Docker
Just use these two commands:
```
docker build -t cicd-buzz .
docker run -p 5000:5000 --rm -it cicd-buzz
```

## Usage
If you run this API locally, find it at http://localhost:5000/api. Otherwise, it's at https://enigmatic-fjord-21043.herokuapp.com/api. See wiki for the list of currently implemented requests.

## Contributing
Olga Emelyanova - API  
Elizaveta Pavliv - mobile app  
Elizaveta Rudko - website  

## Links
[Доска задач](https://trello.com/b/N4SVkmsi/online-book-store)  

### Лабораторная работа №6
[Отчет](https://docs.google.com/document/d/1SxKUJQ3qKWR2iIdwp54GnfThFLRbq41w9RUsQqbt9YE/edit?usp=sharing)

### Лабораторная работа №5
[Отчет](https://docs.google.com/document/d/13xRC4Q1mV95B9rvDL7SD5nQtfdJC0OVN1I8Swgg0RR8/edit?usp=sharing)

### Лабораторная работа №4
[Отчет](https://docs.google.com/document/d/1XCsQlN3ctddITmQk-4DqYc0eJI72WeYPPpzDh3rKV5w/edit?usp=sharing)

### Лабораторная работа №3
[Отчет](https://docs.google.com/document/d/1yqkAIHTJadKMPsDAT156mki4fX61RuriYXG0IMjlrF4/edit?usp=sharing)

### Лабораторная работа №2
[Отчет](https://docs.google.com/document/d/1GajB9ztzVj_wTfkXFviRRLMyeE8dEW_rIhYh-ez5ZEw/edit?usp=sharing)

### Лабораторная работа №1
[Отчет](https://docs.google.com/document/d/1CJvNVqk_2MeYn7cg6lBN1w57VVnbmdHvJZgvyGb2Fx8/edit?usp=sharing)
