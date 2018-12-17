from typing import List


def produce_urls_list()-> List:
    urls_list = []
    with open("urls.txt", encoding='utf-8') as urls:
        for line in urls:
            start = line.index('<a href="') + 9
            end = line.rindex('"', start)
            urls_list.append(line[start:end])
    return urls_list


if __name__ == "__main__":
    urls_list = produce_urls_list()
