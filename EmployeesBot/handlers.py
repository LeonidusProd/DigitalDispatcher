import os
from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery, FSInputFile

import keyboards as kbs
import messages as msg
import backend_connection as bc
from utils import ensure_download_directory

router = Router()
DOWNLOAD_DIR = './EmployeesBot/downloads'


@router.message(CommandStart())
async def cmd_start(message: Message):
    master_tasks = await bc.get_master_tasks(message.from_user.id)
    await message.answer(
        text=await msg.staff_tasks_message(master_tasks),
        reply_markup=await kbs.start_keyboard(master_tasks)
    )
    await message.delete()


@router.callback_query(F.data.startswith('open_task_'))
async def open_task(callback: CallbackQuery):
    task_info = await bc.get_task_info(callback.data.split('_')[-1])
    await callback.message.answer(
        text=await msg.task_info_message(task_info),
        reply_markup=await kbs.task_info_keyboard(task_info)
    )
    await callback.message.delete()


@router.callback_query(F.data.startswith('start_task_'))
async def start_task(callback: CallbackQuery):
    task_id = callback.data.split('_')[-1]
    await bc.start_task(task_id)
    await callback.answer('Выполнение задачи начато')
    task_info = await bc.get_task_info(task_id)
    await callback.message.edit_text(
        text=await msg.task_info_message(task_info),
        reply_markup=await kbs.task_info_keyboard(task_info)
    )


@router.callback_query(F.data.startswith('close_task_'))
async def close_task(callback: CallbackQuery):
    task_id = callback.data.split('_')[-1]
    await bc.close_task(task_id)
    await callback.answer('Выполнение задачи завершено')
    master_tasks = await bc.get_master_tasks(callback.from_user.id)
    await callback.message.edit_text(
        text=await msg.staff_tasks_message(master_tasks),
        reply_markup=await kbs.start_keyboard(master_tasks)
    )


@router.callback_query(F.data.startswith('my_tasks'))
async def my_tasks(callback: CallbackQuery):
    master_tasks = await bc.get_master_tasks(callback.from_user.id)
    await callback.message.answer(
        text=await msg.staff_tasks_message(master_tasks),
        reply_markup=await kbs.start_keyboard(master_tasks)
    )
    await callback.message.delete()


@router.callback_query(F.data.startswith('check_tasks'))
async def check_tasks(callback: CallbackQuery):
    master_tasks = await bc.get_master_tasks(callback.from_user.id)
    await callback.message.answer(
        text=await msg.staff_tasks_message(master_tasks),
        reply_markup=await kbs.start_keyboard(master_tasks)
    )
    await callback.message.delete()


@router.callback_query(F.data.startswith('open_request_'))
async def open_request(callback: CallbackQuery):
    request_id = callback.data.split('_')[-2]
    task_id = callback.data.split('_')[-1]
    request_info = await bc.get_request_info(request_id)
    await callback.answer('')

    if request_info['photo'] is None:
        await callback.message.answer(
            text=await msg.request_info_message(request_info),
            reply_markup=await kbs.request_info_keyboard(task_id)
        )
    else:
        ensure_download_directory(DOWNLOAD_DIR)
        local_photo_path = str(await bc.download_photo(request_info['photo'], DOWNLOAD_DIR))

        await callback.message.answer_photo(
            photo=FSInputFile(local_photo_path),
            caption=await msg.request_info_message(request_info),
            reply_markup=await kbs.request_info_keyboard(task_id)
        )

        os.remove(local_photo_path)

    await callback.message.delete()
