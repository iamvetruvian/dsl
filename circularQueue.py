class Node:
    def __init__(self, song):
        self.song = song
        self.next = None
        self.prev = None

class MusicPlaylist:
    def __init__(self):
        self.front = None
        self.rear = None
        self.current = None

    def AddSong(self, song):
        new_node = Node(song)
        if self.front is None:
            self.front = self.rear = new_node
            new_node.next = new_node.prev = new_node
            self.current = new_node
        else:
            new_node.prev = self.rear
            new_node.next = self.front
            self.rear.next = new_node
            self.front.prev = new_node
            self.rear = new_node
        print(f"Added: {song}")

    def RemoveSong(self, song):
        if self.front is None:
            print("Playlist empty")
            return
        temp = self.front
        while True:
            if temp.song == song:
                # Only one song
                if self.front == self.rear:
                    self.front = self.rear = self.current = None
                else:
                    temp.prev.next = temp.next
                    temp.next.prev = temp.prev
                    if temp == self.front:
                        self.front = temp.next
                    if temp == self.rear:
                        self.rear = temp.prev
                    if temp == self.current:
                        self.current = temp.next  # move to next song
                print(f"Removed: {song}")
                return
            temp = temp.next
            if temp == self.front:
                print("Song not found")
                return

    def PlayNext(self):
        if self.current is None:
            print("Playlist empty")
            return
        self.current = self.current.next
        print(f"Now playing: {self.current.song}")

    def PlayPrevious(self):
        if self.current is None:
            print("Playlist empty")
            return
        self.current = self.current.prev
        print(f"Now playing: {self.current.song}")

    def ViewCurrentSong(self):
        if self.current is None:
            print("Playlist empty")
        else:
            print(f"Currently playing: {self.current.song}")

    def ShowAllSongs(self):
        if self.front is None:
            print("Playlist empty")
            return
        temp = self.front
        print("Playlist:", end=" ")
        while True:
            print(temp.song, end=" → ")
            temp = temp.next
            if temp == self.front:
                break
        print()

# Example usage
pl = MusicPlaylist()
pl.AddSong("Song A")
pl.AddSong("Song B")
pl.AddSong("Song C")
pl.ViewCurrentSong()
pl.PlayNext()
pl.PlayPrevious()
pl.RemoveSong("Song B")
pl.ShowAllSongs()
