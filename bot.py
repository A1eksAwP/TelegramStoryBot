from aiogram import Bot, Dispatcher, executor, types
from weather import get_weather
import logging
import time
from tokens import bot_token
from kata import Kata
import requests
import json
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ParseMode, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, \
    CallbackQuery
import aiogram.utils.markdown as md
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from str_helper import STR_HELP, INT_HELP, FLOAT_HELP, BYTE_HELP, SET_HELP, TUPLE_HELP, DICT_HELP, LIST_HELP
from random import shuffle as sh
from random import choice as ch
from eggs import eggs_pictures, eggs, eggs_dict, battle_eggs, final_states


MESSAGE = '{}, надеюсь, ты в прекрасном настроении!))'

bot = Bot(bot_token)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


class PSGroup(StatesGroup):
    tell = State()
    last_tell = State()
    edit_tell = State()
    help_str = State()
    help_int = State()
    help_float = State()
    help_byte = State()
    help_set = State()
    help_list = State()
    help_tuple = State()
    help_dict = State()


@dp.message_handler(commands=['story'])
async def story_handler(message: types.Message):
    await PSGroup.tell.set()
    await message.reply('Начинай историю, а я попробую ее продолжить! Для остановки введи: "!stop!"')


@dp.message_handler(commands=['egg_restart'])
async def restart_eggs(message: types.Message):
    battle_eggs.clear()
    global eggs
    eggs.clear()
    eggs = ['красный', 'черный', 'зеленый', 'бело-черный', 'желтый', 'голубой', 'коричневый', 'многоцветный']
    await message.reply(f'Корзиночка с пасхальными яйцами снова заполнена полностью! Сейчас там {len(eggs)} яиц.')


@dp.message_handler(commands=['str'])
async def get_help_str(message: types.Message):
    await PSGroup.help_str.set()
    await message.reply('Какие методы строк в Python тебя интересуют? Для остановки введи: "!exit!"')


@dp.message_handler(commands=['int'])
async def get_help_int(message: types.Message):
    await PSGroup.help_int.set()
    await message.reply('Какие методы для целых чисел в Python тебя интересуют? Для остановки введи: "!exit!"')


@dp.message_handler(commands=['float'])
async def get_help_float(message: types.Message):
    await PSGroup.help_float.set()
    await message.reply('Какие методы для вещественных чисел в Python тебя интересуют? Для остановки введи: "!exit!"')


@dp.message_handler(commands=['list'])
async def get_help_list(message: types.Message):
    await PSGroup.help_list.set()
    await message.reply('Какие методы списка в Python тебя интересуют? Для остановки введи: "!exit!"')


@dp.message_handler(commands=['set'])
async def get_help_set(message: types.Message):
    await PSGroup.help_set.set()
    await message.reply('Какие методы множества в Python тебя интересуют? Для остановки введи: "!exit!"')


@dp.message_handler(commands=['dict'])
async def get_help_dict(message: types.Message):
    await PSGroup.help_dict.set()
    await message.reply('Какие методы словарей в Python тебя интересуют? Для остановки введи: "!exit!"')


@dp.message_handler(commands=['tuple'])
async def get_help_tuple(message: types.Message):
    await PSGroup.help_tuple.set()
    await message.reply('Какие методы кортежей в Python тебя интересуют? Для остановки введи: "!exit!"')


@dp.message_handler(commands=['byte'])
async def get_help_byte(message: types.Message):
    await PSGroup.help_byte.set()
    await message.reply('Какие методы байтов в Python тебя интересуют? Для остановки введи: "!exit!"')


@dp.poll_answer_handler()
async def continue_story(message: types.Message, text: str, state: FSMContext):
    temp = {"prompt": text}
    question = json.dumps(temp)
    response = 'https://pelevin.gpt.dobro.ai/generate/'
    reply = requests.post(response, question)
    data = reply.json()
    reply_text = data.get('replies')[0]
    async with state.proxy() as data:
        data['last_tell'] = reply_text
    reply_markup = InlineKeyboardMarkup().add(
        InlineKeyboardButton(text="Сгенерировать другой вариант", callback_data="reload")
    )
    await message.answer(reply_text, reply_markup=reply_markup)


@dp.callback_query_handler(text="reload", state='*')
async def story_reload(message: types.Message, state: FSMContext):
    # await query.message.delete()
    async with state.proxy() as data:
        text = data['tell']
    await continue_story(message, text, state)


