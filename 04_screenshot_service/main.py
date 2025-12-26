from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession

# Імпорти твоїх модулів
from database import engine, Base, get_db
from models import Screenshot
from service import make_screenshot
from schemas import ScreenshotCreate

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Цей блок створює таблиці в базі при старті сервера
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(
    title="Screenshot Service",
    lifespan=lifespan
)

@app.post("/screenshots")
async def screen(data: ScreenshotCreate, db: AsyncSession = Depends(get_db)):
    # 1. Робимо скріншот через Playwright
    path = await make_screenshot(data.url)

    # 2. Створюємо запис для бази даних
    new_screenshot = Screenshot(
        url=data.url,
        screenshot_path=path
    )

    # 3. Зберігаємо в SQLite
    db.add(new_screenshot)
    await db.commit()
    await db.refresh(new_screenshot)

    # 4. Повертаємо об'єкт (FastAPI сам конвертує його в JSON)
    return new_screenshot