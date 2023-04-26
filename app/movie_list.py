"""Creates the data for movies"""
from typing import List
from dataclasses import dataclass

@dataclass
class Movie:
    """Creates a movie database"""
    name: str
    cast: List[str]
    year: int
    box_office: float

# Create an instance of the Movie class
movie = Movie(
    name='Sholay',
    cast=['Dharmendra', 'Amitabh Bachchan', 'Hema Malini', 'Jaya Bhaduri', \
        'Sanjeev Kumar','Amjad Khan'],
    year=1975,
    box_office=200000000.0
)

# Print the details of the movie
print(f"Movie Name: {movie.name}")
print(f"Cast: {', '.join(movie.cast)}")
print(f"Year of release: {movie.year}")
print(f"Box office collection: {movie.box_office}")
