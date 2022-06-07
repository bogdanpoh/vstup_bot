import os
from os import path
from models.menu import MenuButton, MenuAction
from models.letter import MotivationLetter
from telebot import TeleBot
from managers.keyboards import BotKeyboards
from tools import constants


class Dialog(object):
    def __init__(self, bot: TeleBot, bot_keyboard: BotKeyboards, callback=None, message=None, motivation_letter: MotivationLetter=None):
        self.bot = bot
        self.bot_keyboard = bot_keyboard
        self.message = None
        self.motivation_letter = motivation_letter

        if callback:
            self.message_id = callback.message.message_id
            user = callback.from_user
            self.chat_id = user.id
            self.user_info = f"{user.first_name} {user.last_name}" if user.last_name else f"{user.first_name}"
            self.message = callback.message

        elif message:
            self.message_id = message.message_id
            self.chat_id = message.chat.id
            user = message.from_user
            self.user_info = f"{user.first_name} {user.last_name}" if user.last_name else f"{user.first_name}"
            self.message = message

        self.menu_buttons = [
            MenuButton(bot_keyboard.callback_lessons, constants.lessons_info, bot_keyboard.lessons_keyboard()),
            MenuButton(bot_keyboard.callback_about_university, constants.university_info, bot_keyboard.university_keyboard()),
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
                bot_keyboard.university_how_find_us,
                constants.university_how_find_us,
                image="images/geo.png",
                keyboard=bot_keyboard.link_keyboard("Знайти нас на мапі", "https://goo.gl/maps/Fz6m4iagcdT2U6fz7")
            ),

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
            MenuAction(bot_keyboard.vstup_addiction_information, constants.vstup_addiction_information),

            MenuAction("s_", constants.ml_get_school, action=lambda: self.motivation_letter_continue)
        ]

    def edit_message_text(self, text, keyboard=None):
        if keyboard:
            return self.bot.edit_message_text(message_id=self.message_id, chat_id=self.chat_id, text=text,
                                       reply_markup=keyboard, parse_mode="HTML")
        else:
            return self.bot.edit_message_text(message_id=self.message_id, chat_id=self.chat_id, text=text, parse_mode="HTML")

    def send_photo(self, image_name):
        image_path = path.join(os.getcwd(), image_name)

        if os.path.isfile(image_path):
            with open(image_path, "rb") as image:
                self.bot.send_photo(self.chat_id, image)

    def menu_transition(self, menu_item: MenuButton):
        self.edit_message_text(menu_item.text, menu_item.keyboard)

    def menu_action(self, menu_action: MenuAction):
        text = menu_action.text
        images = menu_action.images
        image = menu_action.image

        if menu_action.action:
            msg = self.edit_message_text(text)
            self.bot.register_next_step_handler(msg, menu_action.action())
        else:
            if images:
                for image in images:
                    self.send_photo(image)

            elif image:
                self.send_photo(image)

            if text:
                if menu_action.keyboard:
                    self.bot.send_message(self.chat_id, text, reply_markup=menu_action.keyboard, parse_mode="HTML")
                else:
                    self.bot.send_message(self.chat_id, text, parse_mode="HTML")

    def motivation_letter_start(self, username):
        self.bot.send_message(self.chat_id, username + constants.ml_start_info, reply_markup=self.bot_keyboard.specialities_keyboard())

    def motivation_letter_continue(self, message):
        self.motivation_letter.school_name = message.text
        msg = self.edit_message_text(constants.ml_get_best_lessons)

        self.bot.register_next_step_handler(msg, self.best_lessons)

    def best_lessons(self, message):
        self.motivation_letter.best_lessons = message.text
        msg = self.edit_message_text(constants.ml_best_three_motivation)

        self.bot.register_next_step_handler(msg, self.best_three_motivation)

    def best_three_motivation(self, message):
        self.motivation_letter.three_motivation = message.text
        msg = self.edit_message_text(constants.ml_action_out_lessons)

        self.bot.register_next_step_handler(msg, self.action_out_lessons)

    def action_out_lessons(self, message):
        self.motivation_letter.action_out_lessons = message.text
        msg = self.edit_message_text(constants.ml_have_success_in_competition)

        self.bot.register_next_step_handler(msg, self.have_success_in_competition)

    def have_success_in_competition(self, message):
        self.motivation_letter.have_success_in_competition = message.text

        self.edit_message_text(constants.ml_get_sex, keyboard=self.bot_keyboard.sex_keyboard())

    def have_great_attestat(self):
        self.edit_message_text(constants.ml_have_great_attestat, keyboard=self.bot_keyboard.yes_no_keyboard())

    def make_motivation_letter(self):
        text = self.motivation_letter.make_text()
        self.bot.send_message(self.chat_id, text)
