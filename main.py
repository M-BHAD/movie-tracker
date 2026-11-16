to_watch=[]
watched=[]
def show_menu():

    print("==================MOVIE WATCHLIST====================")
    print("1.Add a movie")
    print("2. View movies")
    print("3.Mark as watched")
    print("4.Remove a movie")
    print("5.Exit")
    choice=int(input("Enter your choice(1-5): "))
    return choice 


def add_movie():
    movie_name=input("enter a movie name: ").strip()
    to_watch.append(movie_name)
    print("Movie added successfully!")

def view_movies():

    if not to_watch:
       print("No movies to watch")
    else:
       for index, movie in enumerate( to_watch, start=1):
           print(index,movie)

def mark_as_watched():

    if not to_watch:
       print("No movies available")
       return 
    for movie in to_watch:
        print(movie)
    movie_watched=input("enter movie you watched: ").strip()
    

    if movie_watched in to_watch:
        to_watch.remove(movie_watched)
        watched.append(movie_watched)
        print("movie marked as watched ")
    else:
        print("Movie not found!")

def remove_movie():
    movie = input("Enter movie name: ")

    if movie in to_watch:
        to_watch.remove(movie)
    elif movie in watched:
        watched.remove(movie)
    else:
        print("Movie not found!")

while True:
    choice = show_menu()

    if choice == 1:
        add_movie()

    elif choice == 2:
        view_movies()

    elif choice == 3:
        mark_as_watched()

    elif choice == 4:
        remove_movie()

    elif choice == 5:
        print("Thank you for using Movie Watchlist!")
        break

    else:
        print("Invalid choice! Please enter 1-5.")
    
