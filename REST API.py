import requests


def bestInGenre(genre):
    base_url = "https://jsonmock.hackerrank.com/api/tvseries" # url were taking data from
    page = 1 # initial page
    best_show = None # empty best show var
    best_rating = float('-inf') # neg inf so any show will have a better rating

    while True: # while loop to sift through pages
        response = requests.get(f"{base_url}?page={page}") # get page
        data = response.json() # parse in json

        for show in data['data']: # iterate through shows in the array called data
            if genre.lower() in show['genre'].lower(): # if there is a genre section, all lower for ease
                rating = show['imdb_rating'] # store rating
                name = show['name'] # store name

                if rating > best_rating or (rating == best_rating and name < best_show): # if rating is best OR if rating is equal , get alphabetical order
                    best_rating = rating # store as best rating
                    best_show = name # store name

        if page >= data['total_pages']: # if page is greater than max pages, this is on the json doc
            break

        page +=1 # iterate to next page
    return best_show

print(bestInGenre("Action"))