from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, func
from database import Base
import datetime



class Screenshot(Base):
    __tablename__ = "screenshots"

    id: Mapped[int] = mapped_column(primary_key=True)
    url: Mapped[str] = mapped_column(String(255))
    screenshot_path: Mapped[str] = mapped_column(String(500))
    created_at: Mapped[datetime.datetime] = mapped_column(server_default=func.now())