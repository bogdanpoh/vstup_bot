from telebot import TeleBot
from datetime import datetime
from managers.keyboards import BotKeyboards
from managers.dialog import Dialog
from models.menu import MenuAction
from tools.switch import Switch
from tools import constants
import configs

bot = TeleBot(configs.token)
bot_keyboard = BotKeyboards()

command_list = ["start"]


# system
def get_current_date() -> str:
    # now = datetime.datetime.now() - datetime.timedelta(minutes=7)
    now = datetime.now()
    formatted_date = now.strftime("%d.%m.%Y %H:%M")

    return formatted_date


def show_log(message):
    msg = str(message.text)
    chat_id = message.chat.id
    date = get_current_date()

    print(f"{date} {chat_id} - {msg}")


# bot functions
def get_user_info(message) -> str:
    user = message.from_user
    user_info = f"{user.first_name} {user.last_name}"

    return user_info


# handlers
@bot.callback_query_handler(func=lambda call: True)
def callback_query(callback):
    dialog = Dialog(bot, bot_keyboard, callback=callback)
    data = callback.data

    for menu_button in dialog.menu_buttons:
        if menu_button.identifier == data:
            dialog.menu_transition(menu_button)

    for menu_action in dialog.menu_actions:
        if menu_action.identifier == data:
            dialog.menu_action(menu_action)


@bot.message_handler(commands=command_list)
def command_handler(message):
    msg = str(message.text)
    user_info = get_user_info(message)
    dialog = Dialog(bot, bot_keyboard, message=message)

    start_action = MenuAction(
        text=user_info + constants.start_info,
        image="images/logo.png",
        keyboard=bot_keyboard.main_keyboard()
    )

    Switch(msg)\
        .case("/start", lambda: dialog.menu_action(start_action))

    show_log(message)


@bot.message_handler(content_types="text")
def text_handler(message):
    show_log(message)


# main
def main():
    try:
        bot.infinity_polling()
    except Exception as ex:
        bot.send_message(constants.admin_chat_id, f"Error in main: {str(ex)}")


if __name__ == "__main__":
    main()
