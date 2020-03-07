from commands import *

import time

# import vk_api.vk_api

from vk_api.bot_longpoll import VkBotLongPoll
from vk_api.bot_longpoll import VkBotEventType


LPS_params = {"vk": vkApi_token,
              "group_id": 188524220,
              "v": 5.103}

long_poll = VkBotLongPoll(LPS_params["vk"], group_id=LPS_params["group_id"], wait=25)


def received_message(message=""):
    """
    :param message: str
    :return: True if received from user message is equal with param 'message'
    or return just received from user message
    """

    if message:
        if event.object.message["text"] == message:
            return True
        else:
            return False

    return event.object.message["text"]


# Перезагрузить скрипт и сообщение отправится в конфу Quadro
# send_message(47289987, "Сообщение")

#  "Listening" for actions
if __name__ == "__main__":
    for event in long_poll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            if received_message():
                print(event, "\n", f"{event.object.message['from_id']}:", event.object.message["text"])

            if received_message("Анекдот") or received_message("анекдот"):
                send_message(event.object.message["peer_id"], random_joke())
                print("Анекдот показан")
                continue
