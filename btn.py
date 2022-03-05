import aiogram
from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

creator = InlineKeyboardButton('🧑🏻‍💻CREATOR🧑🏻‍💻', url='https://t.me/dastur4i_uz')
markup = InlineKeyboardMarkup(row_width=1).add(creator)