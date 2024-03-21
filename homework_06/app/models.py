from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import DeclarativeBase, declared_attr, relationship


class Models(DeclarativeBase):
    id = Column(Integer, primary_key=True)

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"


class Post(Models):
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


class User(Models):
    name = Column(String(32), nullable=False, unique=True)
    username = Column(String(50), nullable=False, index=True)
    email = Column(String, nullable=True, unique=True)

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
