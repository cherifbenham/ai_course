import requests

def fetch_lyrics(artist,title):
    url = f"https://lyrics.lewagon.ai/search?artist={artist}&title={title}"
    response = requests.get(url=url)
    status = response.status_code
    
    if status == 200:
        return response.json()['lyrics']
    else:
        return ''