# coding: utf-8
from bs4 import BeautifulSoup, NavigableString
from urllib.request import urlopen
from os import mkdir, listdir

def openFile(filename):
	with open(filename, 'r') as file:
		f = file.read()
	return f	


# def downloadAll():
# 	with open('urllist.txt', 'r') as l:
# 		url = l.readline()

# 		while url:
# 			response = urlopen(url, timeout = 5)
# 			timesleep = 2
# 			content = response.read()
# 			print(url)
# 			name_dir = url.split('/')[3]
# 			name_file = url.split('/')[-2]
# 			print(name_file)

# 			if name_file == '':
# 				name_file = 'index'

# 			if not name_dir in listdir():
# 				mkdir(name_dir)
# 			getcontext(content, url, name_dir + '/' + name_file + '.txt')

# 			url = l.readline()

def get_all_files():
	with open("list_of_html", 'r') as f:
		lines = f.readlines()

	result_lines = [line.replace("\n", "") for line in lines]
	
	return result_lines


def getcontext(file, file_to_save):
	soup = BeautifulSoup(openFile(file), 'html.parser')
	#edvs = soup.find('div', {'id': 'maincontentcontainer'})
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
	try:
		second_sentence = soup.div.find_all_next(text=True)
	except Exception as exc:
		print(exc)
	else:

		with open(file_to_save, 'a') as f:
			f.write(file + '\n')
			for item in second_sentence:
				if item != '1750 Steeles Ave West, Unit 204, Concord, ON L4K 2L7':
					if item == '\n':
						pass
					else:	
						print(item)
						f.write(item + '\n')		

	return True


def main():
	#downloadAll()
	# files = get_all_files()
	# for file in files:
	# 	getcontext(file, "main.txt")
	# with open("goal.txt", "r") as file:
	# 	text = file.read()
	# 	with open("dublicaties.txt", 'r') as dup_file:
	# 		dupls = dup_file.readlines()
	# 		for dupl in dupls:
	# 			text = text.replace(dupl, "\n")
	# 		with open("goal1.text", "w") as f:
	# 			f.write(text)
	# index = ['index.html']
	# for i in index:
	# 	getcontext(i, "index.txt")
	with open("index.txt", "r") as file:
		lines = file.readlines()
		text = ""
		for line in lines:
			if line.startswith('\n') or line.startswith(' \n') or line.startswith(','):
				pass
			else:
				text += line
		with open("index.goal.txt", "w") as f:
			f.write(text)


if __name__ == '__main__':
	main()