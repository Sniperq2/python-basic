from datetime import datetime

from sqlalchemy import Column, DateTime, func
from sqlalchemy import String
from sqlalchemy.orm import relationship

from homework_04.models.mixins.create_at_mixin import CreatedAtMixin
from models import Model


class User(CreatedAtMixin, Model):
    name = Column(String(32), nullable=False, unique=True)
    username = Column(String(50), nullable=False, index=True)
    email = Column(String, nullable=True, unique=True)
    created_at = Column(
        DateTime,
        nullable=False,
        default=datetime.utcnow,
        server_default=func.now(),
    )

    posts = relationship(
        # accessed through `Post.author`
        "Post",
        back_populates="author",
        uselist=True,
        # cascade="all, delete-orphan",
    )

    def __repr__(self):
        return str(self)

    def __str__(self):
        return (
            "User("
            f"id={self.id}"
            f", username={self.username!r}"
            f", email={self.email!r}"
            ")"
        )
