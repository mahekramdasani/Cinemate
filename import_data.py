import os
import django

# Set the environment variable to specify the Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "moviereviews.settings")

# Initialize Django
django.setup()

# Now you can import your models and perform other Django-related operations
from movie.models import Movie
import json

def import_data_from_json(json_file_path):
    with open(json_file_path, 'r') as file:
        data = json.load(file)

    for item in data:
        Movie.objects.create(
            Title=item['Title'],
            Year=item['Year'],
            Released=item['Released'],
            Runtime=item['Runtime'],
            Genre=item['Genre'],
            Director=item['Director'],
            Writer=item['Writer'],
            Actors=item['Actors'],
            Plot=item['Plot'],
            Language=item['Language'],
            Country=item['Country'],
            Awards=item['Awards'],
            Poster=item['Poster'],
            imdbRating=item['imdbRating'],
            imdbVotes=item['imdbVotes'],
        )

if __name__ == '__main__':
    json_file_path = 'movies.json'  # Adjust the path to your JSON file
    import_data_from_json(json_file_path)
