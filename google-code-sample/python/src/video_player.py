"""A video player class."""
import random

from .video_playlist import Playlist
from .video_library import VideoLibrary



class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self._current_video = None  # A variable to hold current playing video
        self._pause_state = 0  # A state value 0 or 1 to indicate if a video is paused
        self._playlist = {}

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        print("Here's a list of all available videos:")
        videos = self._video_library.get_all_videos()
        videos.sort(key=lambda x: x.title)

        for items in videos:
            tags_string = ' '.join(items.tags)
            print(f"{items.title} ({items.video_id}) [{tags_string}]")

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        videos = self._video_library.get_all_videos()
        video = self._video_library.get_video(video_id)

        if video in videos:
            if self._current_video is None:
                print(f"Playing video: {video.title}")
                self._current_video = video
            else:
                print(f"Stopping video: {self._current_video.title}")
                print(f"Playing video: {video.title}")
                self._current_video = video
                self._pause_state = 0
        else:
            print("Cannot play video: Video does not exist")

    def stop_video(self):
        """Stops the current video."""
        """Stops the current video."""
        playing = self._current_video
        if not playing:
            print("Cannot stop video: No video is currently playing")
        else:
            print(f"Stopping video: {playing.title}")
            self._current_video = None
            self._pause_state = 0

    def play_random_video(self):
        """Plays a random video from the video library."""
        playing = self._current_video
        videos = self._video_library.get_all_videos()
        random_choice = random.choice(videos)

        if not playing:
            print(f"Playing video: {random_choice.title}")
            self._current_video = random_choice
        else:
            print(f"Stopping video: {playing.title}")
            print(f"Playing video: {random_choice.title}")
            self._current_video = random_choice

    def pause_video(self):
        """Pauses the current video."""
        playing = self._current_video

        if not playing:
            print(f"Cannot pause video: No video is currently playing")
        else:
            if self._pause_state == 0:
                print(f"Pausing video: {playing.title}")
                self._pause_state = 1
            else:
                print(f"Video already paused: {playing.title}")

    def continue_video(self):
        """Resumes playing the current video."""
        playing = self._current_video
        pause_state = self._pause_state

        if not playing:
            print(f"Cannot continue video: No video is currently playing")
        else:
            if pause_state == 1:
                print(f"Continuing video: {playing.title}")
                self._pause_state = 0
            else:
                print("Cannot continue video: Video is not paused")

    def show_playing(self):
        """Displays video currently playing."""

        playing = self._current_video
        video_id = ""

        pause_state = self._pause_state

        if not playing:
            print("No video is currently playing")
        else:
            video_id = playing.video_id
            video = self._video_library.get_video(video_id)
            if pause_state == 0:
                tags_string = ' '.join(video.tags)
                print(f"Currently playing: {video.title} ({video.video_id}) [{tags_string}]")
            else:
                tags_string = ' '.join(video.tags)
                print(f"Currently playing: {video.title} ({video.video_id}) [{tags_string}] - PAUSED")


    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        playlistName = playlist_name.lower()
        playlists = self._playlist
        is_present = playlistName in (item.lower() for item in playlists)

        if is_present:
            print("Cannot create playlist: A playlist with the same name already exists")
        else:
            playlists[playlist_name] = []
            print(f"Successfully created new playlist: {playlist_name}")

        self._playlist = playlists

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        playlistName = playlist_name.lower()
        video = self._video_library.get_video(video_id)
        videos = self._video_library.get_all_videos()
        playlists = self._playlist
        is_present = playlistName in (item.lower() for item in playlists)
        if is_present:
            for item in playlists:
                if item.lower() == playlistName:
                    selected = item
            if video in videos:
                if video not in playlists[selected]:
                    playlists[selected].append(video)
                    print(f"Added video to {playlist_name}: {video.title}")
                else:
                    print(f"Cannot add video to {playlist_name}: Video already added")
            else:
                print(f"Cannot add video to {playlist_name}: Video does not exist")
        else:
            print(f"Cannot add video to {playlist_name}: Playlist does not exist")


    def show_all_playlists(self):
        """Display all playlists."""

        playlists = self._playlist
        sorted_playlist = sorted(playlists.items(), key=lambda item: item[0])
        if playlists:
            print("Showing all playlists:")
            for key, value in sorted_playlist:
                print(key)
        else:
            print("No playlists exist yet")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        playlists = self._playlist
        playlistName = playlist_name.lower()
        videos_list = []
        is_present = playlistName in (item.lower() for item in playlists)
        selected = ""
        if is_present:
            for item in playlists:
                if item.lower() == playlistName:
                    selected = item

            if playlists[selected]:
                videos_list = playlists[selected]
                print(f"Showing playlist: {playlist_name}")
                for i in videos_list:
                    tags_string = ' '.join(i.tags)
                    print(f"{i.title} ({i.video_id}) [{tags_string}]")
            else:
                print(f"Showing playlist: {playlist_name}")
                print("No videos here yet")

        else:
            print(f"Cannot show playlist {playlist_name}: Playlist does not exist")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        playlistName = playlist_name.lower()
        video = self._video_library.get_video(video_id)
        videos = self._video_library.get_all_videos()
        playlists = self._playlist
        selected = ""
        is_present = playlistName in (item.lower() for item in playlists)
        if is_present:
            for item in playlists:
                if item.lower() == playlistName:
                    selected = item
            if video in videos:
                if video in playlists[selected]:
                    playlists[selected].remove(video)
                    print(f"Removed video from {playlist_name}: {video.title}")
                else:
                    print(f"Cannot remove video from {playlist_name}: Video is not in playlist")
            else:
                print(f"Cannot remove video from {playlist_name}: Video does not exist")
        else:
            print(f"Cannot remove video from {playlist_name}: Playlist does not exist")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        playlistName = playlist_name.lower()
        playlists = self._playlist
        selected = ""
        is_present = playlistName in (item.lower() for item in playlists)
        if is_present:
            for item in playlists:
                if item.lower() == playlistName:
                    selected = item
            if playlists[selected]:
                playlists[selected].clear()
                print(f"Successfully removed all videos from {playlist_name}")
            else:
                return
        else:
            print(f"Cannot clear playlist {playlist_name}: Playlist does not exist")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        playlistName = playlist_name.lower()
        playlists = self._playlist
        selected = ""
        is_present = playlistName in (item.lower() for item in playlists)
        if is_present:
            for item in playlists:
                if item.lower() == playlistName:
                    selected = item
            del playlists[selected]
            print(f"Deleted playlist: {playlist_name}")
        else:
            print(f"Cannot delete playlist {playlist_name}: Playlist does not exist")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        searchTerm = search_term.lower()
        videos = self._video_library.get_all_videos()
        searched_videos = []
        listed = []
        count = 1
        selected = 0
        for item in videos:
            if searchTerm in item.title.lower():
                searched_videos.append(item)
                # count += 1
            else:
                continue

        if searched_videos:
            print(f"Here are the results for {search_term}")
            for item in searched_videos:
                tags_string = ' '.join(item.tags)
                listed.append(f"{count}) {item.title} ({item.video_id}) [{tags_string}]")
                count += 1
            for i in listed: print(i)
            selected = input("Would you like to play any of the above? If yes, specify the number of the video." \
                             " If your answer is not a valid number, we will assume it's a no. \n")
            for item in listed:
                if selected == int(item[0]):
                    print(f"Playing video: {searched_videos[selected - 1]}")
        else:
            print(f"No search results for {search_term}")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
