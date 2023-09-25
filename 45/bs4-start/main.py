from bs4 import BeautifulSoup
import requests

def main() -> None:    
    response = requests.get('https://news.ycombinator.com/')
    soup = BeautifulSoup(response.text, 'html.parser')
    # get all the titles and links inside athe span with the class 'titleline'
    titles = soup.select('.titleline > a')
    # print the titles: links
    for title in titles:
        print(title.text, title['href'])
        print('='*100)
    
if __name__ == '__main__':
    main()