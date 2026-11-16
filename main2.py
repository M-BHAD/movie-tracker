to_watch=[]
watched=[]
def show_menu():
    print("\n"+ "="*30)
    print("MOVIE WATCHLIST")
    print("\n"+ "="*30)
    print("1. Add a movie ")
    print("2. View movies")
    print("3. Mark as watched")
    print("4. Remove a movie")
    print("5. Exit")
    print("-"*30)

    choice=int(input("Enter your choice (1-5): "))
    return choice

def add_movie():
    movie_name=input("Enter a movie name: ")
    to_watch.append(movie_name)
    print("Movie added succesfully!")
def view_movies():
    print("\n========== YOUR MOVIES ==========")

    print("\nTO WATCH:")

    if not to_watch:
        print("No movies in your watchlist.")
    else:
        for index, movie in enumerate(to_watch, start=1):
            print(f"{index}. {movie}")

    print("\nWATCHED:")

    if not watched:
        print("No watched movies yet.")
    else:
        for index, movie in enumerate(watched, start=1):
            print(f"{index}. {movie}")
def mark_as_watched():
    # movie=input("Which movie did you watch?: ")
    # if movie in to_watch:
    #    to_watch.remove(movie)
    #    watched.append(movie)
    # else:
    #     print("Movie not found!")
   
    if not to_watch:
        print("\nYour watchlist is empty!")
        return

    print("\nMovies to watch:")

    for movie in to_watch:
        print("-", movie)

    movie = input("\nWhich movie did you watch? ").strip()

    if movie in to_watch:
        to_watch.remove(movie)
        watched.append(movie)
        print(f"\n'{movie}' marked as watched successfully!")
    else:
        print("\nMovie not found! Check the spelling.")

def remove_movie():
    name_of_movie=input("enter movie to remove: ")

    if name_of_movie in to_watch:
        to_watch.remove(name_of_movie)
        print("Movie removed!")
    else:
        print("Movie not found!")


while True:
    choice=show_menu()

    if choice==1:
        add_movie()
    elif choice==2:
        view_movies()
    elif choice==3:
            mark_as_watched()
    elif choice==4:
           remove_movie()
    elif choice==5:
        print("Thanks for using Movie watchlist!")
        break
    else:
        print("Invalid choice! Try again!!")

