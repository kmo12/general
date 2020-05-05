class Node:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    def get_data(self):
        return self.__data

    def get_next(self):
        return self.__next

    def set_data(self, data):
        self.__data = data

    def set_next(self, next):
        self.__next = next


class LinkedList:
    #   add(item) - in head
    #   append(item) - in last
    #   is_empty() - True if have no nodes
    #   print(list) - [node, node, node]
    #   size() - num of nodes
    #   remove(item) - search for item and kill it, w/ changing links
    #   search(item) - True if item in nodes
    #   index(int) - show node's data with this index
    #   insert(pos, item) - insert item in pos w/ changing links
    #   pop() - remove last node and show data
    #   pop(pos) - remove node on pos and show data
    def __init__(self):
        self.__head = None
        self.__tail = None  # Last item in list

    def get_tail(self):
        return self.__tail

    def add(self, item):
        node = Node(item)
        if self.__head is not None:
            node.set_next(self.__head)
            self.__head = node
        else:
            self.__head = node
            self.__tail = node

    def is_empty(self):
        return self.__head is None

    def size(self):
        current = self.__head
        counter = 1
        while current.get_next() is not None:
            current = current.get_next()
            counter += 1
        return counter

    def search(self, item):
        if self.__head.get_data() == item:
            return True
        current = self.__head
        while current.get_next() is not None:
            current = current.get_next()
            if current.get_data() == item:
                return True
        return False

    def remove(self, item):
        if not self.search(item):
            raise Exception("Элемент не найден")
        current = self.__head
        prev = None
        if self.__head.get_data() == item:
            # Удаляем первый элемент
            if self.__head.get_next() is not None:
                self.__head = self.__head.get_next()
            else:
                self.__head = None
        while current.get_next() is not None:
            prev = current
            current = current.get_next()
            if current == self.__tail:
                pass
            if current.get_data() == item:
                prev.set_next(current.get_next())
                self.__tail = prev
                break

    def index(self, pos):
        current = self.__head
        index_counter = 0
        while index_counter < pos:
            if current.get_next() is not None:
                current = current.get_next()
            else:
                return "Out of index!"
            index_counter += 1
        return current.get_data()

    def pop(self, position=None):
        if position:
            pop_data = self.index(position)
            self.remove(self.index(position))
        else:
            pop_data = self.__tail.get_data()
            self.remove(self.__tail.get_data())
        return pop_data

    def insert(self, pos: int, item):
        if pos == 0:
            self.add(item)
            return True
        current = self.__head
        prev = None
        index_counter = 0
        while index_counter < pos:
            if current.get_next() is not None:
                prev = current
                current = current.get_next()
                index_counter += 1
            else:
                node = Node(item)
                current.set_next(node)
                node.set_next(None)
                self.__tail = node
                return True
        node = Node(item)
        prev.set_next(node)
        node.set_next(current)

    def append(self, item):
        node = Node(item)
        self.__tail.set_next(node)
        self.__tail = node

    def __str__(self):
        current = self.__head
        if current is None:
            return "[]"
        else:
            main = "[" + str(current.get_data())
            while current.get_next() is not None:
                current = current.get_next()
                main += ", " + str(current.get_data())
            return main + "]"


def linked_list_testing():
    my_list = LinkedList()

    my_list.add("Ы")
    my_list.add("Keke")
    my_list.add("Lolol")
    my_list.add("Lo234")
    my_list.add(141)

    print("my_list: ", my_list)
    print("tail: ", my_list.get_tail().get_data())

    print("******************")
    my_list.insert(99, "Inserted")
    print("my_list: ", my_list)
    print("tail: ", my_list.get_tail().get_data())

    print("******************")
    print("pop(): ", my_list.pop())
    print("my_list: ", my_list)
    print("tail: ", my_list.get_tail().get_data())

    print("******************")
    my_list.remove("Ы")
    print("my_list: ", my_list)
    print("tail: ", my_list.get_tail().get_data())

    print("******************")
    my_list.append(123124)
    print("my_list: ", my_list)
    print("tail: ", my_list.get_tail().get_data())


