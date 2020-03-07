from random import randint

import vk_api.vk_api
from config import group_token

import feedparser


vkApi_token = vk_api.VkApi(token=group_token())
vkApi = vkApi_token.get_api()


def send_message(send_id, message):
    vkApi.messages.send(peer_id=send_id, message=message, random_id=randint(1, 999999999))


def random_joke(random_item=0):
    """
    :param random_item: int 0-9, or it will be randint(0-9)
    :return: random 'fresh joke of the day' (one of 10 in collection)
    """
    random_item = randint(0, 9)
    return feedparser.parse("https://www.anekdot.ru/rss/export_j.xml")["entries"][random_item]['summary']
    # TODO: Добавить, чтобы вначале добавлял все анекдоты в список и при показе удалял отдельные.
    #  когда все анекдоты закончатся, спросить "по второму кругу?" (решение в добавлении копии списка и в возврате к ниму)


if __name__ == "__main__":
    print(random_joke())
