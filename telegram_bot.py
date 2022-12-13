import config
import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.message import ContentType

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

PRICE = types.LabeledPrice(label='Подписка на 1 месяц', amount=1 * 100)


@dp.message_handler(commands=['buy'])
async def buy(message: types.Message):
    if config.PAYMENT_TOKEN.split(':')[1] == 'TEST':
        await bot.send_message(message.chat.id, 'Тестовый платёж!!!')
    await bot.send_invoice(message.chat.id,
                           title='Подписка на бота',
                           description='Активация подписки на бота на 1 месяц',
                           provider_token=config.PAYMENT_TOKEN,
                           currency='rub',
                           photo_url='')


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=False)
