from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
import csv

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """Load songs from a CSV file for the CLI recommender."""
    songs = []
    with open(csv_path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Convert string fields to appropriate types
            row['id'] = int(row['id'])
            row['energy'] = float(row['energy'])
            row['tempo_bpm'] = float(row['tempo_bpm'])
            row['valence'] = float(row['valence'])
            row['danceability'] = float(row['danceability'])
            row['acousticness'] = float(row['acousticness'])
            songs.append(row)
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Score a song against user preferences and return score plus reasons."""
    score = 0.0
    reasons: List[str] = []

    # Agent experiment: reduce genre weight and double energy importance.
    # This tests whether songs with the right energy are ranked higher even if genre is a weaker signal.
    if song.get("genre") == user_prefs.get("favorite_genre"):
        score += 1.0
        reasons.append("Genre matches user favorite")

    if song.get("mood") == user_prefs.get("favorite_mood"):
        score += 1.5
        reasons.append("Mood matches user preference")

    energy_difference = abs(song.get("energy", 0.0) - user_prefs.get("target_energy", 0.0))
    energy_score = max(0.0, 1.0 - energy_difference)
    energy_bonus = energy_score * 2.0
    score += energy_bonus
    reasons.append(f"Energy is close to target (+{energy_bonus:.2f})")

    acoustic_match = song.get("acousticness", 0.0) > 0.5
    if acoustic_match == bool(user_prefs.get("likes_acoustic", False)):
        score += 1.0
        reasons.append("Acoustic preference matches")

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Score all songs and return the top k recommendations."""
    scored_songs = [
        (song, score, "; ".join(reasons))
        for song in songs
        for score, reasons in [score_song(user_prefs, song)]
    ]

    scored_songs.sort(key=lambda item: item[1], reverse=True)
    return scored_songs[:k]
