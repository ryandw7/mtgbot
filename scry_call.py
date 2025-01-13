import requests

def scry_call(query_arr):
    data_arr = []
    for i in query_arr:
        response = requests.get(f"https://api.scryfall.com/cards/search?q={i}")
        if response.status_code == 200:
            data = response.json()
            if 'data' in data and len(data['data']) > 0:
                card_data = data['data'][0]  # Get the first card in the results
                if 'image_uris' in card_data and 'normal' in card_data['image_uris']:
                    img = card_data['image_uris']['normal']
                    data_arr.append(img)
    return data_arr