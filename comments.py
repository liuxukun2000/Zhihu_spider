import requests

# response = requests.get("https://www.zhihu.com/api/v4/comment_v5/answers/2914963294/root_comment?order_by=score&limit=20&offset=")
# data = response.json()
# # 2 男 1 女 0 未知
# conut = data["counts"]["total_counts"]
# data = data["data"]
# ans = []
# for item in data:
#     name = item['author']['name']
#     gender = item['author']['gender']
#     content = item['content']
#     area = item['comment_tag'][0]['text']
#     child = item["child_comments"]
#     print(name, gender, content, area)

from user import User
class Comment:
    def __init__(self) -> None:
        self.comment_id = ""
        self.user = None
        self.content = ""
        self.like = 0
        self.dislike = 0
        self.children = []
    
    def update(self, data):
        self.comment_id = data['id']
        self.like = data['like_count']
        self.dislike = data['dislike_count']
        self.children = data['child_comments']
        self.user = User(
            id = data['author']['id'],
            username=data['author']['name'],
            gender=User.convert_gender(data['author']['gender']),
            description=data['author']['headline'],
            area=data['comment_tag'][0]['text'],
            token=data['author']['url_token']
        )
        self.content = data['content']
    


if __name__ == "__main__":

    response = requests.get("https://www.zhihu.com/api/v4/comment_v5/answers/2914963294/root_comment?order_by=score&limit=20&offset=")
    data = response.json()
    # 2 男 1 女 0 未知
    conut = data["counts"]["total_counts"]
    data = data["data"]
    ans = []
    for item in data:
        x = Comment()
        x.update(item)
        print(x.user.area, x.user.user_id)