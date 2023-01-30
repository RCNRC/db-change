TOP_COMMENDATIONS = [
    "Молодец!",
    "Отлично!",
    "Хорошо!",
    "Гораздо лучше, чем я ожидал!",
    "Ты меня приятно удивил!",
    "Великолепно!",
    "Прекрасно!",
    "Ты меня очень обрадовал!",
    "Именно этого я давно ждал от тебя!",
    "Сказано здорово – просто и ясно!",
    "Ты, как всегда, точен!",
    "Очень хороший ответ!",
    "Талантливо!",
    "Ты сегодня прыгнул выше головы!",
    "Я поражен!",
    "Уже существенно лучше!",
    "Потрясающе!",
    "Замечательно!",
    "Прекрасное начало!",
    "Так держать!",
    "Ты на верном пути!",
    "Здорово!",
    "Это как раз то, что нужно!",
    "Я тобой горжусь!",
    "С каждым разом у тебя получается всё лучше!",
    "Мы с тобой не зря поработали!",
    "Я вижу, как ты стараешься!",
    "Ты растешь над собой!",
    "Ты многое сделал, я это вижу!",
    "Теперь у тебя точно все получится!",
]


def fix_marks(schoolkid):
    from datacenter.models import Mark
    frolov_bad_marks = Mark.objects.filter(schoolkid=schoolkid, points__lt=4)
    for mark in frolov_bad_marks:
        mark.points = 5
        mark.save()


def remove_chastisements(schoolkid):
    from datacenter.models import Chastisement
    Chastisement.objects.filter(schoolkid=schoolkid).delete()


def create_commendation(schoolkid_name="Фролов Иван", subject_name=None):
    from datacenter.models import Commendation, Lesson, Subject, Schoolkid
    from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist
    from random import choice
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=schoolkid_name)
    except MultipleObjectsReturned:
        print("Слишком много совпадений по введённому имени, уточните запрос.")
        return
    except ObjectDoesNotExist:
        print("По введённому имени пользователь не найден.")
        return
    if subject_name:
        subject = Subject.objects.get(title=subject_name, year_of_study=schoolkid.year_of_study)
    else:
        subject = choice(Subject.objects.filter(year_of_study=schoolkid.year_of_study))
    schoolkid_lessons = Lesson.objects.filter(year_of_study=schoolkid.year_of_study, group_letter=schoolkid.group_letter, subject=subject)
    random_lesson = choice(schoolkid_lessons)
    commendation_text = choice(TOP_COMMENDATIONS)
    Commendation.objects.create(text=commendation_text, created=random_lesson.date, schoolkid=schoolkid, subject=random_lesson.subject, teacher=random_lesson.teacher)

