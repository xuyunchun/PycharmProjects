# coding:utf8
import urllib2
'''
urllib2.urlopen()获取网页内容
	getcode=200表示获取成功
	read() 获取内容
'''

class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return None
        response = urllib2.urlopen(url)

        if response.getcode() != 200:
            return None
        return response.read()