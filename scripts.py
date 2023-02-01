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


def get_schoolkid(schoolkid_name):
    from datacenter.models import Schoolkid
    try:
        return Schoolkid.objects.get(full_name__contains=schoolkid_name)
    except Schoolkid.MultipleObjectsReturned:
        print(f"Слишком много совпадений по имени: {schoolkid_name}, уточните запрос.")
        return
    except Schoolkid.DoesNotExist:
        print(f"Пользователь с именем: {schoolkid_name} не найден.")
        return


def get_subject(subject_name, schoolkid):
    from datacenter.models import Subject
    from random import choice
    if subject_name:
        try:
            return Subject.objects.get(title=subject_name, year_of_study=schoolkid.year_of_study)
        except Subject.MultipleObjectsReturned:
            print(f"Слишком много совпадений с предметом: {subject_name}, уточните запрос.")
            return
        except Subject.DoesNotExist:
            print(f"Предмет с названием: {subject_name} не найден.")
            return
    else:
        return choice(Subject.objects.filter(year_of_study=schoolkid.year_of_study))


def fix_marks(schoolkid_name):
    from datacenter.models import Mark
    schoolkid = get_schoolkid(schoolkid_name)
    if not schoolkid:
        return
    Mark.objects.filter(schoolkid=schoolkid, points__lt=4).update(points=5)


def remove_chastisements(schoolkid_name):
    from datacenter.models import Chastisement
    schoolkid = get_schoolkid(schoolkid_name)
    if not schoolkid:
        return
    Chastisement.objects.filter(schoolkid=schoolkid).delete()


def create_commendation(schoolkid_name, subject_name=None):
    from datacenter.models import Commendation, Lesson
    from random import choice
    schoolkid = get_schoolkid(schoolkid_name)
    if not schoolkid:
        return
    subject = get_subject(subject_name, schoolkid)
    if not subject:
        return
    random_lesson = Lesson.objects.filter(
        year_of_study=schoolkid.year_of_study,
        group_letter=schoolkid.group_letter,
        subject=subject
    ).order_by('?').first()
    commendation_text = choice(TOP_COMMENDATIONS)
    Commendation.objects.create(
        text=commendation_text,
        created=random_lesson.date,
        schoolkid=schoolkid,
        subject=random_lesson.subject,
        teacher=random_lesson.teacher
    )