# Добавляем возможность выйти из состояния истории
@dp.message_handler(state='*', commands='cancel')
@dp.message_handler(Text(equals='!stop!', ignore_case=True), state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return

    await state.finish()
    await message.reply('Спасибо! Отличный получился рассказ!')


# Добавляем возможность выйти из состояния документации
@dp.message_handler(state='*', commands='cancel')
@dp.message_handler(Text(equals='!exit!', ignore_case=True), state='*')
async def str_exit_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return

    await state.finish()
    await message.reply('Класс, я уверен, что все эти методы точно помогут тебе в программировании!')


@dp.message_handler(state=PSGroup.tell)
async def process_tell(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if data.get('tell') and data.get('last_tell'):
            data['tell'] += data['last_tell']
        data['tell'] = message.text if not data.get('tell') else data['tell'] + message.text
        text = data['tell']
    await continue_story(message, text, state)
    await PSGroup.tell.set()


@dp.message_handler(state=PSGroup.help_str)
async def process_help_str(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['help_str'] = message.text
        text = STR_HELP.get(data['help_str'], f'В Python нет метода "{message.text}".')
    await message.answer(text)
    await PSGroup.help_str.set()


@dp.message_handler(state=PSGroup.help_int)
async def process_help_int(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['help_int'] = message.text
        text = INT_HELP.get(data['help_int'], f'В Python нет метода "{message.text}".')
    await message.answer(text)
    await PSGroup.help_int.set()


@dp.message_handler(state=PSGroup.help_float)
async def process_help_float(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['help_float'] = message.text
        text = FLOAT_HELP.get(data['help_float'], f'В Python нет метода "{message.text}".')
    await message.answer(text)
    await PSGroup.help_float.set()


@dp.message_handler(state=PSGroup.help_list)
async def process_help_list(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['help_list'] = message.text
        text = LIST_HELP.get(data['help_list'], f'В Python нет метода "{message.text}".')
    await message.answer(text)
    await PSGroup.help_list.set()


@dp.message_handler(state=PSGroup.help_set)
async def process_help_set(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['help_set'] = message.text
        text = SET_HELP.get(data['help_set'], f'В Python нет метода "{message.text}".')
    await message.answer(text)
    await PSGroup.help_set.set()


@dp.message_handler(state=PSGroup.help_tuple)
async def process_help_tuple(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['help_tuple'] = message.text
        text = TUPLE_HELP.get(data['help_tuple'], f'В Python нет метода "{message.text}".')
    await message.answer(text)
    await PSGroup.help_tuple.set()


@dp.message_handler(state=PSGroup.help_dict)
async def process_help_dict(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['help_dict'] = message.text
        text = DICT_HELP.get(data['help_dict'], f'В Python нет метода "{message.text}".')
    await message.answer(text)
    await PSGroup.help_dict.set()


@dp.message_handler(state=PSGroup.help_byte)
async def process_help_byte(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['help_byte'] = message.text
        text = BYTE_HELP.get(data['help_byte'], f'В Python нет метода "{message.text}".')
    await message.answer(text)
    await PSGroup.help_byte.set()


@dp.message_handler(commands=['city'])
async def city_weather_handler(message: types.Message):
    city = message.text.split('/city')[1]
    weather = get_weather(city)
    logging.info(f'Пользователь запросил погоду')
    await message.answer(weather)


@dp.message_handler(commands=['codewars'])
async def kata_parser_handler(message: types.Message):
    url = message.text.split('/codewars')[1].strip()
    kata = Kata(url)
    response = kata.start_parser()
    logging.info(f'Пользователь запросил задачу с codewars')
    await message.answer(response)


@dp.message_handler(commands=['weather'])
async def weather_handler(message: types.Message):
    weather = get_weather()
    logging.info(f'Пользователь запросил погоду')
    await message.answer(weather)
    await message.delete()


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    user_fullname = message.from_user.full_name
    logging.info(f'{user_id}: {user_fullname} [{time.asctime()}]')

    await message.answer(f'Привет, {user_fullname.title()}')
    await bot.send_message(user_id, MESSAGE.format(user_name))


@dp.message_handler(commands=['egg'])
async def egg_battle(message: types.Message):
    if eggs:
        user_fullname = message.from_user.full_name
        sh(eggs)
        egg_pop = eggs.pop()
        egg_state = ['разбито', 'не треснуло']
        await message.answer(f'Христос Воскресе! {user_fullname}, из корзиночки ты берешь яйцо. Его цвет - {egg_pop}.')
        await message.answer(eggs_pictures.get(egg_pop))
        await message.answer(f'{egg_pop} - {eggs_dict.get(egg_pop)}')
        opp_egg_pop = ''
        if battle_eggs:
            opp_egg_pop = battle_eggs[0]
            await message.answer(f'Оппонент выбрал яйцо - {opp_egg_pop}')
            await message.answer(f'Ты будешь биться с ним!')
            await message.answer(eggs_pictures.get(opp_egg_pop))
            await message.answer(f'{opp_egg_pop} - {eggs_dict.get(opp_egg_pop)}')
        battle_eggs.append(egg_pop)
        if len(battle_eggs) == 2:
            await message.answer(f'Да начнется битва!')
            count_time = 10
            while count_time > 0:
                await message.answer(f'{count_time}..')
                time.sleep(1)
                count_time -= 1
            final_state = ch(egg_state)
            opp_final_state = ch(egg_state)
            final_states[egg_pop] = final_state
            final_states[opp_egg_pop] = opp_final_state
            if final_state == egg_state[1]:
                eggs.append(egg_pop)
                await message.answer(f'Яйцо цвета "{egg_pop}" возвращается в корзиночку!')
            if opp_final_state == egg_state[1]:
                eggs.append(opp_egg_pop)
                await message.answer(f'Яйцо цвета "{opp_egg_pop}" возвращается в корзиночку!')
            await message.answer(f'Итоги: ')
            await message.answer(f'Яйцо цвета "{egg_pop}" {final_state} в бою.')
            await message.answer(f'Яйцо цвета "{opp_egg_pop}" {opp_final_state} в бою.')
            await message.answer(f'В корзиночке осталось {len(eggs)} яиц :)')
            await message.answer(f'Если в корзиночке остались яйца, можете сыграть еще раз, набрав /egg! :)')
            battle_eggs.clear()
        if len(battle_eggs) == 1:
            await message.answer(f'Теперь пусть оппонент наберет /egg! Его битва будет с яйцом цвета "{egg_pop}" :)')
    else:
        await message.answer(f'В корзиночке не осталось яиц, давайте покрасим еще! :)')
    # await message.answer(f'Увы и ах, но пасха закончилась, теперь можно просто кушать яйца, это полезно :)')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
