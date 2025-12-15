// Timestamp: 2025-12-15 02:09:48

@retry(retries=3, delay=1)
def fetch_remote_resource(url):
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json()

