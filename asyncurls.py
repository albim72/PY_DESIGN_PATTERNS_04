import concurrent.futures
import urllib.request

URLS = [
    "https://www.foxnews.com/",
    "https://edition.cnn.com/",
    "https://www.bbc.co.uk/",
    "https://www.wp.pl/",
    "https://www.gov.pl/web/obrona-narodowa",
    "https://mil.ru/"
]

def load_url(url,timeout):
    with urllib.request.urlopen(url,timeout=timeout) as conn:
        return conn.read()

with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
    future_to_url = {executor.submit(load_url,url,60):url for url in URLS}
    for future in concurrent.futures.as_completed(future_to_url):
        url = future_to_url[future]
        try:
            data = future.result()
        except Exception as exc:
            print(f'{url} generuje wyjątek: {exc}')
        else:
            print(f'{url} - strona na rozmiar {len(data)} bajtów')
            # print(type(data))
            # print(data)
