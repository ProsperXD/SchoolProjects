import pickle


class Song:
    def __init__(self, title, year, rating):
        self.title = title
        self.year = year
        self.rating = rating

    def update_rating(self, new_rating):
        self.rating = new_rating

    def __str__(self):
        return f"{self.title} - {self.year} (Rating: {self.rating})"


def view_songs(songs):
    print("----- Your Playlist -----")
    if songs:
        for index, song in enumerate(songs):
            print(f"{index + 1}. {song}")
    else:
        print("Your playlist is empty.")
    print("------------------------")


def add_song(songs):
    title = input("Enter song title: ")
    year = input("Enter song year: ")
    rating = input("Enter song rating: ")
    song = Song(title, year, rating)
    songs.append(song)
    print("Song added successfully!")


def remove_song(songs):
    view_songs(songs)
    if songs:
        index = int(input("Enter the index of the song you want to remove: ")) - 1
        if 0 <= index < len(songs):
            del songs[index]
            print("Song removed successfully!")
        else:
            print("Invalid index!")
    else:
        print("No songs to remove!")


def update_rating(songs):
    view_songs(songs)
    if songs:
        index = int(input("Enter the index of the song you want to update rating for: ")) - 1
        if 0 <= index < len(songs):
            new_rating = input("Enter the new rating for the song: ")
            songs[index].update_rating(new_rating)
            print("Rating updated successfully!")
        else:
            print("Invalid index!")
    else:
        print("No songs to update rating!")


def save_playlist(songs):
    with open("../playlist.pkl", "wb") as file:
        pickle.dump(songs, file)
    print("Playlist saved successfully!")


def load_playlist():
    try:
        with open("../playlist.pkl", "rb") as file:
            songs = pickle.load(file)
        print("Playlist loaded successfully!")
        return songs
    except FileNotFoundError:
        print("No saved playlist found.")
        return []


def main():
    print("Welcome to the Music Application!")
    songs = load_playlist()

    while True:
        print("\nMenu:")
        print("1. View songs")
        print("2. Add song")
        print("3. Remove song")
        print("4. Update rating")
        print("5. Save playlist")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_songs(songs)
        elif choice == "2":
            add_song(songs)
        elif choice == "3":
            remove_song(songs)
        elif choice == "4":
            update_rating(songs)
        elif choice == "5":
            save_playlist(songs)
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
