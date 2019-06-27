from google.cloud import translate

translate_client = translate.Client()

target_lang = 'ru'
translated_text_in_list = []

def get_translate(text):
    """
    translate each section by paragrapfs
    return dist of paragrapgs
    """
    result_text = translate_client.translate(
            text,
            target_language = target_lang)
    print(result_text)
    #result_text['translatedText']
    return result_text['translatedText']


def main():
	with open("contact.txt", 'r') as file:
		lines = file.readlines()
		#print(lines)
		for line in lines:
			trans_line = get_translate(line)
			with open("contact_translated.txt", "a") as f:
				f.write(line.replace("\n", "")+"==="+trans_line+"\n")

if __name__=="__main__":
	main()