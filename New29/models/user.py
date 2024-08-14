from sqlalchemy.orm import Mapped, mapped_column

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(db.String(32), nullable=False)
    password: Mapped[str] = mapped_column(db.String(256), nullable=False)
    role: Mapped[str] = mapped_column(db.String(32), nullable=False)