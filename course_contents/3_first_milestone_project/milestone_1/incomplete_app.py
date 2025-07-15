# Incomplete app!

MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "
movies = []


def add_movie():
    title = input("Enter the movie title: ")
    director = input("Enter the movie director: ")
    year = input("Enter the movie release year: ")

    movies.append({
        'title': title,
        'director': director,
        'year': year
    })

def list_movies():
    for movie in movies:
        print_movie(movie)

def find_movie():
    title = input("Input movie title to find: ")
    for movie in movies:
        if movie['title'] == title:
            print_movie(movie)
            break
    else:
        print("Movie not found")

def print_movie(movie):
    print(f"Title: {movie['title']}")
    print(f"Director: {movie['director']}")
    print(f"Year: {movie['year']}")

ops = {
    'a': add_movie,
    'l': list_movies,
    'f': find_movie,
}

def menu():
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection in ops:
            ops[selection]()
        else:
            print('Unknown command. Please try again.')

        selection = input(MENU_PROMPT)

menu()
