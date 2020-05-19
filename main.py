import bs4
import requests
import time
from selenium import webdriver
import urllib


YANDEX_IMAGES = 'https://yandex.ru/images/search?from=tabbar&text={}' # слова разделяются %20

BING_IMAGES ='https://www.bing.com/images/search?q={}&form=HDRSC2&first=1&cw=1350&ch=943' # слова разделяются +

GOOGLE_IMAGES ='https://www.google.com/search?q={}&tbm=isch&ved=2ahUKEwiH6rG6lb7pAhVMON8KHRAsDQ0Q2-cCegQIABAA&oq&gs_lcp=CgNpbWcQARgAMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnUPGqA1jxqgNg6LcDaAFwAHgAgAEAiAEAkgEAmAEAoAEBqgELZ3dzLXdpei1pbWewAQk&sclient=img&ei=xeTCXsfzNczw_AaQ2LRo&bih=943&biw=1920&hl=ru'
# слова разделяются +


class ParseImage(object):
    def __init__(self , user_browser : str , item : str):
        self.yandex = YANDEX_IMAGES
        self.bing = BING_IMAGES
        self.google = GOOGLE_IMAGES
        self.session = requests.Session()
        self.headers= {'accept': '*/*',
                       'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/81.0.4044.138 Chrome/81.0.4044.138 Safari/537.36'}

        self.user_browser = user_browser
        self.href = ''
        self.item = item
        self.list_href = []
        self.selection = ('a.serp-item__link',
                          'img.rg_i.Q4LuWd.tx8vtf',
                          'img.mimg')

        self.href_selection =('href',
                              'src')

        self.new_dop_href = ('https://yandex.ru/')

    def parametrization(self):
        self.href = self.href.format(self.parse_name())
        return self.href

    def parse_name(self):
        result_name = ''
        if self.href == self.yandex:
            for i in self.item.split():
                if len(self.item) <2 or i == self.item[-1]:
                    result_name+=i
                else:
                    result_name +=i +'%20'


        elif self.href == self.google or self.href == self.bing:
            for i in self.item.split():
                if len(self.item) < 2 or i == self.item[-1]:
                    result_name += i
                else:
                    result_name += i + '+'

        return result_name

    def choice_browser(self):
        if self.user_browser == 'chrome':
            self.href = self.google

        elif self.user_browser == 'yandex':
            self.href = self.yandex

        elif self.user_browser == 'bing' :
            self.href = self.bing

        else :
            print('Вы ошиблись повторите еще раз пожалуйста')

    def get_url(self):
        r = self.session.get(self.href)

        return r


    def parser(self , flag):
        if flag == 'chrome':
            self.work(self.selection[1] , self.href_selection[1])

        elif flag == 'yandex':
            self.work(self.selection[0], self.href_selection[0])

        elif flag =='bing' :
            self.work(self.selection[2] , self.href_selection[1])

    def work(self , selection , href_image):
        print(selection)
        print(self.get_url().url)
        soup = bs4.BeautifulSoup(self.get_url().content, 'lxml')
        images = soup.select(selection)
        print(images)
        for href in images:
            print(href[href_image])
            self.list_href.append(href[href_image])

    def download_page(self):
        for href in self.list_href:
            resource = urllib.urlopen(href)
            out = open("...\img.jpg", 'wb')
            out.write(resource.read())
            out.close()

    def scrolling_web_page(self):
        pass


if __name__ == '__main__':
    user_browser_output = str(input('Введите с какого браузера вам парсить картинки : chrome или yandex или bing вводите также как указано на экране ')).lower().strip()
    user_item_output = str(input('Введите поисковый запрос')).lower().strip()
    clf = ParseImage(user_browser_output , user_item_output)
    clf.choice_browser()
    clf.parametrization()
    clf.parser(clf.user_browser)





