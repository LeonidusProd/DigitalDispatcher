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
                return dict(await response.json())['residentBotToken']
    except aiohttp.ClientError as e:
        print(f"Backend conection error: {e}. Source: get_bot_token")


@authorization(BASE_URL)
async def get_complexes_list(token):
    headers = {
        'Authorization': f'Token {token}',
    }

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(
                    url=f'{BASE_URL}/api/v1/complex/',
                    headers=headers
            ) as response:
                return list(await response.json())
    except aiohttp.ClientError as e:
        print(f"Backend conection error: {e}. Source: get_complexes_list")


@authorization(BASE_URL)
async def get_houses_list(token, complex_id):
    headers = {
        'Authorization': f'Token {token}',
    }

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(
                    url=f'{BASE_URL}/api/v1/complex/{complex_id}/houses',
                    headers=headers
            ) as response:
                print(list(await response.json()))
                return list(await response.json())
    except aiohttp.ClientError as e:
        print(f"Backend conection error: {e}. Source: get_houses_list")


async def check_user_exists(token, user_id):
    headers = {
        'Authorization': f'Token {token}',
    }

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(
                    url=f'{BASE_URL}/api/v1/resident/by_tgid/{user_id}',
                    headers=headers
            ) as response:
                resp = dict(await response.json())
                if resp['exists']:
                    return True, dict(resp['resident'])['pk']
                else:
                    return False, -1
    except aiohttp.ClientError as e:
        print(f"Backend conection error: {e}. Source: check_user_exists")


async def get_or_create_resident(token, state):
    headers = {
        'Authorization': f'Token {token}',
    }

    user_data = dict(await state.get_data())

    check, resident_id = await check_user_exists(token, user_data['user_tg_id'])

    if check:
        return resident_id
    else:
        try:
            data = {
                'name': user_data['resident_name'],
                'surname': user_data['resident_surname'],
                'phone': user_data['phone_number'],
                'tg_id': user_data['user_tg_id']
            }

            if 'resident_patronymic' in user_data and user_data['resident_patronymic'] is not '-':
                data['patronymic'] = user_data['resident_patronymic']

            async with aiohttp.ClientSession() as session:
                async with session.post(
                        url=f'{BASE_URL}/api/v1/resident/create/',
                        headers=headers,
                        data=data
                ) as response:
                    return dict(await response.json())['pk']
        except aiohttp.ClientError as e:
            print(f"Backend conection error: {e}. Source: get_or_create_resident")


@authorization(BASE_URL)
async def create_new_request(token, state, bot):
    headers = {
        'Authorization': f'Token {token}'
    }

    user_data = dict(await state.get_data())

    form = aiohttp.FormData()
    form.add_field('text', str(user_data['request_reason']))
    form.add_field('status', '1')
    form.add_field('resident', str(await get_or_create_resident(token, state)))
    form.add_field('address', str(user_data['selected_address_id']))

    if 'apartment_number' in user_data:
        form.add_field('apartment', str(user_data['apartment_number']))

    if 'request_photo' in user_data:
        file = await bot.get_file(user_data['request_photo'])
        photo = await bot.download_file(file.file_path)

        form.add_field('photo',
                       photo,
                       filename='request_photo.jpg',
                       content_type='image/jpeg')

    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(
                    url=f'{BASE_URL}/api/v1/request/create/',
                    headers=headers,
                    data=form
            ) as response:
                return await response.json()
    except aiohttp.ClientError as e:
        print(f"Backend conection error: {e}. Source: create_new_request")


@authorization(BASE_URL)
async def get_user_requests(token, user_id):
    headers = {
        'Authorization': f'Token {token}',
    }

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(
                    url=f'{BASE_URL}/api/v1/requests/from-user/{user_id}',
                    headers=headers
            ) as response:
                return list(await response.json())
    except aiohttp.ClientError as e:
        print(f"Backend conection error: {e}. Source: get_user_requests")
