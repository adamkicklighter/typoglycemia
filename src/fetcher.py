import requests

def fetch_article():
    """
    Fetches a random Wikipedia article using the Wikipedia API.

    Utilizes the `random` generator of the API to retrieve a random article from the
    main namespace and extracts its content in plain text format. If the fetch is
    successful, it returns the title and content of the article. If the fetch fails
    due to a network or API error, it returns None and prints an error message.

    Returns:
        dict or None: A dictionary containing the 'title' and 'content' of the article
                      if successful, None otherwise.
    """
    url = 'https://en.wikipedia.org/w/api.php'
    params = {
        'action': 'query',
        'format': 'json',
        'generator': 'random',
        'grnnamespace': 0,
        'prop': 'extracts',
        'explaintext': True,
        'exintro': False
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        page = next(iter(data['query']['pages'].values()))
        return {'title': page['title'], 'content': page['extract']}
    except requests.RequestException as e:
        print(f"Failed to fetch data: {e}")
        return None
