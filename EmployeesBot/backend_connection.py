import os
import aiohttp

from decorators import authorization


BASE_URL = str(os.environ.get(
    "BASE_URL",
    default='http://127.0.0.1:8000'
))


@authorization(BASE_URL)
async def get_bot_token(token):
    headers = {
        'Authorization': f'Token {token}',
    }

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(
                    url=f'{BASE_URL}/api/v1/bottokens/manage/1',
                    headers=headers
            ) as response:
                return dict(await response.json())['staffBotToken']
    except aiohttp.ClientError as e:
        print(f"Backend conection error: {e}. Source: get_bot_token")


@authorization(BASE_URL)
async def get_master_tasks(token, user_id):
    headers = {
        'Authorization': f'Token {token}',
    }

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(
                    url=f'{BASE_URL}/api/v1/tasks/for-master/{user_id}',
                    headers=headers
            ) as response:
                return list(await response.json())
    except aiohttp.ClientError as e:
        print(f"Backend conection error: {e}. Source: get_master_tasks")


@authorization(BASE_URL)
async def get_task_info(token, task_id):
    headers = {
        'Authorization': f'Token {token}',
    }

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(
                    url=f'{BASE_URL}/api/v1/task/{task_id}',
                    headers=headers
            ) as response:
                return dict(await response.json())
    except aiohttp.ClientError as e:
        print(f"Backend conection error: {e}. Source: get_task_info")


@authorization(BASE_URL)
async def start_task(token, task_id):
    headers = {
        'Authorization': f'Token {token}',
    }

    data = {
        'status': 2
    }

    try:
        async with aiohttp.ClientSession() as session:
            async with session.patch(
                    url=f'{BASE_URL}/api/v1/task/{task_id}',
                    data=data,
                    headers=headers
            ) as response:
                return dict(await response.json())
    except aiohttp.ClientError as e:
        print(f"Backend conection error: {e}. Source: start_task")


@authorization(BASE_URL)
async def close_task(token, task_id):
    headers = {
        'Authorization': f'Token {token}',
    }

    data = {
        'status': 4
    }

    try:
        async with aiohttp.ClientSession() as session:
            async with session.patch(
                    url=f'{BASE_URL}/api/v1/task/{task_id}',
                    data=data,
                    headers=headers
            ) as response:
                return dict(await response.json())
    except aiohttp.ClientError as e:
        print(f"Backend conection error: {e}. Source: close_task")


@authorization(BASE_URL)
async def get_request_info(token, request_id):
    headers = {
        'Authorization': f'Token {token}',
    }

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(
                    url=f'{BASE_URL}/api/v1/request/{request_id}',
                    headers=headers
            ) as response:
                return dict(await response.json())
    except aiohttp.ClientError as e:
        print(f"Backend conection error: {e}. Source: get_request_info")


async def download_photo(url: str, dest_folder: str) -> str:
    filename = os.path.basename(url)
    file_path = os.path.join(dest_folder, filename)

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    with open(file_path, 'wb') as f:
                        f.write(await response.read())

        return file_path.replace('\\', '/')
    except aiohttp.ClientError as e:
        print(f"Backend conection error: {e}. Source: download_photo")
