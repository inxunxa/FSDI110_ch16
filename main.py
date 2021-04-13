# imports
from display import print_menu, print_header, clear
from album import Album

# globals
# declare a catalog variable (list)

# functions

def register_album():
    print_header("Register new Album")

    title = input("Please provide Title: ")
    genre = input("Please provide Genre: ")
    artist = input("Please provide Artist Name: ")
    release_year = int(input("Please provide Release Year: "))
    price = float(input("Please provide Price: $"))
    album_art = input("Please provide Album Art URL: ")
    related_artist = input("Please provide Related Artist: ")
    record_label = input("Please provide Record Label: ")

    album = Album(title, genre, artist, release_year, price, album_art, related_artist, record_label)
    print(album)

    # push the album into the list
    
    input("Press Enter to continue...")


# instructions

opc = ''
while(opc != 'q' and opc != 'x'):
    clear()
    print_menu()
    opc = input("Please select an option: ")

    if(opc == '1'):
        register_album()
