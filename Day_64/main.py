import requests
import webbrowser

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJiN2YwZjY1MWY1ZTUyMmM3MzYyMDNlNjFhMmU3N2ZiZiIsIm5iZiI6MTczNjE4NDYzMy43MTQsInN1YiI6IjY3N2MxMzM5MTU1MjFmODNkOTY3MjNjYiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.tP-RQjsGKWti5w2O1PGh3NcMYiw-Fhu1tAYYZiV92pU "

}

param = {
    "query": input("Enter what you want to search for movies: ")
}

response = requests.get(
    url="https://api.themoviedb.org/3/search/multi", headers=headers, params=param)

data = response.json()

for i in range(len(data["results"])):
    pic = data["results"][i]["poster_path"]
    response = requests.get(f"https://image.tmdb.org/t/p/w500/{pic}")
    rating = data["results"][i]["vote_average"]
    description = data["results"][i]["overview"]
    if data["results"][i]["media_type"] == "movie":
        released = data["results"][i]["release_date"].split("-")[0]

    else:
        released = data["results"][i]["first_air_date"]
    print(released)
    print(round(rating, 1))
    print(description)

    # with open("Day_64/hello.png", "wb") as f:
    #     f.write(response.content)
    #     break
