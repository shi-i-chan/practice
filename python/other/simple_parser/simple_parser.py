# June 2018

# IDE Sublime Text

# requests 2.25.1
# pandas 1.2.4
# bs4 4.11.1

import sys
import requests
import pandas as pd
from bs4 import BeautifulSoup

def progress_bar(count, total, status=''):
	bar_len = 60
	filled_len = int(round(bar_len * count / float(total)))

	percents = round(100.0 * count / float(total), 1)
	bar = '=' * filled_len + '-' * (bar_len - filled_len)

	sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))
	sys.stdout.flush()

old_words = pd.read_csv("old_words.csv", index_col=0).Word.tolist()

with open("new_words.txt") as file:
    new_words = file.readlines()
    new_words = [line.rstrip() for line in new_words]

words = list(set(new_words) - set(old_words))

LINK = "https://wooordhunt.ru/word/"
USA = "американская транскрипция слова "

tot = len(words)

pronuntiations = []
translates = []

counter = 0
for word in words:
	page_html = requests.get(LINK + word)
	page_text = BeautifulSoup(page_html.text, 'html.parser')
	pron = page_text.find('span', attrs={'class': 'transcription', 'title': USA + word})
	if pron is not None:
		pronuntiation = pron.text.strip().replace("|", "")
		rus = page_text.find('div', attrs={'class': 't_inline_en'})
		if rus is not None:
			translate = rus.text.strip()

			pronuntiations.append(pronuntiation)
			translates.append(translate)
	#time.sleep(2)
	counter += 1
	progress_bar(counter, tot, status=" STATUS")

df = pd.DataFrame({'Word': words,
				   'Pronuntiation': pronuntiations,
				   'Translate': translates})

df.to_csv('new_new_words.csv') # file with translates