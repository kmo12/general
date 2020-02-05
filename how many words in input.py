while True:
    phrase = input("Введите фразу: ")
    words_counter = 1

    if phrase:
        for i in phrase:
            if i == " ":
                words_counter += 1
        else:
            print("Количество слов в вашей фразе:", words_counter)
    else:
        print("Вы не ввели фразу\n")
        continue

    break
