import tkinter as tk  # Import the Tkinter module and rename it as tk for easier reference
from tkinter import messagebox  # Import the messagebox module from Tkinter for displaying error messages
from spotipy.oauth2 import SpotifyOAuth  # Import the SpotifyOAuth class for authentication with the Spotify API
import spotipy  # Import the spotipy module for accessing the Spotify Web API
import matplotlib.pyplot as plt  # Import the pyplot module from matplotlib for creating visualizations
from collections import defaultdict  # Import the defaultdict class from collections for handling default values

# Spotify API credentials
client_id = 'e6ebbe4707f44c71b2c477012d8a0d5a'  # My Spotify API client ID
client_secret = '3700d932e7144e4e93678baf0afb30ed'  # My Spotify API client secret
redirect_uri = 'http://localhost:8888/callback'  # URI to redirect to after authentication
scope = 'user-top-read'  # Scope of permissions required for accessing user data

# Initialize Spotify client
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri=redirect_uri,
                                               scope=scope))


# Function to fetch and visualize top artists
def fetch_and_visualize_artists():
    try:
        # Fetch top tracks
        top_tracks = sp.current_user_top_tracks(limit=50, time_range='long_term')

        # Count appearances of each artist in top tracks
        artist_appearances = defaultdict(int)
        for track in top_tracks['items']:
            for artist in track['artists']:
                artist_appearances[artist['name']] += 1

        # Sort artists by number of appearances, descending
        sorted_artists = sorted(artist_appearances.items(), key=lambda x: x[1], reverse=True)

        # Select top 20 artists for plotting
        top_artist_names, artist_appearance_counts = zip(*sorted_artists[:20])

        # Create bar chart for top artists
        plt.figure(figsize=(10, 6))
        plt.barh(top_artist_names, artist_appearance_counts, color='skyblue')
        plt.xlabel('NUMBER OF APPEARANCES IN TOP TRACKS', fontweight='bold', fontsize=12)
        plt.ylabel('ARTISTS', fontweight='bold', fontsize=12)
        plt.title('FAVORITE ARTISTS PER LISTENING FREQUENCY', fontweight='bold', fontsize=14)
        plt.tight_layout()
        plt.show()
    except Exception as e:
        messagebox.showerror("Error", str(e))


# Function to fetch and visualize top genres
def fetch_and_visualize_genres():
    try:
        # Fetch top tracks
        top_tracks = sp.current_user_top_tracks(limit=50, time_range='long_term')

        # Count appearances of each artist's genre in top tracks
        genre_appearances = defaultdict(int)
        for track in top_tracks['items']:
            for artist in track['artists']:
                artist_info = sp.artist(artist['id'])
                for genre in artist_info['genres']:
                    genre_appearances[genre] += 1

        # Sort genres by number of appearances, descending
        sorted_genres = sorted(genre_appearances.items(), key=lambda x: x[1], reverse=True)

        # Select top 10 genres for plotting
        top_genre_names, genre_appearance_counts = zip(*sorted_genres[:10])

        # Create pie chart for top genres
        plt.figure(figsize=(8, 8))
        plt.pie(genre_appearance_counts, labels=top_genre_names, autopct='%1.1f%%', startangle=140)
        plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.title('TOP GENRES', fontweight='bold', fontsize=14)
        plt.show()
    except Exception as e:
        messagebox.showerror("Error", str(e))


# Create the GUI
root = tk.Tk()  # Create the main Tkinter window
root.title("Spotify Listening Patterns Visualization")  # Set the title of the main window

# Create button to show top artists
artist_button = tk.Button(root, text="Show Top Artists", command=fetch_and_visualize_artists)
artist_button.pack(pady=10)  # Place the artist button in the main window with some vertical padding

# Create button to show top genres
genre_button = tk.Button(root, text="Show Top Genres", command=fetch_and_visualize_genres)
genre_button.pack(pady=10)  # Place the genre button in the main window with some vertical padding

root.mainloop()  # Enter the Tkinter event loop, keeping the GUI responsive
