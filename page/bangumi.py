# coding=utf-8
import js2py
from bs4 import BeautifulSoup as Bs
from source import routes, apis
from page.utils import get_channel_info, get_page_pagelets, AcDanmaku

__author__ = 'dolacmeo'


class AcBangumi:
    aa_num = None
    page_obj = None
    page_pagelets = []
    bangumi_data = None
    bangumi_list = None
    vid = None
    item_id = None
    resourceType = 6

    def __init__(self, acer, aa_num: [str, int]):
        if isinstance(aa_num, str) and aa_num.startswith('aa'):
            aa_num = aa_num[2:]
        self.aa_num = str(aa_num)
        self.acer = acer
        self.loading()
        self.set_video()
        self.page_url = f"{routes['bangumi']}{self.aa_num}_36188_{self.item_id}"

    def __repr__(self):
        title = self.bangumi_data.get('showTitle', self.bangumi_data.get('bangumiTitle', ""))
        return f"AcBangumi([ac{self.aa_num}_{self.item_id}]{title})"

    def loading(self):
        req = self.acer.client.get(routes['bangumi'] + self.aa_num)
        self.page_obj = Bs(req.text, 'lxml')
        js_data = self.page_obj.select_one("#pagelet_newheader").find_next_sibling("script").text.strip().split('\n')
        bangumi_data = js_data[0]
        self.bangumi_data = js2py.eval_js(bangumi_data).to_dict()
        bangumi_list = js_data[2]
        self.bangumi_list = js2py.eval_js(bangumi_list).to_dict()
        self.bangumi_data.update(get_channel_info(req.text))
        self.item_id = self.bangumi_data.get("itemId")
        self.vid = self.bangumi_data.get("videoId")
        self.page_pagelets = get_page_pagelets(self.page_obj)

    @property
    def season_data(self):
        return self.bangumi_data.get('relatedBangumis', [])

    @property
    def episode_data(self):
        return self.bangumi_list.get('items', [])

    def set_video(self, num=1):
        if num > len(self.episode_data):
            return False
        this_episode = self.episode_data[num - 1]
        self.vid = this_episode['videoId']
        self.item_id = this_episode['itemId']
        self.bangumi_data.update({
            'videoId': self.vid, 'itemId': self.item_id,
            'showTitle': f"{this_episode['bangumiTitle']} {this_episode['episodeName']} {this_episode['title']}"
        })
        self.page_url = f"{routes['bangumi']}{self.aa_num}_36188_{self.item_id}"
        return True

    def danmaku(self):
        return AcDanmaku(self.acer, self.bangumi_data)

    def comment(self):
        return self.acer.AcComment(f"{self.aa_num}_{self.vid}", 6, self.page_url)

    def like(self):
        return self.acer.like(self.item_id, 18)

    def like_cancel(self):
        return self.acer.like_cancel(self.item_id, 18)

    def favorite_add(self):
        return self.acer.favourite.add(self.aa_num, 1)

    def favorite_cancel(self):
        return self.acer.favourite.cancel(self.aa_num, 1)

    def banana(self):
        return self.acer.throw_banana(self.item_id, 18, 1)
