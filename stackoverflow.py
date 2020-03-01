import requests
from bs4 import BeautifulSoup
import json

res = requests.get("https://stackoverflow.com/questions")

soup = BeautifulSoup(res.text, "html.parser")

questions_data = {
    'questions': []
}

questions = soup.select(".question-summary")

for question in questions:
    q = question.select_one('.question-hyperlink').getText()
    vote_count = question.select_one('.vote-count-post').getText()
    views = question.select_one('.views').attrs['title']
    questions_data['questions'].append({
        'question': q,
        'views': views,
        'vote_count': vote_count
    })

json_data = json.dumps(questions_data)

print(json_data)
