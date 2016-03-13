#coding = utf-8

from win32 import win32clipboard
import sys, os
import requests
from bs4 import BeautifulSoup

def get_url_content(url):
    response = requests.get(url)
    print("URL: " + response.url)
    response.encoding = "utf-8"
    return response.text

def get_word_from_clipboard():
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    return data

def query_form_youdao(word):
    html = get_url_content("http://dict.youdao.com/w/" + word)
    return html


if __name__ == "__main__":
    word = get_word_from_clipboard()
    if len(sys.argv) == 2:
        wordFromCommand = sys.argv[1]
        word = wordFromCommand
    print("单词: " + word)
    html_parsed = BeautifulSoup(query_form_youdao(word), "html.parser")
    if not html_parsed.find(id = "authDictTrans"):
        print("查询失败")
        os.system("pause")
        exit()
    if not html_parsed.find(id = "authDictTrans"):
        print("21世纪大英汉词典查询失败")
        os.system("pause")
        exit()
    items_list = html_parsed.find(id = "authDictTrans").find_all("ul", recursive = False)
    print("\n21世纪大英汉词典:\n")
    for item in items_list:
        li_list1 = item.find_all("li", recursive = False)
        for i in li_list1:
            if not i.find("span", recursive = False):
                continue
            type = i.find("span", recursive = False).string

            if type == "近义词:":
                print()
            elif type == "短语:":
                print()
            elif i.ul:
                print("----> " + type)
                li_list2 = i.ul.find_all("li", recursive = False)
                for li in li_list2:
                    print("  |->" + li.span.string)

    os.system("pause")

