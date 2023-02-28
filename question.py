#https://www.zhihu.com/api/v4/questions/586488911//answers?include=content&limit=5&offset=10
from user import User
from comments import Comment
import requests
from random import randint

class Answer:
    def __init__(self) -> None:
        self.answer_id = ""
        self.user = None
        self.content = ""
        self.update_time = 0
        self.comments = []
        self.comments_count = -1
    
    def update(self, data, update_comments=False, limit=-1):
        self.answer_id = data['id']
        self.user = User(
            id=data['author']['id'],
            username=data['author']['name'],
            gender=data['author']['gender'],
            description=data['author']['headline'],
            token=data['author']['url_token']
        )
        self.content = data['content']
        self.update_time = data['updated_time']
        if update_comments:
            self.update_comments()

    def update_comments(self, l=-1):
        limit, offset = 20, ""
        while True:
            url = f"https://www.zhihu.com/api/v4/comment_v5/answers/{self.answer_id}/root_comment?order_by=score&limit={limit}&offset={offset}"
            response = requests.get(url)
            data = response.json()
            if self.comments_count == -1:
                self.comments_count = data["counts"]["total_counts"]
            inner_data = data['data']
            for comment in inner_data:
                tmp = Comment()
                tmp.update(comment)
                self.comments.append(tmp)
            offset = f"{randint(0, 9)}_{self.comments[-1].comment_id}_{0}"
            if data['paging']['is_end'] or (l>0 and len(self.comments)>l):
                break


class Question:
    def __init__(self, id) -> None:
        self.question_id = id
        self.answers = []
        self.answer_count = 0
    
    def get_step(self, limit=5, offset=0):
        url = f"https://www.zhihu.com/api/v4/questions/{self.question_id}//answers?include=content&limit={limit}&offset={offset}"
        response = requests.get(url).json()
        data = response['data']
        for answer in data:
            tmp = Answer()
            tmp.update(answer)
            self.answers.append(tmp)
        return offset + limit
    
    def get(self, total=100, limit=0):
        offset = 0
        while len(self.answers) < min(self.answer_count, total):
            offset = self.get_step(limit, offset)
    