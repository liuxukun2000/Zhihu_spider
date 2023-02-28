from hot import HotItem, HotList
from question import Question

if __name__ == '__main__':
    hot_list = HotList()
    print("Get hot list!")
    hot_list.get()
    print("Done!")
    for i in hot_list.items:
        print(i.rank, i.title, i.question_url)

    target = hot_list.items[0]
    question = Question(target.question_id)
    print("Get 5 answers!")
    question.get_step()
    print("Done!")

    for i in question.answers:
        i.user.get_ip_by_token()
        print("Get author ip!", i.answer_id, i.user.username, i.user.area)
    
    answer = question.answers[0]
    print("Get comments!")
    answer.update_comments(l=20)
    print("Done!")
    for comment in answer.comments:
        print(comment.user.username, comment.user.area, comment.content)


