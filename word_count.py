from os import mkdir, listdir


def deleteAllNotText():
	total_space = 0
	for direct in listdir('alldirs'):
		for file in listdir('alldirs/' + direct):
			with open('alldirs/' + direct + '/' + file, 'r') as fr:
				lines = fr.readlines()
				with open('alldirs/' + direct + '/' + file, 'w') as fw:
					for line in lines:
						if '\t' not in line and ';' not in line:
							if '\n' in line and len(line)>2:
								fw.write(line)
								#print(line)
				with open('alldirs/' + direct + '/' + file, 'r') as fr:
					text = fr.read()
					# text_without_scripts = f.split('1750 Steeles Ave West, Unit 204, Concord, ON L4K 2L7')[0]
					total_space += text.count(" ")
					#f.write(text_without_scripts)
	print(total_space)


def make_one_file():
	for direct in listdir('alldirs'):
		with open('main_again.txt', 'a') as main_file:
			for file in listdir('alldirs/' + direct):
				with open('alldirs/' + direct + '/' + file, 'r') as fr:
					text = fr.read()
					main_file.write(text)
				main_file.write('\n')


def del_css():
	with open('main.txt', 'r') as main_file:
		text = main_file.read()
		with open('main_result.txt', 'w') as main_file:
			if 'Теги:' in text:
				prev_text = text.split('Теги')[0]


def del_duplicates():
	with open('main_again.txt', 'r') as fr:
		with open('main_k.txt', 'w') as fw:
			with open('duplicates.txt', 'r') as fdr:
				lines_text = fr.readlines()
				lines_dupl = fdr.readlines()
				for tline in lines_text:
					if tline not in lines_dupl:
						fw.write(tline)


def add_spaces():
	count = 1
	with open('main_k.txt', 'r') as fr:
		with open('main.txt', 'a') as fw:
			lines = fr.readlines()
			for line in lines:
				if 'https://' in line:
					fw.write('_________________________________________________________________________________________________')
					fw.write('\n')
					fw.write('\n')
					fw.write('Section № {}'.format(count))
					fw.write('\n')
					fw.write(line)
					fw.write('\n')
					fw.write('\n')
					count += 1
				else:
					fw.write(line)


alfabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def make_more_readable():
	with open('main.txt', 'r') as fr:
		text = fr.read()
		text = text.replace(',\n,', ',')
		text = text.replace('\n ', ' ')
		text = text.replace('\n.', '.')
		text = text.replace(',\n', ',')
		for letter in alfabet:
			if '\n{}'.format(letter) in text:
				text = text.replace(' \n{}'.format(letter), ' ' + letter)
				text = text.replace('\n{}'.format(letter), letter)
	with open('main.txt', 'w') as fw:
		fw.write(text)


if __name__ == '__main__':
	deleteAllNotText()
	make_one_file()
	del_duplicates()
	add_spaces()
	make_more_readable()
