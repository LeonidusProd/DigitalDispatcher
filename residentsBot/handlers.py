from aiogram import F, Router, Bot
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery, ContentType
from aiogram.fsm.context import FSMContext

import keyboards as kbs
import messages as msg
import backend_connection as bc
from utils import is_valid_integer

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await state.update_data(user_state='start')
    await message.answer(
        text=msg.START_MESSAGE,
        reply_markup=await kbs.start_keyboard()
    )
    await message.delete()


@router.callback_query(lambda query: query.data in ['send_req_first_step'])
async def send_req_first_step(callback: CallbackQuery, state: FSMContext):
    await state.update_data(user_state='send_first_step_menu')
    await callback.message.edit_text(
        text=msg.FIRST_STEP_MESSAGE,
        reply_markup=await kbs.request_first_step(state)
    )


@router.callback_query(lambda query: query.data in ['select_complex'])
async def select_complex(callback: CallbackQuery, state: FSMContext):
    await state.update_data(user_state='complex_selecting')
    await callback.message.edit_text(
        text=msg.SELECT_COMPLEX_MESSAGE,
        reply_markup=await kbs.complexes_list()
    )


@router.callback_query(F.data.startswith('complex_selected_'))
async def complex_selected(callback: CallbackQuery, state: FSMContext):
    await state.update_data(user_state='house_selecting')
    complex_id = callback.data.split('_')[-1]
    await state.update_data(selected_complex_id=int(complex_id))
    await callback.message.edit_text(
        text=msg.SELECT_HOUSE_MESSAGE,
        reply_markup=await kbs.houses_list(complex_id)
    )


@router.callback_query(F.data.startswith('house_selected_'))
async def house_selected(callback: CallbackQuery, state: FSMContext):
    await state.update_data(user_state='send_first_step_menu')
    address_id = callback.data.split('_')[-2]
    address_name = callback.data.split('_')[-1]
    await state.update_data(selected_address_id=int(address_id))
    await state.update_data(selected_address_name=str(address_name))
    await callback.message.edit_text(
        text=msg.FIRST_STEP_MESSAGE,
        reply_markup=await kbs.request_first_step(state)
    )


@router.callback_query(lambda query: query.data in ['input_apartment'])
async def input_apartment(callback: CallbackQuery, state: FSMContext):
    await state.update_data(user_state='input_apartment')
    await callback.message.edit_text(
        text=msg.INPUT_APARTMENT_MESSAGE
    )


@router.callback_query(lambda query: query.data in ['second_step'])
async def second_step(callback: CallbackQuery, state: FSMContext):
    await state.update_data(user_state='send_second_step_menu')
    await callback.message.edit_text(
        text=msg.SECOND_STEP_MESSAGE,
    )


@router.callback_query(lambda query: query.data in ['input_snp'])
async def input_snp(callback: CallbackQuery, state: FSMContext):
    await state.update_data(user_state='input_surname')
    await callback.message.edit_text(
        text=msg.INPUT_SURNAME_MESSAGE,
    )


@router.callback_query(lambda query: query.data in ['input_phone'])
async def input_snp(callback: CallbackQuery, state: FSMContext):
    await state.update_data(user_state='input_phone')
    await callback.message.answer(
        text=msg.INPUT_PHONE_MENU,
        reply_markup=await kbs.share_phone_number()
    )
    await callback.message.delete()


@router.callback_query(lambda query: query.data in ['save_request'])
async def save_request(callback: CallbackQuery, state: FSMContext, bot: Bot):
    await state.update_data(user_tg_id=callback.from_user.id)
    await bc.create_new_request(state=state, bot=bot)

    await state.clear()
    await state.update_data(user_state='start')

    await callback.message.answer(
        text=msg.REQUEST_SENDED_MESSAGE,
        reply_markup=await kbs.start_keyboard()
    )
    await callback.message.delete()


