# coding:utf8
'''
爬虫主程序
通过调用URL管理器、URL下载器、解析器、输出器完成网页内容的抓取和下载输出
'''
from baike_spider import url_manager,html_downloader,html_parser,html_outputer


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()
	'''
	抓取方法，输入URL，输出output.html文件
	主要逻辑:
	URL管理器输入要获取的URL
	
	'''
    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print 'craw %d:%s' % (count,new_url)
                html_cont = self.downloader.download(new_url)
                new_urls,new_data = self.parser.parse(new_url,html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)

                if count==10:
                    break
                count = count + 1
            except:
                print 'craw failed'

        self.outputer.output_html()


if __name__=="__main__":
    root_url="http://baike.baidu.com/link?url=44FMe6cQ7AS0jVHUuhfk-KmMNEYal1z_SenfodKnQPWB0d_x8h5EwLpwcJDV3iEoY5MVJFjbFk4CEzPl-Eeo2_"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
