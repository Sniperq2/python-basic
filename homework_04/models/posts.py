from sqlalchemy import Column, Text
from sqlalchemy import String
from sqlalchemy.orm import relationship

from homework_04.models.mixins.create_at_mixin import CreatedAtMixin
from homework_04.models.mixins.user_relation_mixin import UserRelationMixin
from models import Model


class Post(CreatedAtMixin, UserRelationMixin, Model):
    title = Column(
        String(100),
        nullable=False,
        default="",
        server_default="",
    )
    body = Column(Text, nullable=False)

    author = relationship(
        # accessed through `User.posts`
        "User",
        back_populates="posts",
        uselist=False,
    )

    def __repr__(self):
        return str(self)

    def __str__(self):
        return (
            f"Post(id={self.id}, "
            f"title={self.title!r}, "
            f"user_id={self.user_id})"
            f"body={self.body}, "
        )