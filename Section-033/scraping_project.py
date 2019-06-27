from bs4 import BeautifulSoup
from random import choice
import requests 

BASE_URL = "http://quotes.toscrape.com"

def get_request(url):
    response = requests.get(url)
    if response.status_code == 200:
        html_str = response.text
    else:
        html_str = ""
    return html_str


def get_quote_info():
    quotes = []
    url = BASE_URL

    while url:
        html_str = get_request(url)
        html_page = BeautifulSoup(html_str, "html.parser")
        quotes_html = html_page.select("div.quote")
        if len(html_page.select("li.next a")) > 0:
            url = BASE_URL + html_page.select("li.next a")[0]['href']
        else:
            url = None
        for q in quotes_html:
            quote = q.select("span.text")[0].get_text()
            span = q.select("span")[1]
            quote_author = span.select("small.author")[0].get_text()
            quote_author_bio_url = span.select("a")[0]["href"]

            quotes.append({'quote': quote, 'author': quote_author, 'link': quote_author_bio_url})
    return quotes


def get_author_info(partial_url):
    html_str = get_request(f"{BASE_URL}{partial_url}")
    html_page = BeautifulSoup(html_str, "html.parser")
    author_birth_date = html_page.select("span.author-born-date")[0].get_text()
    author_birth_loc = html_page.select("span.author-born-location")[0].get_text()
    return {'date': author_birth_date, 'location': author_birth_loc}


def round(quote_info):
    author_info = get_author_info(quote_info['link'])
    tips = []
    name = quote_info['author'].split(' ')
    tips.append(f"The author's first name starts with {name[0][0]}")
    tips.append(f"The author's last name starts with {name[1][0]}")
    tips.append(f"The author was born on {author_info['date']}.")
    tips.append(f"The author was born {author_info['location']}.")
    tips.append(f"There are {len(name[0])} letters in the author's first name.")
    tips.append(f"There are {len(name[1])} letters in the author's last name.")

    guesses_left = 4
    print('\n\n') 
    print('=' * 100)
    print(quote_info['quote'])
    print("\n")
    guess = input(f"Who is this quote from (you have {guesses_left} guesses left)? ")
    
    while guesses_left > 1:
        if guess.lower() == quote_info['author'].lower():
            print("You WIN!")
            return
        else:
            guesses_left -= 1
            print(f'\nNope, try again. You have {guesses_left} guesses left.')
            guess = input(f'Hint: {choice(tips)}: ')
            
    print(f"You lose. The author was {quote_info['author']}.")
    return


def game():
    quotes = get_quote_info()

    while True:
        round(choice(quotes))
        text = input('\n\nWould you like to play again (y/n)? ')
        if text.lower() == 'n':
            break


game()