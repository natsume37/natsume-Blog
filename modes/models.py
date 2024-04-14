from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), nullable=False, unique=True, comment='用户名')
    password = db.Column(db.String(128), nullable=False, comment='密码')
    phone_number = db.Column(db.String(16), comment='手机号')
    email = db.Column(db.String(32), comment='用户邮箱')
    user_status = db.Column(db.Boolean, nullable=False, default=True, comment='是否启用[False:否，True:是]')
    gender = db.Column(db.Integer, comment='性别[1:男，2:女，0:保密]')
    open_id = db.Column(db.String(128), comment='openId')
    avatar = db.Column(db.String(256), comment='头像')
    admire = db.Column(db.String(32), comment='赞赏')
    subscribe = db.Column(db.Text, comment='订阅')
    introduction = db.Column(db.String(4096), comment='简介')
    user_type = db.Column(db.Integer, nullable=False, default=2, comment='用户类型[0:admin，1:管理员，2:普通用户]')
    create_time = db.Column(db.DateTime, nullable=False, server_default=db.func.current_timestamp(), comment='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, server_default=db.func.current_timestamp(),
                            onupdate=db.func.current_timestamp(), comment='最终修改时间')
    update_by = db.Column(db.String(32), comment='最终修改人')
    deleted = db.Column(db.Boolean, nullable=False, default=False, comment='是否删除[False:未删除，True:已删除]')

    def __repr__(self):
        return f"User(id={self.id}, username={self.username})"




class Article(db.Model):
    # 文章表模型类
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False, comment='用户ID')
    sort_id = db.Column(db.Integer, nullable=False, comment='分类ID')
    label_id = db.Column(db.Integer, nullable=False, comment='标签ID')
    article_cover = db.Column(db.String(256), comment='封面')
    article_title = db.Column(db.String(32), nullable=False, comment='博文标题')
    article_content = db.Column(db.Text, nullable=False, comment='博文内容')
    video_url = db.Column(db.String(1024), comment='视频链接')
    view_count = db.Column(db.Integer, default=0, nullable=False, comment='浏览量')
    like_count = db.Column(db.Integer, default=0, nullable=False, comment='点赞数')
    view_status = db.Column(db.Boolean, default=True, nullable=False, comment='是否可见')
    password = db.Column(db.String(128), comment='密码')
    tips = db.Column(db.String(128), comment='提示')
    recommend_status = db.Column(db.Boolean, default=False, nullable=False, comment='是否推荐')
    comment_status = db.Column(db.Boolean, default=True, nullable=False, comment='是否启用评论')
    create_time = db.Column(db.DateTime, default=db.func.current_timestamp(), nullable=False, comment='创建时间')
    update_time = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp(),
                            nullable=False, comment='最终修改时间')
    update_by = db.Column(db.String(32), comment='最终修改人')
    deleted = db.Column(db.Boolean, default=False, nullable=False, comment='是否启用')


# 评论类
class Comment(db.Model):
    __tablename__ = 'comment'

    id = db.Column(db.Integer, primary_key=True)
    source = db.Column(db.Integer, nullable=False)
    type = db.Column(db.String(32), nullable=False)
    parent_comment_id = db.Column(db.Integer, default=0, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    floor_comment_id = db.Column(db.Integer)
    parent_user_id = db.Column(db.Integer)
    like_count = db.Column(db.Integer, default=0, nullable=False)
    comment_content = db.Column(db.String(1024), nullable=False)
    comment_info = db.Column(db.String(256))
    create_time = db.Column(db.DateTime, default=db.func.current_timestamp(), nullable=False)

    def __repr__(self):
        return f"<Comment(id={self.id}, source={self.source}, type={self.type}, user_id={self.user_id}, comment_content='{self.comment_content}')>"
