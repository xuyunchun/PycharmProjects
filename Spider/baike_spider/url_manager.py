# coding:utf8
class UrlManager(object):
    def __init__(self):
        self.new_urls = set()	#将新url存在set中
        self.old_urls = set()	#将旧url存在set中

    '''
    添加单个新URL方法：
    URL不为空，既不在新URLS中和旧URL中时，添加
    '''
    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.old_urls and url not in self.new_urls:
            self.new_urls.add(url)
    '''
    批量添加新URL方法：
    URLS不为空时，逐个调用单个添加方法
    '''
    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)
    '''
    判断URLS是否为空
    '''
    def has_new_url(self):
        return len(self.new_urls) !=0
    '''
    从新URLS中取出新的一条URL，并将此条URL移至旧URLS中
    '''
    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url

