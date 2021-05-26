# from scrapy.cmdline import execute
# import os
# import sys

# if __name__ == '__main__':

#     sys.path.append(os.path.dirname(os.path.abspath(__file__)))
#     # execute(['scrapy','crawl','weibo','-O','weibo.json'])
#     # execute(['scrapy','crawl','hot'])
#     execute(['scrapy','crawl','zhihu'])
from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess

def main():
    setting = get_project_settings()
    process = CrawlerProcess(setting)
    # WorkSpider = ['hot','weibo','zhihu']
    WorkSpider = ['hot']



    for spider_name in WorkSpider:
        print("Running spider %s" % (spider_name))
        process.crawl(spider_name)
    process.start()

if __name__ == '__main__':
    main()