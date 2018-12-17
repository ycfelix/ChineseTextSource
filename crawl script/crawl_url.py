import ctext
import json
from time import sleep
from typing import List, Dict
from ratelimit import limits, sleep_and_retry


def produce_urls_list()-> List:
    urls_list = []
    with open("urls.txt", encoding='utf-8') as urls:
        for line in urls:
            start = line.index('<a href="') + 9
            end = line.rindex('"', start)
            urls_list.append(line[start:end])
    return urls_list


def get_text_from_url(url: str)-> Dict:
    return ctext.gettext("ctp:"+url)


def get_data_from_urls(urls: List):
    # hardcoded api call limit which should be 50 per day/hour or sth
    # 0:49 done
    calling = 0
    for url in urls[50:100]:
        raw_text = get_text_from_url(url)
        file_title = 'data/' + raw_text['title'] + '.json'
        with open(file_title, "w", encoding='utf-8') as f:
            f.write(json.dumps(raw_text, ensure_ascii=False))
        print("Got " + raw_text['title'])
        calling += 1
        if calling % 50 == 0:
            print("Finished call " + str(calling))


if __name__ == "__main__":
    urls_list = produce_urls_list()
    get_data_from_urls(urls_list)
