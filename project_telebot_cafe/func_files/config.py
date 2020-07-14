# Before work you need to contact @BotFather in telegram and create an API token.
# Than put it below in the empty string.
def api_token():
    return "0000000000:AAAAAAAaAaaAAAAAAaA_aaaAaaAaAaaAaaa"


def yandex_corp_id():
    return 000000000000


def pg_db_connection_info():
    return ("",  # database
            "",  # user
            "",  # password
            "",  # host
            "5432",  # port
            )


# In case you need to use proxy for connection.
# Still can't make it work and now Im using dedicated server.

# >> pip install pysocks
# from telebot import apihelper
# apihelper.proxy = {'https': 'socks5://0.000.000.00:0000/'}
