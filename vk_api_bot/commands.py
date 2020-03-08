from random import randint

import vk_api.vk_api
from config import group_token

import feedparser


vkApi_token = vk_api.VkApi(token=group_token())
vkApi = vkApi_token.get_api()


def send_message(send_id, message):
    vkApi.messages.send(peer_id=send_id, message=message, random_id=randint(1, 999999999))


class TenJokes:
    def give_joke(self, joke_num=False):
        """
        Отдаёт одну из 10 "шуток дня по версии anekdot.ru".
        Если указать int (0-9), то отдаст шутку по номеру.
        Без параметра: отдаст случайную.

        Warning: чаще всего шутки крайней степени унылости.

        :param joke_num: int. 0-9, or it will be randint(0-9)
        :return: str: random 'fresh joke of the day' (one of 10 in collection)
        """
        if not joke_num:
            random_joke_num = randint(0, 9)
            return feedparser.parse("https://www.anekdot.ru/rss/export_j.xml")["entries"][random_joke_num]['summary']
        else:
            return feedparser.parse("https://www.anekdot.ru/rss/export_j.xml")["entries"][joke_num]['summary']

    # TODO: Добавить, чтобы вначале добавлял все анекдоты в список и при показе удалял отдельные.
    #  когда все анекдоты закончатся, спросить "по второму кругу?" (решение в добавлении копии списка и в возврате к ниму)
    def give_list(self):
        """
        Отдаёт все 10 "шуток дня по версии anekdot.ru" списком.
        :return: list
        """
        return [self.give_joke(i) for i in range(10)]


if __name__ == "__main__":
    # print(TenJokes().give_list())
    # give_a_joke()
    # print(give_a_joke())
