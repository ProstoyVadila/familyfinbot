from aiogram import types
from aiogram.dispatcher import FSMContext

from app import dp, bot
from config import ADMIN_ID
from utils.keyboards.inline.start_markups import back_to_menu_markup
from utils.messages import base
from models.states.finance_states import FeedbackState


@dp.message_handler(commands=['feedback'])
async def get_feedback(message: types.Message):
    await message.answer(base.FEEDBACK_MESSAGE)
    await FeedbackState.message.set()


@dp.message_handler(state=FeedbackState.message)
async def send_feedback(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['message'] = message.text

    message_to_admin = base.SEND_FEEDBACK_TO_ADMIN + data['message']

    await bot.send_message(
        ADMIN_ID,
        message_to_admin
    )
    await message.answer(
        base.THANKS_MESSAGE,
        reply_markup=back_to_menu_markup
    )
    await state.finish()
