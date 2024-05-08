# SpotifyAnalytics

## Description
This Python script fetches data from the Spotify API related to the user's top tracks, analyzes the data to identify top artists and genres, and visualizes the results using matplotlib. It allows users to explore their listening patterns and preferences through interactive charts.

## Features
- Fetches user's top tracks from Spotify API.
- Analyzes the data to determine top artists and genres based on listening frequency.
- Visualizes the top artists using a horizontal bar chart and the top genres using a pie chart.
- Provides an interactive GUI built with Tkinter for user interaction.

## Usage
1. Ensure you have Python installed along with the required libraries: tkinter, spotipy, matplotlib, collections.
2. Obtain Spotify API credentials (client ID and client secret) from the Spotify Developer Dashboard.
3. Set up a redirect URI for authentication purposes.
4. Replace the `client_id`, `client_secret`, and `redirect_uri` variables with your Spotify API credentials.
5. Run the Python script (`spotify_visualization.py`).
6. Click the "Show Top Artists" button to visualize top artists based on listening frequency.
7. Click the "Show Top Genres" button to visualize top genres based on listening frequency.

## Files
- `spotify_visualization.py`: The main Python script for fetching data, analysis, visualization, and GUI interaction.
- `README.md`: This file providing information about the script and usage instructions.

## Dependencies
- `tkinter`: Python's standard GUI toolkit for creating graphical user interfaces.
- `spotipy`: A lightweight Python library for accessing the Spotify Web API.
- `matplotlib`: A Python plotting library for creating visualizations such as charts and graphs.
- `collections`: A Python module providing specialized container datatypes.

## Notes
- Ensure you have a Spotify account and are logged in to use this script.
- The script requires user authentication with the Spotify API, which is handled through the OAuth2 authentication flow.
- Make sure to handle any errors or exceptions gracefully to provide a smooth user experience.