class Stack:
    # push(item)
    # pop()
    # peek()
    # is_empty()
    # size()
    def __init__(self):
        self.__data = list()

    def last_element(self):
        return self.__data[-1]

    def push(self, item):
        self.__data.append(item)

    def pop(self):
        if len(self.__data) > 0:
            return self.__data.pop()
        return None

    def peek(self):
        if len(self.__data) > 0:
            return f"{self.last_element()}"
        return None

    def is_empty(self):
        return len(self.__data) == 0

    def size(self):
        return len(self.__data)


def stack_testing():
    stack = Stack()

    stack.push(123)
    stack.push("0001")
    stack.push("hello")

    print(stack.peek())

    print(stack.pop())

    print(stack.is_empty())
    print(stack.size())


def all_brackets_checking(s: str) -> str:
    """
    Для работы функции необходимо наличие класса Stack
    """
    # ()
    brackets_stack = Stack()
    # {}
    curve_stack = Stack()
    # []
    sq_brackets_stack = Stack()
    # <>
    quot_stack = Stack()

    s.replace(" ", "")

    for element in s:
        # ()
        if element == "(" or element == ")":
            if element == "(":
                brackets_stack.push(1)
            elif element == ")":
                if brackets_stack.is_empty():
                    return "'(' is missing."
                brackets_stack.pop()

        # {}
        if element == "{" or element == "}":
            if element == "{":
                curve_stack.push(1)
            elif element == "}":
                if curve_stack.is_empty():
                    return "'{' is missing."
                curve_stack.pop()

        # []
        if element == "[" or element == "]":
            if element == "[":
                sq_brackets_stack.push(1)
            elif element == "]":
                if sq_brackets_stack.is_empty():
                    return "'[' is missing."
                sq_brackets_stack.pop()

        # <>
        if element == "<" or element == ">":
            if element == "<":
                quot_stack.push(1)
            elif element == ">":
                if quot_stack.is_empty():
                    return "'<' is missing."
                quot_stack.pop()

    final_decision = ""

    if not brackets_stack.is_empty():
        final_decision += "Troubles with '()'\n"

    if not curve_stack.is_empty():
        final_decision += "Troubles with '{}'\n"

    if not sq_brackets_stack.is_empty():
        final_decision += "Troubles with '[]'\n"

    if not quot_stack.is_empty():
        final_decision += "Troubles with '<>'\n"

    if not final_decision:
        final_decision = "No troubles were found"

    return final_decision


def all_brackets_checking_testing():
    print(all_brackets_checking("""
                for element in s:
            # ()
            if element == "(" or element == ")":
                if element == "(":
                    brackets_stack.push(1)
                elif element == ")":
                    if brackets_stack.is_empty():
                        return "'(' is missing."
                    brackets_stack.pop()
    
            # {}
            if element == "{" or element == "}":
                if element == "{":
                    curve_stack.push(1)
                elif element == "}":
                    if curve_stack.is_empty():
                        return "'{' is missing."
                    curve_stack.pop()
    
            # []
            if element == "[" or element == "]":
                if element == "[":
                    sq_brackets_stack.push(1)
                elif element == "]":
                    if sq_brackets_stack.is_empty():
                        return "'[' is missing."
                    sq_brackets_stack.pop()
    
            # <>
            if element == "<" or element == ">":
                if element == "<":
                    quot_stack.push(1)
                elif element == ">":
                    if quot_stack.is_empty():
                        return "'<' is missing.
                        
                        *********>********
                        
                        "
                    quot_stack.pop()
    
        final_decision = ""
    
        if not brackets_stack.is_empty():
            final_decision += "Troubles with '()'\n"
    
        if not curve_stack.is_empty():
            final_decision += "Troubles with '{}'\n"
    
        if not sq_brackets_stack.is_empty():
            final_decision += "Troubles with '[]'\n"
    
        if not quot_stack.is_empty():
            final_decision += "Troubles with '<>'\n"
    """))
