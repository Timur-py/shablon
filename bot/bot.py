from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import config

storage=MemoryStorage()
bot = Bot(token=config.cfg['7002314147:AAEKemz8AEgrTFGgGRVxyh1oRQVqmoWb9VQ'])
dp = Dispatcher(bot, storage=storage)