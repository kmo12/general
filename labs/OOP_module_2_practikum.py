# Создайте класс User и его наследника SuperUser, которые описывают пользователя и супер-пользователя
#
# В классе User необходимо описать:
#
# Конструктор, который принимает в качестве параметров значение для атрибутов name, login, password X
# Свойства для изменения и получения значений атрибутов X
# Метод show_info, который печатает в произвольной форме значения атрибутов name и login X
# Атрибут класса count для хранения количества созданных экземпляров класса User X
#
#
# Необходимое условия, которые надо учесть:
#
# После создания объекта:
#  Атрибут name доступен и для чтения, и для изменения X
#  Атрибут login доступен только для чтения X
#  Атрибут password доступен только для изменения. Для чтения выводит звёздочки X
#
# В классе SuperUser необходимо описать:
#
# Конструктор, который принимает в качестве параметров значение для атрибутов name, login, password, role X
# Свойство для изменения и получения значения атрибута role X
# Метод show_info, который печатает в произвольном формате значения атрибутов name, login и role X
# Атрибут класса count для хранения количества созданных экземпляров класса SuperUser X
#
#
# Дополнительно:
# Переназначить __lt__ и __gt__, чтобы можно было сравнить "уровень прав" пользователней ~!~


# Как должно работать:
#     user1 = User("Paul McCartney", "paul", "1234") X
#     user2 = User("George Harrison", "george", "5678") X
#     user3 = User("Richard Starkey", "ringo", "8523") X
#     admin = SuperUser("John Lennon", "john", "0000", "admin") X
#
#     user1.show_info()  # Например: Name: Paul McCartney, Login: paul X
#     admin.show_info()  # Например: Name: John Lennon, Login: john, Role: admin X
#
#     users = User.counter
#     admins = SuperUser.counter
#
#     print(f"Всего обычных пользователей: {users}")  # Всего обычных пользователей: 3
#     print(f"Всего супер-пользователей: {admins}")  # Всего супер-пользователей: 1
#
#     user3.name = "Ringo Star"
#     print(user3.name)  # Ringo Star
#
#     print(user2.login)  # george
#     user2.login = "geo"  # Ошибка
#
#     user1.password = "Pa$$w0rd"
#     print(user2.password)  # Ошибка


class User:
    counter = 0

    def __init__(self, name, login, password):
        self.__name = name
        self.__login = login
        self.__password = password
        User.counter += 1

    # getter name
    @property
    def name(self):
        return self.__name

    # setter name
    @name.setter
    def name(self, name):
        self.__name = name

    # getter login
    @property
    def login(self):
        return self.__login

    # getter password
    @property
    def password(self):
        return "*" * len(self.__password)

    # setter password
    @password.setter
    def password(self, password):
        self.__password = password

    def show_info(self):
        return f"Name: {self.name}, Login: {self.login}"


class SuperUser(User):
    counter = 0

    def __init__(self, name, login, password, role):
        super().__init__(name, login, password)
        self.__role = role
        SuperUser.counter += 1
        User.counter -= 1

    # getter role
    @property
    def role(self):
        return self.__role

    # setter role
    @role.setter
    def role(self, role):
        self.__role = role

    def show_info(self):
        user_name_login = super().show_info()
        return f"{user_name_login}, Role: {self.role}"


if __name__ == "__main__":
    user1 = User("Paul McCartney", "paul", "1234")
    user2 = User("George Harrison", "george", "5678")
    user3 = User("Richard Starkey", "ringo", "8523")
    admin = SuperUser("John Lennon", "john", "0000", "admin")

    users = User.counter
    admins = SuperUser.counter