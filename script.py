from bs4 import BeautifulSoup

def load_all_text_from_site():
	#for file in os.listdir():
	with open('index.html', 'r') as file:
		soup = BeautifulSoup(file, 'html.parser')
		text = soup.find_all(text=True)

		output = ''
		blacklist = [
			'[document]',
			'noscript',
			'header',
			'html',
			'meta',
			'head', 
			'input',
			'script',
			# there may be more elements you don't want, such as "style", etc.
		]

		for t in text:
			if t.parent.name not in blacklist and text != ' ':
				output += '{}\n'.format(t)

		print(output)

def main():
	load_all_text_from_site()


if __name__=='__main__':
	main()