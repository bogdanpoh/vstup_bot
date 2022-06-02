from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


class BotKeyboards(object):
    def __init__(self):
        # callbacks:

        # main
        self.callback_lessons = "main_lessons"
        self.callback_about_university = "main_about_university"
        self.callback_vstup = "main_vstup"
        self.callback_zno = "main_vstup_company"
        self.callback_have_questions = "vstup_have_questions"

        # lessons
        self.lessons_bakalavr = "lessons_bakalavr"
        self.lessons_magistr = "lessons_magistr"
        self.lessons_doctor_philosophii = "lessons_doctor_philosophii"

        self.lessons_form_bakalavr = "lessons_form_bakalavr"
        self.lessons_form_magistr = "lessons_form_magistr"
        self.lessons_form_doctor_philosophii = "lessons_form_doctor_philosophii"

        # zno
        self.zno_language = "zno_language"
        self.zno_math = "zno_math"
        self.zno_history = "zno_history"

        # vstup
        self.vstup_sertificat = "vstup_sertificat"
        self.vstup_child = "vstup_child"
        self.vstup_balls = "vstup_balls"
        self.vstup_atestat = "vstup_atestat"
        self.vstup_addiction_information = "vstup_addiction_information"
        # back button
        self.callback_back_to_main = "back_to_main"

    def main_keyboard(self) -> InlineKeyboardMarkup:
        markup = InlineKeyboardMarkup(row_width=1)
        markup.add(
            InlineKeyboardButton("Навчання", callback_data=self.callback_lessons),
            InlineKeyboardButton("Про університет", callback_data=self.callback_about_university),
            InlineKeyboardButton("Вступна компанія 2022", callback_data=self.callback_vstup),
            InlineKeyboardButton("ЗНО (НМТ) 2022", callback_data=self.callback_zno),
            InlineKeyboardButton("Контакти приймальної комісії", callback_data=self.callback_have_questions)
        )

        return markup

    def lessons_keyboard(self) -> InlineKeyboardMarkup:
        markup = InlineKeyboardMarkup(row_width=1)
        markup.add(
            InlineKeyboardButton("Бакалавр", url="https://nupp.edu.ua/page/spetsialnosti-osvitni-programi-ta-spetsializatsii.html"),
            InlineKeyboardButton("Магістр", url="https://nupp.edu.ua/page/spetsialnosti-osvitni-programi-ta-spetsializatsii.html"),
            InlineKeyboardButton("Доктор філософії", url="https://nupp.edu.ua/page/spetsialnosti-aspiranturi.html"),
            self.make_back_button()
        )

        return markup

    # def lessons_form_keyboard(self, callback_data: str) -> InlineKeyboardMarkup:
    #     markup = InlineKeyboardMarkup(row_width=1)
    #
    #     markup.add(
    #         self.make_link_button("Спеціальності", "https://nupp.edu.ua/page/spetsialnosti-osvitni-programi-ta-spetsializatsii.html"),
    #         InlineKeyboardButton("Форми", callback_data=callback_data)
    #     )
    #
    #     return markup

    def zno_keyboard(self) -> InlineKeyboardMarkup:
        markup = InlineKeyboardMarkup(row_width=1)
        markup.add(
            InlineKeyboardButton("Про тест з української мови", callback_data=self.zno_language),
            InlineKeyboardButton("Про тест з математики", callback_data=self.zno_math),
            InlineKeyboardButton("Про тест з історії України", callback_data=self.zno_history),
            self.make_link_button(link="https://testportal.gov.ua/zno-dpa-2/"),
            self.make_back_button()
        )

        return markup

    def vstup_keyboard(self) -> InlineKeyboardMarkup:
        markup = InlineKeyboardMarkup(row_width=1)
        markup.add(
            InlineKeyboardButton("Сертифікат ЗНО минулих років", callback_data=self.vstup_sertificat),
            InlineKeyboardButton("Діти з окупованих територій", callback_data=self.vstup_child),
            InlineKeyboardButton("Порогові бали", callback_data=self.vstup_balls),
            InlineKeyboardButton("Хто може видавати атестат?", callback_data=self.vstup_atestat),
            InlineKeyboardButton("Додаткова інформація про вступ", callback_data=self.vstup_addiction_information),
            # InlineKeyboardButton("Контакти приймальної комісії", callback_data=self.vstup_have_questions),
            self.make_back_button()
        )

        return markup

    def contacts_keyboard(self) -> InlineKeyboardMarkup:
        markup = InlineKeyboardMarkup(row_width=1)
        markup.add(
            self.make_link_button("Детальніше", "https://vstup.nupp.edu.ua/page/contacts.html"),
            self.make_back_button()
        )
        return markup

    def back_keyboard(self, data: str = None) -> InlineKeyboardMarkup:
        markup = InlineKeyboardMarkup(row_width=1)
        markup.add(self.make_back_button(data))

        return markup

    def link_keyboard(self, text, link) -> InlineKeyboardMarkup:
        markup = InlineKeyboardMarkup(row_width=1)
        markup.add(
            self.make_link_button(text, link)
        )

        return markup

    def make_back_button(self, data: str = None) -> InlineKeyboardButton:
        button = InlineKeyboardButton("Назад", callback_data= data if data else self.callback_back_to_main)
        return button

    def make_link_button(self, text=None, link=None):
        button = InlineKeyboardButton(text if text else "Довідкова інформація", url=link)
        return button

