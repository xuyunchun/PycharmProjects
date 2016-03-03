#-*-coding:utf8-*-
import urlparse
import requests
import re
# import sys
# reload(sys)
# sys.setdefaultencoding("utf-8")


# f = open('source.txt','r')
# html = f.read()
# f.close()
# print html


# url = "https://otc.cbex.com/page/s/search/index"
# #获取网页源码
# html = requests.get(url).text
# '''
# 获取图片地址链接
# '''
# urls_field = re.findall('<div class="bdlist_img">(.*?)</a>',html,re.S)
# pic_urls = []
# for field in urls_field:
#     pic_url = re.findall('<img src="(.*?)"/>',field,re.S)
#     pic_urls.append(pic_url)
# print pic_urls
# '''
# 拼接完整地址，下载图片
# '''
# i = 0
# for each in pic_urls:
#     new_full_url = urlparse.urljoin("https://otc.cbex.com",each[0])
#     print "now downloading:" + str(i)
#     pic = requests.get(new_full_url)
#     fp = open('pic\\'+str(i)+'.jpg','wb')
#     fp.write(pic.content)
#     fp.close()
#     i += 1



class PicDownLoader(object):
    def getpictures(self, url):
        #获取网页源码
        html = requests.get(url).text
        urls_field = re.findall('<div class="bdlist_img">(.*?)</a>',html,re.S)
        pic_urls = []
        for field in urls_field:
            pic_url = re.findall('<img src="(.*?)"/>',field,re.S)
            pic_urls.append(pic_url)
        # print pic_urls
        i = 0
        for each in pic_urls:
            new_full_url = urlparse.urljoin("https://otc.cbex.com",each[0])
            print "now downloading:" + str(i)
            pic = requests.get(new_full_url)
            fp = open('pic\\'+str(i)+'.jpg','wb')
            fp.write(pic.content)
            fp.close()
            i += 1



if __name__ =="__main__":
	url = "https://otc.cbex.com/page/s/search/index"
	pic_downloader = PicDownLoader()
	pic_downloader.getpictures(url)
