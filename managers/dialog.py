import os
from os import path
from models.menu import MenuButton, MenuAction
from telebot import TeleBot
from managers.keyboards import BotKeyboards
from tools import constants


class Dialog(object):
    def __init__(self, bot: TeleBot, bot_keyboard: BotKeyboards, callback=None, message=None):
        self.bot = bot

        if callback:
            self.message_id = callback.message.message_id
            user = callback.from_user
            self.chat_id = user.id
            self.user_info = f"{user.first_name} {user.last_name}"

        elif message:
            self.message_id = message.message_id
            self.chat_id = message.chat.id
            user = message.from_user
            self.user_info = f"{user.first_name} {user.last_name}"

        self.menu_buttons = [
            MenuButton(bot_keyboard.callback_lessons, constants.lessons_info, bot_keyboard.lessons_keyboard()),
            MenuButton(bot_keyboard.callback_about_university, "про університет", bot_keyboard.back_keyboard()),
            MenuButton(bot_keyboard.callback_vstup, constants.vstup_info, bot_keyboard.vstup_keyboard()),
            MenuButton(bot_keyboard.callback_zno, constants.zno_info, bot_keyboard.zno_keyboard()),
            MenuButton(bot_keyboard.callback_have_questions, constants.contacts_have_questions, bot_keyboard.contacts_keyboard()),

            MenuButton(bot_keyboard.callback_back_to_main, self.user_info + constants.start_info,
                       bot_keyboard.main_keyboard())
        ]

        self.menu_actions = [
            MenuAction(bot_keyboard.callback_lessons,
                       images=["images/calendar/bakalavr.jpg", "images/calendar/magistr.jpg"]),

            MenuAction(
                bot_keyboard.zno_language,
                constants.zno_language_info,
                image="images/zno/language.jpg",
                keyboard=bot_keyboard.link_keyboard("Детальніше",
                                                    "https://testportal.gov.ua/skladnyky-natsionalnogo-multypredmetnogo-testu-ukrayinska-mova/")
            ),
            MenuAction(
                bot_keyboard.zno_math,
                constants.zno_math_info,
                image="images/zno/math.jpg",
                keyboard=bot_keyboard.link_keyboard("Детальніше",
                                                    link="https://testportal.gov.ua/skladnyky-natsionalnogo-multypredmetnogo-testu-matematyka/")
            ),
            MenuAction(
                bot_keyboard.zno_history,
                constants.zno_history_info,
                image="images/zno/history.jpg",
                keyboard=bot_keyboard.link_keyboard("Детальніше",
                                                    link="https://testportal.gov.ua/skladnyky-natsionalnogo-multypredmetnogo-testu-istoriya-ukrayiny/")
            ),

            MenuAction(bot_keyboard.vstup_sertificat, constants.vstup_sertificat),
            MenuAction(bot_keyboard.vstup_child, constants.vstup_child),
            MenuAction(bot_keyboard.vstup_balls, constants.vstup_balls),
            MenuAction(bot_keyboard.vstup_atestat, constants.vstup_atestat),
            MenuAction(bot_keyboard.vstup_addiction_information, constants.vstup_addiction_information)
            # MenuAction(bot_keyboard.vstup_have_questions, constants.vstup_have_questions)
        ]

    def edit_message_text(self, text, keyboard=None):
        if keyboard:
            self.bot.edit_message_text(message_id=self.message_id, chat_id=self.chat_id, text=text,
                                       reply_markup=keyboard, parse_mode="HTML")
        else:
            self.bot.edit_message_text(message_id=self.message_id, chat_id=self.chat_id, text=text, parse_mode="HTML")

    def send_photo(self, image_name):
        image_path = path.join(os.getcwd(), image_name)

        if os.path.isfile(image_path):
            with open(image_path, "rb") as image:
                self.bot.send_photo(self.chat_id, image)

    def menu_transition(self, menu_item: MenuButton):
        self.edit_message_text(menu_item.text, menu_item.keyboard)

    def menu_action(self, action: MenuAction):
        text = action.text
        images = action.images
        image = action.image

        if images:
            for image in images:
                self.send_photo(image)

        elif image:
            self.send_photo(image)

        if text:
            if action.keyboard:
                self.bot.send_message(self.chat_id, text, reply_markup=action.keyboard, parse_mode="HTML")
            else:
                self.bot.send_message(self.chat_id, text, parse_mode="HTML")
