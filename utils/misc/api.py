def find_lyric(singer,song):
    url = "https://api.lyrics.ovh/v1/"+str(singer)+str(song)
    import requests
    import json
    rest = requests.get(url)
    if rest.status_code == 200:
        response = json.loads(rest.text)
        print(response)
    else:
        print(rest.status_code)