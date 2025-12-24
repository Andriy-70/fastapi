from database import Base
import datetime


#доробити!
class Screenshot(Base):
    id: int
    url: str
    sreenshot_path: str
    created_at: datetime.datetime.now()