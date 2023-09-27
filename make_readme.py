import os

from typing import NoReturn

verilog_info = ''

a = ['C#', 'assembler', 'verilog']

folders = ['Python', 'SQL']


def add_space() -> NoReturn:
	code.append('')


def details_open(title: str) -> NoReturn:
	add_space()
	code.append('<details>')
	code.append('<summary>')
	add_space()
	code.append('### ' + title)
	add_space()
	code.append('</summary>')
	ul_open()
	

def details_close() -> NoReturn:
	ul_close()
	code.append('</details>')
	add_space()


def add_line(name: str, url: str) -> NoReturn:
	code.append(f'   - ###### [{name}]({url})')
	add_space()


def ul_open() -> NoReturn:
	add_space()
	code.append('<ul>')
	add_space()


def ul_close() -> NoReturn:
	add_space()
	code.append('</ul>')
	add_space()


def rename_path(path: str) -> str:
	replaced_path = path.replace(' ', '_')
	os.rename(path, replaced_path)
	return replaced_path


url = 'https://github.com/shi-i-chan/practice/tree/main/'
code = []

extensions_list = [
	'.py',
	'.ipynb',
	'.sql',
]

black_list = [
	'autoencoders.py',
	'keras timeseries classification from scratch',
	'keras tutorials',

]

def generate_info(folders):
	for folder in folders:
		if ' ' in folder or '-' in folder: folder = rename_path(folder)
		if os.path.isdir(folder):
			details_open(folder.split('/')[-1])

			sub = [f'{folder}/{file}' for file in os.listdir(folder)]
			folders = [s for s in sub if os.path.isdir(s)]
			files = [s for s in sub if os.path.isfile(s)]
			generate_info(folders + files)

			details_close()
		elif os.path.isfile(folder):
			fn, extension = os.path.splitext(folder)
			if extension in extensions_list:
				add_line(fn.split('/')[-1], f'{url}{folder}')

generate_info(folders)

for row in code:
	print(row)
