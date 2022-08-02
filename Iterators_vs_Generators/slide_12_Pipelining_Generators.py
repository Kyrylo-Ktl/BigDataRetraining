import requests  # pip install requests


def download_pages(urls: list):
    for url in urls:
        yield requests.get(url)


def get_jsons(urls: list):
    for response in download_pages(urls):
        yield response.json()


def get_pokemon_names(base_url: str, max_page: int):
    urls = [
        base_url.format(page=page)
        for page in range(1, max_page)
    ]
    for json_data in get_jsons(urls):
        yield json_data['name']


URL = 'https://pokeapi.co/api/v2/pokemon/{page}'
for name in get_pokemon_names(URL, max_page=10):
    print(name)
