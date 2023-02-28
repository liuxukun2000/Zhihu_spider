import requests
import pandas as pd
from utils import get_time
from typing import List, Dict
from random import randint

class HotItem:
    def __init__(self, rank, title, answer_count, follower_count, hot, question_url, id) -> None:
        self.rank = rank
        self.title = title
        self.answer_count = answer_count
        self.follower_count = follower_count
        self.hot = hot
        self.question_url = question_url
        self.question_id = id
        

    @staticmethod
    def convert(rank, item):
        target = item.get('target')
        title = target.get('title')
        answer_count = target.get('answer_count')
        hot = int(item.get('detail_text').split(' ')[0])
        follower_count = target.get('follower_count')
        question_url = target.get('url').replace('api', 'www').replace('questions', 'question')
        id = target.get('id')

        return HotItem(rank, title,answer_count, follower_count, hot, question_url, id)

class HotList: 
    def __init__(self) -> None:
        self.headers: List[Dict[str, str]] = [
            {
                'User-Agent': 'osee2unifiedRelease/4318 osee2unifiedReleaseVersion/7.7.0 Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
                'Host': 'api.zhihu.com'
            }
        ]
        self.params = (
                ('limit', '50'),
                ('reverse_order', '0'),
            )
        self.items: List[HotItem] = []
    
    def get_header(self) -> Dict[str, str]:
        index = randint(0, len(self.headers) - 1)
        return self.headers[index]

    def get(self) -> None:
        response = requests.get(
                'https://zhihu.com/topstory/hot-list', 
                headers=self.get_header(), 
                params=self.params
            )
        items = response.json()['data']

        for rank, item in enumerate(items, start=1):
            self.items.append(HotItem.convert(rank, item))
        

if __name__ == '__main__':
    x = HotList()
    x.get()
    # print(x.items)
    for i in x.items:
        print(i.rank, i.title, i.question_id)