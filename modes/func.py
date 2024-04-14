import logging

from modes.models import User, Article, Comment, db

# User
"""
用户方法
"""


def user_is_have(username):
    res = User.query.filter_by(username=username).first()
    if res:
        return res, True
    return None, False


def add_user(username, password, email):
    new_user = User(
        username=username,
        password=password,
        email=email
    )
    # 添加到数据库
    db.session.add(new_user)
    db.session.commit()
    return "添加完成", True


# 删除用户
def delete_user(user_id):
    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return "User deleted successfully"
    else:
        return "User not found"


def login_validation(username, password):
    user = User.query.filter_by(username=username).first()
    logging.debug(user)
    if user and user.password == password:
        return "登录成功", True
    return "账号或密码错误", False


# 更新用户信息
def update_user(user_id, username=None, password=None, email=None):
    user = User.query.get(user_id)
    if user:
        if username:
            user.username = username
        if password:
            user.password = password
        if email:
            user.email = email

        db.session.commit()
        return "User updated successfully"
    else:
        return "User not found"


# 查询用户信息
def get_user(user_id):
    user = User.query.get(user_id)
    if user:
        return user
    else:
        return None


# Article
"""
文章方法
"""


def add_article(user_id, sort_id, label_id, article_title, article_content, **kwargs):
    # 添加文章
    new_article = Article(
        user_id=user_id,
        sort_id=sort_id,
        label_id=label_id,
        article_title=article_title,
        article_content=article_content,
        **kwargs
    )
    db.session.add(new_article)
    db.session.commit()
    return new_article


def delete_article(article_id):
    # 删除文章
    article = Article.query.get(article_id)
    if article:
        db.session.delete(article)
        db.session.commit()
        return "Article deleted successfully"
    else:
        return "Article not found"


def update_article(article_id, **kwargs):
    # 更新文章
    article = Article.query.get(article_id)
    if article:
        for key, value in kwargs.items():
            setattr(article, key, value)
        db.session.commit()
        return "Article updated successfully"
    else:
        return "Article not found"


def get_article(article_id):
    # 获取文章信息
    return Article.query.get(article_id)


# 获取所有的文章对象
def get_all_article_object():
    articles = Article.query.all()
    return articles


# 评论
"""
评论方法
"""


# 添加评论
def add_comment_func(source, type, user_id, comment_content, **kwargs):
    new_comment = Comment(source=source, type=type, user_id=user_id, comment_content=comment_content, **kwargs)
    db.session.add(new_comment)
    db.session.commit()
    return "添加评论成功",True


# 删除评论
def delete_comment(comment_id):
    comment = db.session.query(Comment).filter_by(id=comment_id).first()
    if comment:
        db.session.delete(comment)
        db.session.commit()


# 更新评论信息
def update_comment(comment_id, **kwargs):
    comment = db.session.query(Comment).filter_by(id=comment_id).first()
    if comment:
        for key, value in kwargs.items():
            setattr(comment, key, value)
        db.session.commit()


# 查询评论信息
def get_comment(comment_id):
    return db.session.query(Comment).filter_by(id=comment_id).first()


# 查询所有评论
def get_all_comments():
    return db.session.query(Comment).all()



# 使用示例
if __name__ == "__main__":
    # 添加评论
    add_comment(source=1, type='article', user_id=1, comment_content='Test comment')

    # 查询所有评论
    print("所有评论：")
    comments = get_all_comments()
    for comment in comments:
        print(f"ID: {comment.id}, Content: {comment.comment_content}")

    # 查询单条评论
    comment_id = 1
    comment = get_comment(comment_id)
    if comment:
        print(f"\n查询评论：")
        print(f"ID: {comment.id}, Content: {comment.comment_content}")

    # 更新评论信息
    update_comment(1, comment_content="Updated comment")

    # 删除评论
    delete_comment(1)
