from vk_api_bot.commands import *
from vk_api_bot.config import main_group_id, admin_id

from vk_api.bot_longpoll import VkBotLongPoll
from vk_api.bot_longpoll import VkBotEventType


###########
# После добавления бота в конфу,
# не забыть дать боту доступ ко всей переписке,
# иначе он не будет видеть сообщения
###########


LPS_params = {"vk": vkApi,
              "group_id": main_group_id(),
              "v": 5.103}

long_poll = VkBotLongPoll(LPS_params["vk"], group_id=LPS_params["group_id"], wait=25)


def received_message(message=""):
    """
    Проверяем полученное от long_poll.listen() VkBotEventType.MESSAGE_NEW на соответствие с параметром "message".

    :param message: str
    :return: True if received from user message is equal with param 'message'.
    If param field will be empty, it'll return received message.
    """

    if message:
        if event.object.message["text"].replace(',', '').upper() == message.upper():
            return True
        else:
            return False

    return event.object.message["text"]


class User:
    """
    При получении сообщения бот должен проверять, есть ли экземпляр класса с таким id или его нужно создать.
    Если такой экземпляр есть, то выполняет через него функции в соответсвии с пришедшим сообщением.

    У класса User может быть classmethod, который отвечает за проверку, создан ли экземпляр класса с пришедшим id или нет.
    
    """
    def __init__(self, from_id: int, user_name: str):
        self.__from_id = from_id
        self.__user_name = user_name
        # Подготавливаем список для дальнейшего добавления в него все 10 анекдотов (TenJokes.give_list())
        self.personal_jokes_list = None
        # Добавляем новый from_id в список и нового пользователя в общий список
        self.identified_users_id.append(self.__from_id)
        self.identified_users[f"{from_id}"] = self

    @property
    def from_id(self) -> int:
        return self.__from_id

    @property
    def user_name(self) -> str:
        return self.__user_name

    # Лист со всеми идентифицированными from_id
    identified_users_id = []

    # Все созданные пользователи
    identified_users = {}

    def class_for_ten_jokes(self):
        pass


def is_admin(received_from_id: int) -> bool:
    return str(received_from_id) == admin_id()


# Режим отладки
starting_vk_bot = True

if __name__ == "__main__":
    # При запуске получаем в ЛС от бота сообщение о запуске
    send_message(admin_id(), "Бот запущен")
    print("Бот запущен")

    # "Listening" for actions
    if starting_vk_bot:  # Для режима отладки
        for event in long_poll.listen():
            if event.object.message is not None:
                # Сюда добавлять переменные, связанные с получаемыми данными
                received_user_personal_id = event.object.message["from_id"]

                received_dialog_id = event.object.message["peer_id"]

                received_message_text = event.object.message["text"]

                GetUserInfo_ = GetUserInfo(received_user_personal_id)
                #
                user_by_personal_id = User.identified_users.get(f"{received_user_personal_id}")

            if event.type == VkBotEventType.MESSAGE_NEW:
                if received_message():
                    # Logging any incoming message
                    print("--------------------------------------------------")
                    print(event, "\n",
                          f"Новое сообщение (от {received_user_personal_id}):", received_message_text)

                # Проверка: есть ли такой пользователь в базе, если нет, то создаём нового
                if received_user_personal_id not in User.identified_users_id:
                    User(received_user_personal_id, GetUserInfo_.name("именительный"))
                    print(f"Новый пользователь ({received_user_personal_id}, {GetUserInfo_.name}) добавлен")

                    # print(f"{User.identified_users_id=}\n{User.identified_users=}")

                # Ниже прописываем условия if, исходящие из полученного сообщения

                if received_message("exit()") and is_admin(received_user_personal_id):
                    send_message(admin_id(), "Бот отключён")
                    print("Бот отключён")
                    break

                if received_message("привет бот") or received_message("бот привет"):
                    hello(received_dialog_id, GetUserInfo_.name())
                    print("Приветствие отправлено")

                if received_message("анекдот"):
                    send_message(received_dialog_id, TenJokes().give_joke())
                    print("Анекдот показан")
