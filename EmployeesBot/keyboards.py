from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


async def start_keyboard(master_tasks):
    keyboard = InlineKeyboardBuilder()

    if len(master_tasks) == 0:
        keyboard.row(InlineKeyboardButton(text='Проверить наличие задач', callback_data='check_tasks'))
    else:
        i = 1
        for task in master_tasks:
            keyboard.row(InlineKeyboardButton(text=f'Открыть задачу {i}', callback_data=f'open_task_{task['pk']}'))
            i += 1

    return keyboard.as_markup()


async def task_info_keyboard(task_info):
    keyboard = InlineKeyboardBuilder()

    if task_info['status'] == 1:
        keyboard.row(InlineKeyboardButton(text='Начать выполнение', callback_data=f'start_task_{task_info['pk']}'))
    else:
        keyboard.row(InlineKeyboardButton(text='Завершить задачу', callback_data=f'close_task_{task_info['pk']}'))

    keyboard.row(InlineKeyboardButton(
        text='Посмотреть заявку',
        callback_data=f'open_request_{task_info['request']}_{task_info['pk']}')
    )
    keyboard.row(InlineKeyboardButton(text='Назад к списку задач', callback_data='my_tasks'))

    return keyboard.as_markup()


async def request_info_keyboard(task_info):
    keyboard = InlineKeyboardBuilder()

    keyboard.row(InlineKeyboardButton(text='Назад к задаче', callback_data=f'open_task_{task_info}'))

    return keyboard.as_markup()
