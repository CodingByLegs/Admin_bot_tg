from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

from data import config
from utils.sql import create_pool

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

loop = asyncio.get_event_loop()
db = loop.run_until_complete(create_pool())
