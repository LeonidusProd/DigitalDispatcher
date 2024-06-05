async def staff_tasks_message(master_tasks):
    if len(master_tasks) == 0:
        return "У вас нет задач."
    else:
        message = "Ваши задачи:\n"
        i = 1
        for task in master_tasks:
            message += (f"{i}. {task['status']} задача:\n"
                        f"{task['task']}.\n\n")
            i += 1

        return message


async def task_info_message(task_info):
    return (f"{task_info['status_name']} задача: \n"
            f"{task_info['task']}\n"
            f"Описание: {task_info['task_description']}")


async def request_info_message(request_info):
    return (f"Сообщение от жителя:\n"
            f"{request_info['info']}\n\n"
            f"Дата: {request_info['date']}\n"
            f"Житель: {request_info['resident']}\n"
            f"ЖК: {request_info['complex']}\n"
            f"Адрес: {request_info['address']}\n")
