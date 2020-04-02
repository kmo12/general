from random import randint, choice

import vk_api.vk_api
from vk_api_bot.config import group_token

import feedparser

vkApi = vk_api.VkApi(token=group_token())
vkApi_get_api = vkApi.get_api()


def send_message(send_id, message):
    vkApi_get_api.messages.send(peer_id=send_id, message=message, random_id=randint(1, 999999999))


class GetUserInfo:
    def __init__(self, user_id: int):
        self._user_id = user_id

    case_dict = {"именительный": "nom",
                 "родительный": "gen",
                 "дательный": "dat",
                 "винительный": "acc",
                 "творительный": "ins",
                 "предложный": "abl"}

    def general_info(self, case="") -> dict:
        if case:
            return vkApi.method("users.get", {"user_ids": self._user_id,
                                              "fields": "sex",
                                              "name_case": self.case_dict[case]})[0]
        # VKApi пришлёт именительный падеж, если не пришло условия для другого
        return vkApi.method("users.get", {"user_ids": self._user_id, "fields": "sex"})[0]

    def __repr__(self):
        return str(self.general_info())

    def name(self, case="") -> str:
        return self.general_info(case)['first_name']

    def last_name(self, case="") -> str:
        return self.general_info(case)['last_name']

    def fullname(self, case="") -> str:
        return self.last_name(case) + self.name(case)

    def sex(self) -> int:
        """
        Отдаёт:
        1 — женский;
        2 — мужской;
        0 — пол не указан.
        """
        return self.general_info()['sex']


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
    #  когда все анекдоты закончатся, спросить "по второму кругу?" (решение в добавлении копии списка и в возврате к нему)
    @classmethod
    def give_list(cls):
        """
        Отдаёт все 10 "шуток дня по версии anekdot.ru" списком.
        :return: list
        """
        return [cls.give_joke(i) for i in range(10)]


# TODO чтобы сделать "добрый ДЕНЬ/ВЕЧЕР/УТРО" можно написать такую функцию:
# import time
# mytime = time.localtime()
# myhour = mytime.tm_hour
# if myhour == 0:
#     print('It is midnight') полночь
# elif myhour < 12:
#     print ('It is AM') утро
# elif myhour == 12:
#     print('It is noon') полдень
# else:
#     print ('It is PM') день

def hello(dialog_id, name=""):
    if name:
        answer_variables = [f"Привет, {name}!",
                            f"{name} здравствуй.",
                            f"{name}, здравствуйте.",
                            f"Здравствуйте, {name}."]
    else:
        answer_variables = ["Привет!"]
    send_message(dialog_id, choice(answer_variables))

    
if __name__ == "__main__":
    pass
