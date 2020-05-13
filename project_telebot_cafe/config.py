from telebot import apihelper


# Before work you need to contact @BotFather in telegram and create an API token.
# Than put it below in the empty string.
def api_token():
    return ""


# In case you need to use proxy for connection.
# Still can't make it work and using dedicated server.

# pip install pysocks
# apihelper.proxy = {'https': 'socks5://5.252.161.48:1080/'}
# apihelper.proxy = {'https': 'socks5://138.68.165.154:1080/'}
