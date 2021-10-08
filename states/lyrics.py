from aiogram.dispatcher.filters.state import StatesGroup,State

class Lyricsbot(StatesGroup):
    singer=State()
    song=State()
