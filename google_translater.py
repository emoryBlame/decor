# coding: utf-8
from time import sleep
from threading import Thread
from google.cloud import translate

translate_client = translate.Client()

target_lang = 'heb'
translated_text_in_list = []

class TranslateTread(Thread):
    def __init__(self, name, data_list):
        super().__init__()
        self.name = name
        self.data = data_list
        print('Thread # {} started with data {} - {}'
            .format(self.name, str(self.data[0]["number"]), str(self.data[-1]["number"])))

    def run(self):
        translated_text_in_dist = {}
        for el in self.data:
            el['main_text'] = share_text_by_paragraph(el['main_text'])
            translated_text_in_dist = {
                "number": el['number'],
                "url": el['url'],
                "main_text": get_translate(el['main_text']) #el['main_text'] # get_translate(el['main_text']) #
            }
            translated_text_in_list.append(translated_text_in_dist)
            #print(translated_text_in_dist)


def conform_a_data():
    """
    share a text to the title, url
    return dict of dicts
    """
    applied_list = []
    with open('main_last.txt', 'r') as fr:
        text = fr.read()
        text = text.replace('_', '')
        sections = text.split('Section № ')
        for section in sections[1:]:
            section_number = section.split('\n')[0]
            section_url = section.split('\n')[1]
            section_text = section.split('\n\n\n')[1]
            section_dict = {
                'number': section_number,
                'url': section_url,
                'main_text': section_text,
            }
            applied_list.append(section_dict)
    return applied_list


def share_text_by_paragraph(text):
    """
    share text per paragraph
    return dist of current text part of section
    """
    dict_of_paragraphs = {}
    count = 0
    paragraphs = text.split('\n')
    for pr in paragraphs:
        if pr != '' and pr != ' ':# or len(pr) < 1:
            dict_of_paragraphs[count] = pr
            count += 1
    return dict_of_paragraphs


def get_translate(text_dict):
    """
    translate each section by paragrapfs
    return dist of paragrapgs
    """
    count = 0
    result_dist = {}
    for text in text_dict.values():
        result_dist[count] = translate_client.translate(
            text,
            target_language = target_lang)['translatedText']
        count += 1
    return result_dist


def make_a_file(result_list):
    """
    write translated text into the file
    """
    with open('translated.txt', 'w') as f:
        for item in result_list:
            f.write("________________________________________________________________\n")
            f.write("Section №" + item['number'] + '\n')
            f.write(item["url"]+ '\n\n')
            for text_item in item['main_text'].values():
                f.write(text_item + "\n")
            f.write("\n\n")


def get_tread():
    data_list = conform_a_data()
    for i in range(0, 3):
        #print(i, data_list[i*5:5*(i+1)])
        tr = TranslateTread(i, data_list[i*5:5*(i+1)])
        tr.start()
    sleep(15)
    print(len(translated_text_in_list))
    return translated_text_in_list

def no_more_thead():
    data_list = conform_a_data()
    for el in data_list:
        el['main_text'] = share_text_by_paragraph(el['main_text'])
        translated_text_in_dist = {
            "number": el['number'],
            "url": el['url'],
            "main_text": get_translate(el['main_text']) #el['main_text'] # get_translate(el['main_text']) #
        }
        translated_text_in_list.append(translated_text_in_dist)
        sleep(2)
    print(len(translated_text_in_list))
    return translated_text_in_list

def main():
    """
    main def per getting list of dist per each section
    """
    tread = False
    if tread:
        translated_text_in_list = get_tread()
    else:
        translated_text_in_list = no_more_thead()

    return translated_text_in_list


if __name__ == '__main__':
    data = main()
    make_a_file(data)
