from datacenter.models import Mark, Schoolkid, Lesson, Chastisement, Commendation
import random


def get_schoolkid(schoolkid_name):
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=schoolkid_name)

        return schoolkid

    except Schoolkid.DoesNotExist:
        print("Такого ученика нет в базе \nПроверьте правильность написания фамилии и имени, а также их порядок \n(сначала фамилия, потом имя)")

    except Schoolkid.MultipleObjectsReturned:
        print("Напишите фамилию и имя ученика")


def fix_marks(schoolkid):
    schoolkid_bad_marks = Mark.objects.filter(points__in=[2, 3],
                                              schoolkid=schoolkid)
    schoolkid_bad_marks.update(points=5)


def remove_chastisements(schoolkid):
    schoolkid_chastisements = Chastisement.objects.all()
    schoolkid_chastisements.delete()


def create_commendation(schoolkid, subject_title):
    commendations = ["Молодец!", "Отлично!", "Хорошо!",
                     "Гораздо лучше, чем я ожидал!",
                     "Ты меня приятно удивил!", "Великолепно!", "Прекрасно!",
                     "Ты меня очень обрадовал!",
                     "Именно этого я давно ждал от тебя!"
                     "Сказано здорово – просто и ясно!",
                     "Ты, как всегда, точен!",
                     "Очень хороший ответ!", "Талантливо",
                     "Ты сегодня прыгнул выше головы!", "Я поражен!",
                     "Уже существенно лучше!", "Потрясающе!",
                     "Замечательно!", "Прекрасное начало!", "Так держать!",
                     "Ты на верном пути!", "Здорово!",
                     "Это как раз то, что нужно!", "Я тобой горжусь!",
                     "С каждым разом у тебя получается всё лучше!",
                     "Мы с тобой не зря поработали!",
                     "Я вижу, как ты стараешься!", "Ты растешь над собой!",
                     "Ты многое сделал, я это вижу!",
                     "Теперь у тебя точно все получится!"]

    try:
        schoolkid_lessons = Lesson.objects.filter(year_of_study=6,
                                                  group_letter="А",
                                                  subject__title=subject_title)
        schoolkid_lesson = random.choice(schoolkid_lessons)
        Commendation.objects.create(text=random.choice(commendations),
                                    created=schoolkid_lesson.date,
                                    schoolkid=schoolkid,
                                    subject=schoolkid_lesson.subject,
                                    teacher=schoolkid_lesson.teacher)
    except IndexError:
        print("Проверьте правильность написания предмета")
