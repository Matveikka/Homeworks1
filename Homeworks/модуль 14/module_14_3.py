import aiogram
from aiogram import Bot, dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
import products

api = ''
bot = aiogram.Bot(token=api)
dp = aiogram.Dispatcher(bot, storage=MemoryStorage())

kb1 = ReplyKeyboardMarkup()
button1 = KeyboardButton(text='Информация')
button2 = KeyboardButton(text='Рассчитать')
button3 = KeyboardButton(text='Купить')
kb1.row(button1, button2, button3)

kb2 = InlineKeyboardMarkup()
button1 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
button2 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
kb2.row(button1, button2)

kb3 = InlineKeyboardMarkup()
button1 = InlineKeyboardButton(text='Product1', callback_data='product_buying')
button2 = InlineKeyboardButton(text='Product2', callback_data='product_buying')
button3 = InlineKeyboardButton(text='Product3', callback_data='product_buying')
button4 = InlineKeyboardButton(text='Product4', callback_data='product_buying')
kb3.row(button1, button2, button3, button4)

start_menu = ReplyKeyboardMarkup(
     keyboard=[
         [KeyboardButton(text='Выберите опцию:')],
         [
             KeyboardButton(text='Рассчитать норму калорий', callback_data='calories'),
             KeyboardButton(text='Формулы расчёта', callback_data='formulas')
         ]
     ], resize_keyboard=True)
class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer("Привет! Я бот помогающий твоему здоровью."
                         " Для того чтобы вычислить суточную норму калорий используйте команду - 'Рассчитать'",
                         reply_markup=kb1)

@dp.message_handler(text=['Рассчитать'])
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=kb2)

@dp.message_handler(text=['Купить'])
async def get_buying_list(message):
    with open("files/1.jpg", "rb") as img1:
        await message.answer_photo(img1,
    f"Название: Product {products.Product1} | Описание: описание {products.Product1} | Цена: {products.Product1 * 100}")
    with open("files/2.jpg", "rb") as img2:
        await message.answer_photo(img2,
    f"Название: Product {products.Product2} | Описание: описание {products.Product2} | Цена: {products.Product2 * 100}")
    with open("files/3.jpg", "rb") as img3:
        await message.answer_photo(img3,
    f"Название: Product {products.Product3} | Описание: описание {products.Product3} | Цена: {products.Product3 * 100}")
    with open("files/4.jpg", "rb") as img4:
        await message.answer_photo(img4,
    f"Название: Product {products.Product4} | Описание: описание {products.Product4} | Цена: {products.Product4 * 100}")
    await message.answer("Выберите продукт для покупки: ", reply_markup=kb3)

@dp.callback_query_handler(text="product_buying")
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()

@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('Формула Миффлина-Сан Жеора: '
                                 '(10 * вес + 6.25 * рост - 5 * возраст + 5)')
    await call.answer()

@dp.callback_query_handler(text=['calories'])
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await call.answer()
    await UserState.age.set()

@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост (см):')
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    calories_man = int(10 * int(data['weight']) + 6.25 * int(data['growth']) - 5 * int(data['age']) + 5)
    await message.answer(f'Ваша норма калорий {calories_man} в день')
    await state.finish()

if __name__ == '__main__':
    aiogram.executor.start_polling(dp, skip_updates=True)


