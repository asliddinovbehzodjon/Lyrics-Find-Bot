from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from states.lyrics import Lyricsbot
from aiogram.dispatcher import  FSMContext
from loader import dp
from utils.misc.api import find_lyric
@dp.message_handler(CommandStart(),state=None)
async def test(message:types.Message):
    await message.answer('Assalomu aleykum.Botga Xush kelibsiz!Xonanda nomini kiriting!!!')
    await Lyricsbot.singer.set()
@dp.message_handler(state=Lyricsbot.singer)
async def test2(message:types.Message,state:FSMContext):
    singer=message.text
    await message.answer("Qo'shiq nomini kiriting")
    await state.update_data(
        {'singer':singer}
    )
    await Lyricsbot.next()
@dp.message_handler(state=Lyricsbot.song)
async def test3(message:types.Message,state:FSMContext):
    song=message.text
    await state.update_data(
        {'song':song}
    )
    data = await state.get_data()
    singer=data.get('singer')
    song=data.get('song')

    import requests
    import json
    url = "https://api.lyrics.ovh/v1/" + str(singer)+'/' + str(song)
    print(url)
    rest = requests.get(url)
    if rest.status_code == 200:
        response = json.loads(rest.text)
        #print(response)
        info=response['lyrics']
        if len(info) > 4096:
            for x in range(0, len(info), 4096):
               await message.answer(info[x:x + 4096])
        else:
             await message.answer(info)
        await state.finish()
    else:
        await message.answer('Xatolik')
        await state.finish()



