from random import choice
import requests
import json

# Gets the API with user selected parameters, if valid, converts text from API to a python dictionary, data.
def getAPI(genre, score, start_date):

    apiURL = "https://api.jikan.moe/v4/anime"
    params = {'min_score': score, 'start_date': start_date, 'genre': genre}

    response = requests.get(apiURL, params)

    if response.status_code == 200:
        data = json.loads(response.text)
        return data

# Takes in genre as an input from user, returns an id that corresponds to the genre, 
# as genres are stored through numbers in the API.
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

# Creates a list to store anime names, retrieves a set of data from API, takes the title in english from 
# that set of data, stores into list, if unique. Returns list.
def animeSelector(data):

    list = []
    
    while len(list) < len(data):
        anime = choice(data['data'])
        anime_title = anime['title_english']
        
        if (not(anime_title in list)):
            list.append(anime_title)

    return list

# Asks user for 3 inputs, genre, score, premiere date. Uses those inputs as parameteres for the API, 
# then chooses a random anime from the list created.
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
