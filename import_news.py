import os
import django

# Set the environment variable to specify the Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "moviereviews.settings")

# Initialize Django
django.setup()

# Now you can import your models and perform other Django-related operations
from news.models import News
import json

def import_data_from_json(json_file_path):
    with open(json_file_path, 'r') as file:
        data = json.load(file)
        
    for item in data:
        News.objects.create(
            headline=item['title'],
            description=item['description'],
            date=item['publishedAt'][0:10],
            url=item['url'],
            urlToImage=item['urlToImage'],
        )

if __name__ == '__main__':
    json_file_path = 'news.json'  # Adjust the path to your JSON file
    import_data_from_json(json_file_path)
