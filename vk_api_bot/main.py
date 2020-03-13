from commands import *
from config import main_group_id, admin_id

import time

from vk_api.bot_longpoll import VkBotLongPoll
from vk_api.bot_longpoll import VkBotEventType


LPS_params = {"vk": vkApi_token,
              "group_id": main_group_id(),
              "v": 5.103}

long_poll = VkBotLongPoll(LPS_params["vk"], group_id=LPS_params["group_id"], wait=25)


def received_message(message=""):
    """
    Проверяем полученное от long_poll.listen() VkBotEventType.MESSAGE_NEW на соответствие с параметром "message".

    :param message: str
    :return: True if received from user message is equal with param 'message'.
    If param field will empty, it'll return received message.
    """

    if message:
        if event.object.message["text"].upper() == message.upper():
            return True
        else:
            return False

    return event.object.message["text"]


class User:
    def __init__(self, peer_id):
        self.__peer_id = peer_id


if __name__ == "__main__":
    # При запуске получаем в ЛС от бота сообщение о запуске
    send_message(admin_id(), "Бот запущен")

    # TODO Добавляем в этот словарь event.object.message["peer_id"] в key и TenJokes().give_list() в value
    people_jokes_status = dict()

    # "Listening" for actions
    for event in long_poll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            # Any incoming message log
            if received_message():
                print("--------------------------------------------------")
                print(event, "\n", f"{event.object.message['from_id']}:", event.object.message["text"])

            # Ниже прописываем условия if, исходящие из полученного сообщения
            if received_message("exit()"):
                send_message(event.object.message["peer_id"], "Бот отключён")
                break

            if received_message("анекдот"):
                # if event.object.message["peer_id"] in people_jokes_status:
                #     send_message(event.object.message["peer_id"], TenJokes().give_joke())
                #     print("Анекдот показан")
                # else:
                #     pass
                      
                send_message(event.object.message["peer_id"], TenJokes().give_joke())
                print("Анекдот показан")
