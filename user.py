import requests

class User:
    def __init__(self, id, username, area = "", description = "", gender = 0, token="") -> None:
        self.user_id = id
        self.username = username
        self.area = area
        self.description = description
        self.gender = gender
        self.url_token = token
    
    @staticmethod
    def convert_gender(gender: int) -> str:
        if gender == 1:
            return "女"
        elif gender == 2:
            return "男"
        return "未知"
    
    def get_ip_by_token(self):
        if self.url_token:
            url = f"https://www.zhihu.com/api/v4/members/{self.url_token}?include=allow_message,is_followed,is_following,is_org,is_blocking,employments,answer_count,follower_count,articles_count,gender,badge[?(type=best_answerer)].topics"
            response = requests.get(url).json()
            self.area = response['ip_info']

if __name__ == '__main__':
    user = User("", "", token="yang-guang-kong-qi-shui-71")
    user.get_ip_by_token()
    print(user.area)
