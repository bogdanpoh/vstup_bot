import os.path
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from managers.file import FileManager


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

        #university
        self.university_how_find_us = "university_how_find_us"

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

        #motivation letter
        self.callback_motivation_letter = "callback_motivation_letter"

        # speciality
        self.callback_speciality = "s_"

        # sex
        self.sex_man = "sex_man"
        self.sex_woman = "sex_woman"

        # yes, no
        self.callback_yes = "callback_yes"
        self.callback_no = "callback_no"

        # back button
        self.callback_back_to_main = "back_to_main"

    def main_keyboard(self) -> InlineKeyboardMarkup:
        markup = InlineKeyboardMarkup(row_width=1)
        markup.add(
            InlineKeyboardButton("📚 Навчання", callback_data=self.callback_lessons),
            InlineKeyboardButton("🏫 Про університет", callback_data=self.callback_about_university),
            InlineKeyboardButton("📑 Вступна компанія 2022", callback_data=self.callback_vstup),
            InlineKeyboardButton("✍️ ЗНО (НМТ) 2022", callback_data=self.callback_zno),
            InlineKeyboardButton("☎️ Контакти приймальної комісії", callback_data=self.callback_have_questions),
            InlineKeyboardButton("📩 Генератор мотиваційного листа", callback_data=self.callback_motivation_letter)
        )

        return markup

    def lessons_keyboard(self) -> InlineKeyboardMarkup:
        markup = InlineKeyboardMarkup(row_width=1)
        markup.add(
            self.make_link_button("Бакалавр", link="https://nupp.edu.ua/page/spetsialnosti-osvitni-programi-ta-spetsializatsii.html"),
            self.make_link_button("Магістр", link="https://nupp.edu.ua/page/spetsialnosti-osvitni-programi-ta-spetsializatsii.html"),
            self.make_link_button("Доктор філософії", link="https://nupp.edu.ua/page/spetsialnosti-aspiranturi.html"),
            self.make_back_button()
        )

        return markup

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

    def university_keyboard(self) -> InlineKeyboardMarkup:
        markup = InlineKeyboardMarkup(row_width=1)
        markup.add(
            self.make_link_button("Детальніше", "https://nupp.edu.ua/page/vstup.html"),
            self.make_link_button("Спеціальності", "https://nupp.edu.ua/page/spetsialnosti-osvitni-programi-ta-spetsializatsii.html"),
            self.make_link_button("Освітній центр «КРИМ - УКРАЇНА»", "https://nupp.edu.ua/page/osvitniy-tsentr-krim-ukraina.html"),
            self.make_link_button("Освітній центр «ДОНБАС – УКРАЇНА»", "https://nupp.edu.ua/page/osvitniy-tsentr-donbas-ukraina.html"),
            self.make_link_button("Безкоштовні тренінги «Високий бал НМТ»", "https://nupp.edu.ua/news/vidkrita-reestratsiya-na-trening-visokiy-bal-nmt.html"),
            self.make_link_button("Міжнародні програми", "https://nupp.edu.ua/page/mizhnarodni-programi.html"),
            self.make_link_button("Підготовчі курси", "https://nupp.edu.ua/page/pidgotovche-viddilennya.html"),
            self.make_link_button("Держзамовлення", "https://nupp.edu.ua/page/derzhzamovlennya.html"),
            self.make_link_button("Вступ на основі повної загальної середньої освіти", "https://nupp.edu.ua/page/vstup-na-osnovi-pzso.html"),
            self.make_link_button("Вступ на основі рівня молодшого спеціаліста", "https://nupp.edu.ua/page/vstup-na-osnovi-okr-ms.html"),
            self.make_link_button("Вступ на основі ступеня бакалавра, магістра", "https://nupp.edu.ua/page/vstup-na-osnovi-stupenya-bakalavra-magistra.html"),
            self.make_link_button("Приймальна комісія", "https://vstup.nupp.edu.ua"),
            self.make_link_button("Вартість навчання", "https://vstup.nupp.edu.ua/page/vartist-navchannya.html"),
            self.make_link_button("Реквізити", "https://nupp.edu.ua/page/requisites.html"),
            self.make_link_button("Вступ на кафедру військової підготовки", "https://nupp.edu.ua/page/vstup-na-viyskovu-kafedru.html"),
            self.make_link_button("Післядипломна освіта", "https://nupp.edu.ua/page/pislyadiplomna-osvita-pidvishchennya-kvalifikatsii-ta-stazhuvannya.html"),
            self.make_link_button("Аспірантура та Докторантура", "https://nupp.edu.ua/page/aspirantura-ta-doktorantura.html"),
            self.make_link_button("Студентське самоврядування", "https://nupp.edu.ua/page/studentske-samovriaduvannya.html"),
            InlineKeyboardButton("Як нас знайти?", callback_data=self.university_how_find_us),
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

    def specialities_keyboard(self) -> InlineKeyboardMarkup:
        markup = InlineKeyboardMarkup(row_width=2)
        specialities = FileManager.get_specialities()

        for key, speciality_name in specialities.items():
            callback = f"{self.callback_speciality}{key}"
            markup.add(InlineKeyboardButton(speciality_name, callback_data=callback))

        return markup

    def sex_keyboard(self) -> InlineKeyboardMarkup:
        markup = InlineKeyboardMarkup(row_width=1)
        markup.add(
            InlineKeyboardButton("Ч", callback_data=self.sex_man),
            InlineKeyboardButton("Ж", callback_data=self.sex_woman)
        )

        return markup

    def yes_no_keyboard(self) -> InlineKeyboardMarkup:
        markup = InlineKeyboardMarkup(row_width=1)
        markup.add(
            InlineKeyboardButton("Так", callback_data=self.callback_yes),
            InlineKeyboardButton("Ні", callback_data=self.callback_no)
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
        button_title = "↩️ Назад"
        button = InlineKeyboardButton(button_title, callback_data=data if data else self.callback_back_to_main)

        return button

    def make_link_button(self, text=None, link=None):
        default_name = "Довідкова інформація"
        button_title = f"🔗 {text if text else default_name}"
        button = InlineKeyboardButton(button_title, url=link)

        return button

