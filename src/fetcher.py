import requests

def get_random_wikipedia_article():
    """
    Fetches a random Wikipedia article using the Wikipedia API.

    Uses the `random` generator of the API to obtain a random article from the
    main namespace and extracts its content in plain text format. If the fetch
    is successful, it returns the title and content of the article. If the fetch
    fails due to a network or API error, it returns None and prints an error message.

    Returns:
        dict or None: A dictionary containing the 'title' and 'content' of the article
                      if successful, None otherwise.
    """
    # Endpoint for Wikipedia's random article API
    url = 'https://en.wikipedia.org/w/api.php'

    # Parameters for fetching a random article in plain text
    params = {
        'action': 'query',
        'format': 'json',
        'generator': 'random',
        'grnnamespace': 0,  # Limit to articles (main namespace)
        'prop': 'extracts',
        'explaintext': True,  # Get plain text extracts
        'exintro': False  # Get the full content, not just the intro
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        data = response.json()

        # Extract the page details
        pages = data['query']['pages']
        # Get the first (and only) page returned
        page = next(iter(pages.values()))

        return {
            'title': page['title'],
            'content': page['extract']
        }
    except requests.RequestException as e:
        print(f"Failed to fetch data: {e}")
        return None

# Fetch a random article and store the content
article = get_random_wikipedia_article()
if article:
    print(f"Title: {article['title']}\n")
    print(f"Content: {article['content']}\n")
else:
    print("Failed to fetch a random Wikipedia article.")