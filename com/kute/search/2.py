from lxml import html
import requests


def main():
    response = requests.get('http://catalog.data.gov/dataset?q=&sort=metadata_created+desc')
    doc = html.fromstring(response.text)
    for title in doc.cssselect('h3.dataset-heading'):
        print(title.text_content().strip())

if __name__ == '__main__':
    main()