@router.callback_query(lambda query: query.data in ['user_requests'])
async def input_snp(callback: CallbackQuery, state: FSMContext):
    await state.update_data(user_state='user_requests')
    await callback.message.answer(
        text=await msg.user_requests_message(callback.from_user.id),
        reply_markup=await kbs.start_keyboard()
    )
    await callback.message.delete()


@router.message(lambda message: message.content_type in [ContentType.TEXT, ContentType.PHOTO])
async def union_text_handler(message: Message, state: FSMContext):
    try:
        curent_user_state = dict(await state.get_data())['user_state']

        match curent_user_state:
            case 'input_apartment':
                if is_valid_integer(message.text):
                    await state.update_data(user_state='send_first_step_menu')
                    await state.update_data(apartment_number=int(message.text))
                    await message.answer(
                        text=msg.FIRST_STEP_MESSAGE,
                        reply_markup=await kbs.request_first_step(state)
                    )
                    await message.delete()
                    await message.chat.delete_message(message.message_id - 1)
                else:
                    await message.edit_text(
                        text=msg.INCORRECT_APARTMENT_MESSAGE
                    )
                    await message.delete()
                    await message.chat.delete_message(message.message_id - 1)
            case 'send_second_step_menu':
                if message.photo:
                    if message.caption:
                        await state.update_data(request_reason=str(message.caption))
                        print(message.photo)
                        await state.update_data(request_photo=message.photo[-1].file_id)
                        await message.answer(
                            text=msg.THIRD_STEP_MESSAGE,
                            reply_markup=await kbs.request_third_step(state)
                        )
                        await message.delete()
                        await message.chat.delete_message(message.message_id - 1)
                    else:
                        await message.delete()
                else:
                    await state.update_data(request_reason=str(message.text))
                    await message.answer(
                        text=msg.THIRD_STEP_MESSAGE,
                        reply_markup=await kbs.request_third_step(state)
                    )
                    await message.delete()
                    await message.chat.delete_message(message.message_id - 1)
                await state.update_data(user_state='send_third_step_menu')
            case 'input_surname':
                await state.update_data(user_state='input_name')
                await state.update_data(resident_surname=str(message.text))
                await message.answer(
                    text=msg.INPUT_NAME_MESSAGE,
                )
                await message.delete()
                await message.chat.delete_message(message.message_id - 1)
            case 'input_name':
                await state.update_data(user_state='input_patronymic')
                await state.update_data(resident_name=str(message.text))
                await message.answer(
                    text=msg.INPUT_PATRONYMIC_MESSAGE,
                )
                await message.delete()
                await message.chat.delete_message(message.message_id - 1)
            case 'input_patronymic':
                await state.update_data(user_state='send_third_step_menu')
                if str(message.text) == '-':
                    if 'resident_patronymic' in dict(await state.get_data()):
                        await state.update_data(resident_patronymic='-')
                else:
                    await state.update_data(resident_patronymic=str(message.text))

                await message.answer(
                    text=msg.THIRD_STEP_MESSAGE,
                    reply_markup=await kbs.request_third_step(state)
                )
                await message.delete()
                await message.chat.delete_message(message.message_id - 1)
            case 'input_phone':
                await state.update_data(user_state='send_third_step_menu')
                await state.update_data(phone_number=str(message.text))
                await message.answer(
                    text=msg.THIRD_STEP_MESSAGE,
                    reply_markup=await kbs.request_third_step(state)
                )
                await message.delete()
                await message.chat.delete_message(message.message_id - 1)
    except KeyError:
        await cmd_start(message, state)


@router.message(lambda message: message.content_type == ContentType.CONTACT)
async def handle_contact(message: Message, state: FSMContext):
    await state.update_data(user_state='send_third_step_menu')
    await state.update_data(phone_number=message.contact.phone_number)
    await message.answer(
        text=msg.THIRD_STEP_MESSAGE,
        reply_markup=await kbs.request_third_step(state)
    )
    await message.delete()
    await message.chat.delete_message(message.message_id - 1)
