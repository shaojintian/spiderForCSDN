from src.article_content_spider import ArticleContentSpider
from src.article_id_spider import ArticleIdSpider

"""
Auther : SnailMann
temporary cookies version
"""

HOME_URL = 'https://blog.csdn.net/'
PAGE_URL = '/article/list/'
MARKDOWN_URL = 'https://mp.csdn.net/mdeditor/getArticle?id='

"""User Settings"""
GLO_CONFIG = {
    'download_path': r"./md/",  # Default path
    'download_img': False,  # Default not to download pictures
    'sleep_time': 1,
    'name': 'qq_39871498',  # https://blog.csdn.net/yourname <- yourname
    'cookies': 'uuid_tt_dd=10_37405685640-1570527783741-382274; dc_session_id=10_1570527783741.448498; Hm_ct_6bcd52f51e9b3dce32bec4a3997715ac=6525*1*10_37405685640-1570527783741-382274!1788*1*PC_VC!5744*1*qq_39871498; UserName=qq_39871498; UserInfo=069331a300e247fa93b99347a6953b12; UserToken=069331a300e247fa93b99347a6953b12; UserNick=Enzo%E9%82%B5%E9%9D%B3%E5%A4%A9; AU=186; UN=qq_39871498; BT=1570528629955; p_uid=U100000; hasSub=true; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1574087214,1574087439,1574089440,1574089640; announcement=%257B%2522isLogin%2522%253Atrue%252C%2522announcementUrl%2522%253A%2522https%253A%252F%252Fblogdev.blog.csdn.net%252Farticle%252Fdetails%252F103053996%2522%252C%2522announcementCount%2522%253A0%252C%2522announcementExpire%2522%253A3600000%257D; CloudGuest=O1P8EN83FHymIhQ9a6HbbhGyzHjEUab0yWp9BNI5+UvPmT1Ai2IEGeGZeQAJnJpEuAd1lhaMmdNH2F1/7sh+bT7or2//Yyi92CWbzCSLDnbIAERQKB1ZCK2SGN/gaSIicXgQZAl/z5ZL5QBNruQIMvUdSaglIdTlrl3xD+x66FaZOHMlf82jP07PEWP/WkNk; sid=4kjexnotptqv3bxmglkgumyb; dc_tos=q16zs4; Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1574126510'
}


def _main():
    """
    Main Logic
    :return:
    """
    # Initialization
    article_id_spider = ArticleIdSpider()
    article_content_spider = ArticleContentSpider()
    print("==================================================begin====================================================")
    print("Backup Path : %s" % GLO_CONFIG['download_path'])
    print("Download Picture Or Not ?  %s" % GLO_CONFIG['download_img'])
    print("Crawl article interval : %s seconds" % GLO_CONFIG['sleep_time'])
    print("===========================================================================================================")

    # backup article
    global HOME_URL
    article_ids = article_id_spider.getArticleId(HOME_URL + GLO_CONFIG['name'],
                                                 HOME_URL + GLO_CONFIG['name'] + PAGE_URL)
    article_content_spider.getArticle(GLO_CONFIG['sleep_time'],
                                      GLO_CONFIG['download_path'], GLO_CONFIG['download_img'],
                                      MARKDOWN_URL, article_ids, convert_cookies_to_dict(GLO_CONFIG['cookies']))

    # end
    print('')
    print("===========================================================================================================")
    print("User %s have a total of %s articles, It's all finished. Please check it." % (
        GLO_CONFIG['name'], str(len(article_ids))))
    input("====================================================end====================================================")


def convert_cookies_to_dict(cookies):
    '''
    convert cookies to dict
    :param cookies:
    :return:
    '''
    cookies = dict([l.split("=", 1) for l in cookies.split("; ")])
    print(cookies)
    return cookies


if __name__ == '__main__':
    _main()
