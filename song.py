class SongNode:
    def __init__(self, title):
        self.title = title
        self.next = None


class MusicPlaylist:
    def __init__(self):
        self.head = None

    def create_playlist(self, song_list):
        """Create a new playlist from a list of song titles."""
        for title in song_list:
            self.insert_song(title)

    def insert_song(self, title):
        """Insert a song at the end of the playlist."""
        new_node = SongNode(title)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
        print(f"Song '{title}' added to the playlist.")

    def delete_song(self, title):
        """Delete a song from the playlist by title."""
        temp = self.head
        prev = None

        while temp:
            if temp.title == title:
                if prev:
                    prev.next = temp.next
                else:
                    self.head = temp.next
                print(f"Song '{title}' deleted from the playlist.")
                return
            prev = temp
            temp = temp.next
        print(f"Song '{title}' not found in the playlist.")

    def display_playlist(self):
        """Display all songs in the playlist."""
        if not self.head:
            print("Playlist is empty.")
            return
        print("Music Playlist:")
        temp = self.head
        while temp:
            print(f"*{temp.title}")
            temp = temp.next


def main():
    playlist = MusicPlaylist()

    while True:
        print("\n--- Music Playlist Menu ---")
        print("1. Create Playlist")
        print("2. Insert Song")
        print("3. Delete Song")
        print("4. Display Playlist")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            songs = input("Enter song titles separated by commas: ").split(",")
            songs = [song.strip() for song in songs]
            playlist.create_playlist(songs)
        elif choice == '2':
            title = input("Enter song title to insert: ").strip()
            playlist.insert_song(title)
        elif choice == '3':
            title = input("Enter song title to delete: ").strip()
            playlist.delete_song(title)
        elif choice == '4':
            playlist.display_playlist()
        elif choice == '5':
            print("Exiting Music Playlist. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
