from random import choice
import requests
import json


def getAPI(genre, score, start_date):

    apiURL = "https://api.jikan.moe/v4/anime"
    query_params = {'min_score': score, 'start_date': start_date, 'genre': genre}

    response = requests.get(apiURL, query_params)

    if response.status_code == 200:
        data = json.loads(response.text)
        return data

def genreToMALid(genre):

    genre = genre.lower()

    match genre:
        case "action":
            return 1
        case "adventure":
            return 2
        case "comedy":
            return 4
        case "drama":
            return 8
        case "fantasy":
            return 10
        case "horror":
            return 14
        case "romance":
            return 22
        case "sci-fi":
            return 24
        case "sports":
            return 30
        case "slice of life":
            return 36


def animeSelector(data):

    list = []
    synopsis_list = []

    while len(list) < len(data):
        anime = choice(data['data'])

        anime_title = anime['title_english']

        list.append(anime_title)

    return list

def main():

    genre = input("Please provide a valid genre: ")
    score = input("Please provide a minimum score: ")
    start_date = input("Please provide a starting date (YYYY-MM-DD): ")

    genre = genreToMALid(genre)

    list = animeSelector(getAPI(genre, score, start_date))

    randomAnime = choice(list)
    
    print("You should watch " + randomAnime + "!")    

if __name__ == "__main__":
    main()
