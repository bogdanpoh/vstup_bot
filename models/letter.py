from models.base import BaseModel


class MotivationLetter(BaseModel):
    def __init__(self,
                 usernname=None,
                 speciality=None,
                 school_name=None,
                 best_lessons=None,
                 three_motivation=None,
                 action_out_lessons=None,
                 have_success_in_competition=None,
                 sex=None,
                 have_great_attestat=None):
        self.username = usernname
        self.speciality = speciality
        self.school_name = school_name
        self.best_lessons = best_lessons
        self.three_motivation = three_motivation
        self.action_out_lessons = action_out_lessons
        self.have_success_in_competition = have_success_in_competition
        self.sex = sex
        self.have_great_attestat = have_great_attestat

    def make_text(self) -> str:
        is_man = self.sex == "man"

        sex_text = "закінчив" if is_man else "закінчила"
        sex_text_2 = "брав" if is_man else "брала"
        sex_text_3 = "зацікавився" if is_man else "цікавилася"
        sex_text_4 = "хотів" if is_man else "хотіла"
        sex_text_5 = "отримував" if is_man else "отримувала"

        school_text = f"В цьому році я із відзнакою {sex_text} {self.school_name}" if self.have_great_attestat else f"У цьому році я {sex_text} {self.school_name}"
        success_in_completion_text = f"Протягом навчання в школі я {sex_text_2} участь в предметних олімпіадах та маю наступні результати: {self.have_success_in_competition}." if str(self.have_success_in_competition) != "0" else ""

        text = f"""
Шановний Володимире Олександровичу!

Я пишу цей мотиваційний лист, бо прагну навчатися в Національному університеті «Полтавська політехніка» на бакалаврській 
програмі зі спеціальності «{self.speciality}», оскільки Ваш університет має низку переваг, серед яких найвагомішими для мене є:
{self.three_motivation}.

{school_text}.
{success_in_completion_text}
Я не лише маю хороші оцінки з профільних предметів, такі як {self.best_lessons} але й 
також {sex_text_3} навчальними дисциплінами цієї спеціальності, які не входять у шкільну програму.

Я завжди {sex_text_4} здобути навички з освітньої програми «{self.speciality}» і я вважаю, що ваш університет може допомогти мені 
перетворити свою мрію в реальність.

Я розумію, що для того, щоб бути хорошим фахівцем потрібно поєднувати навчання та практичну роботу. Тому у вільний від навчання в школі час, я {sex_text_5} практичний досвід, {self.action_out_lessons}.
Цей практичний досвід лише підвищив мій інтерес продовжувати освіту та вступити на 
бакалаврат за спеціальністю «{self.speciality}».

З повагою, {self.username}
"""
        return text