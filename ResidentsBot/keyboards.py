from aiogram.types import InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

import backend_connection as bc
from utils import shorten_name


async def start_keyboard():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text='Отправить заявку', callback_data='send_req_first_step'))
    keyboard.add(InlineKeyboardButton(text='Мои заявки', callback_data='user_requests'))
    return keyboard.as_markup()


async def request_first_step(state):
    user_data = dict(await state.get_data())
    selected_address = None
    entered_apartment = None

    if 'selected_address_name' in user_data:
        selected_address = user_data['selected_address_name']
    if 'apartment_number' in user_data:
        entered_apartment = user_data['apartment_number']

    if selected_address:
        address_select_btn_text = f'Адрес: {selected_address}. Изменить.'
    else:
        address_select_btn_text = 'Выбрать адрес'

    if entered_apartment:
        entered_apartment_btn_text = f'Квартира: {entered_apartment}. Изменить.'
    else:
        entered_apartment_btn_text = 'Указать квартиру'

    keyboard = InlineKeyboardBuilder()
    keyboard.row(InlineKeyboardButton(text=address_select_btn_text, callback_data='select_complex'))
    keyboard.row(InlineKeyboardButton(text=entered_apartment_btn_text, callback_data='input_apartment'))
    if selected_address is not None:
        keyboard.row(InlineKeyboardButton(text='Следующий шаг', callback_data='second_step'))
    return keyboard.as_markup()


async def complexes_list():
    keyboard = InlineKeyboardBuilder()
    all_complexes = await bc.get_complexes_list()

    for complex_el in all_complexes:
        keyboard.row(
            InlineKeyboardButton(text=complex_el['name'], callback_data=f'complex_selected_{complex_el['pk']}')
        )
    return keyboard.as_markup()


async def houses_list(complex_id):
    keyboard = InlineKeyboardBuilder()
    all_houses = await bc.get_houses_list(complex_id)

    for house_el in all_houses:
        max_l = 30
        short_name = shorten_name(house_el['name'], max_length=max_l)
        callback_data = f'house_selected_{house_el['pk']}_{short_name}'

        while len(callback_data.encode('utf-8')) > 64:
            max_l -= 1
            short_name = shorten_name(house_el['name'], max_length=max_l)
            callback_data = f'house_selected_{house_el['pk']}_{short_name}'

        keyboard.row(
            InlineKeyboardButton(text=house_el['name'],
                                 callback_data=callback_data)
        )
    return keyboard.as_markup()


async def request_third_step(state):
    user_data = dict(await state.get_data())
    entered_snp = None
    entered_phone = None

    if 'resident_name' in user_data:
        if 'resident_patronymic' in user_data and user_data['resident_patronymic'] is not '-':
            patronymic = f' {user_data['resident_patronymic']}'
        else:
            patronymic = ''

        entered_snp = f'{user_data['resident_surname']} {user_data['resident_name']}{patronymic}'
    if 'phone_number' in user_data:
        entered_phone = user_data['phone_number']

    if entered_snp:
        entered_snp_btn_text = f'ФИО: {entered_snp}. Изменить.'
    else:
        entered_snp_btn_text = 'Ввести ФИО'

    if entered_phone:
        entered_phone_btn_text = f'Номер телефона: {entered_phone}. Изменить.'
    else:
        entered_phone_btn_text = 'Указать номер телефона'

    keyboard = InlineKeyboardBuilder()
    keyboard.row(InlineKeyboardButton(text=entered_snp_btn_text, callback_data='input_snp'))
    keyboard.row(InlineKeyboardButton(text=entered_phone_btn_text, callback_data='input_phone'))
    if entered_snp is not None and entered_phone is not None:
        keyboard.row(InlineKeyboardButton(text='Сохранить заявку', callback_data='save_request'))
    return keyboard.as_markup()


async def share_phone_number():
    request_phone_keyboard = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text='Отправить номер телефона', request_contact=True)]],
        resize_keyboard=True
    )
    return request_phone_keyboard
