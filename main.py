from hot import HotItem, HotList
from question import Question as Q
from utils import init

init("/home/satan/Zhihu_spider/database")
from zhihu.models import User, Answer, Question, Comment

# def get_user_or_create(user):


if __name__ == '__main__':

    hot_list = HotList()
    print("Get hot list!")
    hot_list.get()
    print("Done!")
    for i in hot_list.items:
        print(i.rank, i.title, i.question_url)

    target = hot_list.items[0]
    question = Q(target.question_id, target.answer_count, target.title)

    db_question, _ = Question.objects.get_or_create(id=question.question_id, defaults={
        "answer_count": question.answer_count, "content": question.title
    })

    print("Get 5 answers!")
    question.get_step()
    print("Done!")

    for i in question.answers:
        i.user.get_ip_by_token()
        db_user, _ = User.objects.get_or_create(id=i.user.user_id, defaults={
            "username": i.user.username,
            "area": i.user.area,
            "description": i.user.description,
            "gender": i.user.gender,
            "url_token": i.user.url_token
        })
        db_answer, _ = Answer.objects.get_or_create(
            id=i.answer_id,
            defaults={
                "user": db_user,
                "content": i.content,
                "question": db_question,
                "update_time": i.update_time,
                "comment_count": i.comments_count
            }
        )

        print("Get author ip!", i.answer_id, i.user.username, i.user.area)

    answer = question.answers[0]
    print("Get comments!")
    answer.update_comments(l=20)
    print("Done!")
    for i in answer.comments:
        db_user, _ = User.objects.get_or_create(id=i.user.user_id, defaults={
            "username": i.user.username,
            "area": i.user.area,
            "description": i.user.description,
            "gender": i.user.gender,
            "url_token": i.user.url_token
        })
        Comment.objects.get_or_create(
            id=i.comment_id,
            defaults={
                "user": db_user,
                "like": i.like,
                "dislike": i.dislike,
                "children": "",
                "answer": db_answer,
                "content": i.content
            }
        )
        print(i.user.username, i.user.area, i.content)


