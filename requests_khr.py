import requests
from bs4 import BeautifulSoup



url = "https://yandex.com/news/rubric/politics?from=index"

yandex_politics_request = requests.get(url)

if yandex_politics_request.status_code == 200:
    print('Yay! We performed a successfull request')
else:
    print('Oops! Something went wrong...')

parsed_page = BeautifulSoup(yandex_politics_request.text, 'html.parser')

page_title_tag = parsed_page.title
print('Page title HTML tag: ', page_title_tag)

page_title_text = page_title_tag.text
print('Page title text: ', page_title_text)
print(type(page_title_tag))
print(page_title_tag.name)
print(page_title_tag.attrs)

print('Elements with id: ', page_title_tag.get('id'))
print('Elements with h3: ', parsed_page.h3)
print('Elements with h2: ', parsed_page.h2)

parsed_news_section = parsed_page.select_one('#root section.b-section')

