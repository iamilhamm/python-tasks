playlist = {}

print("Welcome to the playlist")

print("Let's add some songs to your playlist")
while True:
    try:
        title = input("Enter the song title: ").strip()
        if not title:
            raise ValueError("Song title cannot be blank")

        artist = input("Enter the artist's name: ").strip()
        if not artist:
            raise ValueError("Artist name cannot be blank")

        genre = input("Enter the genre of the song: ").strip()
        if not genre:
            raise ValueError("Genre cannot be empty.")

        playlist[title] = {"artist": artist, "genre": genre}
        print(f"Added '{title}' by {artist} to your playlist successfully.\n")

    except ValueError as e:
        print(f"Error: {e}")

    
    print("Here is your playlist:")
    for title, details in playlist.items():
        print(f"Title: {title}, Artist: {details['artist']}, Genre: {details['genre']}")


try:
    title_to_update = input("Enter the title of the song you want to update: ").strip()
    if title_to_update in playlist:
        new_artist = input("Enter the new artist's name (leave blank to keep current): ").strip()
        new_genre = input("Enter the new genre (leave blank to keep current): ").strip()

        if new_artist:
            playlist[title_to_update]["artist"] = new_artist
        if new_genre:
            playlist[title_to_update]["genre"] = new_genre

        print(f"Updated details for '{title_to_update}'.\n")
    else:
        raise KeyError(f"'{title_to_update}' is not in the playlist.")
except KeyError as e:
    print(f"Error: {e}")


try:
    title_to_delete = input("Enter the title of the song you want to delete: ").strip()
    if title_to_delete in playlist:
        del playlist[title_to_delete]
        print(f"Deleted '{title_to_delete}' from the playlist.\n")
    else:
        raise KeyError(f"'{title_to_delete}' is not in the playlist.")
except KeyError as e:
    print(f"Error: {e}")


print("Here is your final playlist:")
if not playlist:
    print("Your playlist is empty.")
else:
    for title, details in playlist.items():
        print(f"Title: {title}, Artist: {details['artist']}, Genre: {details['genre']}")

print("\nThank you for using the Simple Music Playlist!")
