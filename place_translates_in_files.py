

def get_indexes():
	indexes = []
	with open("translated.txt", 'r') as file:
		count = 1
		lines = file.readlines()
		for line in lines:
			try:
				first, second = line.split("===")
			except Exception as exc:
				print(exc)
			else:
				if '/' in first and not "var" in first:
					indexes.append(count)
			count += 1

	return indexes


def main():
	indexes = get_indexes()
	with open("translated.txt", 'r') as file:
		count = 1
		lines = file.readlines()
		for line in lines:
			try:
				first, second = line.split("===")
				#print(first)
			except Exception as exc:
				print(exc)
			else:
				if '/' in first and not "var" in first and first != 'Green roof planting list / planting schedule':
					try:
						with open(first, 'r') as f:
							text = f.read()
							#print(count, indexes[indexes.index(count)+1])
							res = replace_text(lines[count:indexes[indexes.index(count)+1]], text)
							if res:
								with open(first, 'w') as fil:
									fil.write(res)
					except Exception as exc:
						print(exc)
			count += 1


def one_file_place(from_file, to_file):
	with open(from_file, "r") as file:
		lines = file.readlines()
		with open(to_file, 'r') as f:
			text = f.read()
			res = replace_text(lines, text)
			if res:
				with open(to_file, 'w') as fil:
					fil.write(res)


def replace_text(lines, filetext):
	for line in lines:
		#print("in 1")
		try:
			first, second = line.split("===")
		except Exception as exc:
			print(exc)
		else:
			if first in filetext:
				print("we are replacing!")
				filetext = filetext.replace(first, second)

	return filetext




def place_same_text_in_all_site():
	with open("translated.txt", "r") as file:
		t_lines = file.readlines()
		with open("list_of_html", "r") as f:
			l_lines = f.readlines()
			for line in l_lines:
				with open(line.replace("\n", ""), 'r') as ff:
					text = ff.read()
					for tl in t_lines:
						try:
							first, second = tl.split("===")
							text = text.replace(first, second)
							with open(line.replace("\n", ""), 'w') as fff:
								fff.write(text)
						except Exception as exc:
							print(exc)


if __name__=="__main__":
	#print(get_indexes())
	#one_file_place("translated.txt", "index.html")
	place_same_text_in_all_site()

# def index_translate():
# 	with open