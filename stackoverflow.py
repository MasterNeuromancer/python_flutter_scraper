import requests
from bs4 import BeautifulSoup

res = requests.get("https://stackoverflow.com/questions")

soup = BeautifulSoup(res.text, "html.parser")

questions = soup.select(".question-summary")

print(questions[0].select_one('.question-hyperlink').getText())
