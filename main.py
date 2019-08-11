import file_operations
from file_operations import VERSION
from faker import Faker
from random import *


skills = [
    "Стремительный прыжок",
    "Электрический выстрел",
    "Ледяной удар",
    "Стремительный удар",
    "Кислотный взгляд",
    "Тайный побег",
    "Ледяной выстрел",
    "Огненный заряд"
]


letter = {
    'а': 'а͠', 'б': 'б̋', 'в': 'в͒͠',
    'г': 'г͒͠', 'д': 'д̋', 'е': 'е͠',
    'ё': 'ё͒͠', 'ж': 'ж͒', 'з': 'з̋̋͠',
    'и': 'и', 'й': 'й͒͠', 'к': 'к̋̋',
    'л': 'л̋͠', 'м': 'м͒͠', 'н': 'н͒',
    'о': 'о̋', 'п': 'п̋͠', 'р': 'р̋͠',
    'с': 'с͒', 'т': 'т͒', 'у': 'у͒͠',
    'ф': 'ф̋̋͠', 'х': 'х͒͠', 'ц': 'ц̋',
    'ч': 'ч̋͠', 'ш': 'ш͒͠', 'щ': 'щ̋',
    'ъ': 'ъ̋͠', 'ы': 'ы̋͠', 'ь': 'ь̋',
    'э': 'э͒͠͠', 'ю': 'ю̋͠', 'я': 'я̋',
    'А': 'А͠', 'Б': 'Б̋', 'В': 'В͒͠',
    'Г': 'Г͒͠', 'Д': 'Д̋', 'Е': 'Е',
    'Ё': 'Ё͒͠', 'Ж': 'Ж͒', 'З': 'З̋̋͠',
    'И': 'И', 'Й': 'Й͒͠', 'К': 'К̋̋',
    'Л': 'Л̋͠', 'М': 'М͒͠', 'Н': 'Н͒',
    'О': 'О̋', 'П': 'П̋͠', 'Р': 'Р̋͠',
    'С': 'С͒', 'Т': 'Т͒', 'У': 'У͒͠',
    'Ф': 'Ф̋̋͠', 'Х': 'Х͒͠', 'Ц': 'Ц̋',
    'Ч': 'Ч̋͠', 'Ш': 'Ш͒͠', 'Щ': 'Щ̋',
    'Ъ': 'Ъ̋͠', 'Ы': 'Ы̋͠', 'Ь': 'Ь̋',
    'Э': 'Э͒͠͠', 'Ю': 'Ю̋͠', 'Я': 'Я̋',
    ' ': ' '
}


fake = Faker("ru_RU")
letter_runic_list = []
skills_item = []


for i in range(len(skills)):
    for m in skills[i]:
        for j in letter:
            if j == m:
                skills_item.append(letter[j])
    if len(skills_item) == len(skills[i]):
        letter_runic_list.extend([skills_item])
        skills_item = []


letter_runic = {
    i: ''.join(letter_runic_list[i])
    for i in range(len(letter_runic_list))}


for i in range(0, 10):
    three_runic_skills = sample(list(letter_runic.values()), k=3)
    context = {
        "first_name": fake.first_name_male(),
        "last_name": fake.last_name_male(),
        "job": fake.job(),
        "town": fake.city(),
        "strength": randint(8, 14),
        "agility": randint(8, 14),
        "endurance": randint(8, 14),
        "intelligence": randint(8, 14),
        "luck": randint(8, 14),
        "skill_1": three_runic_skills[0],
        "skill_2": three_runic_skills[1],
        "skill_3": three_runic_skills[2]
    }
    file_operations.render_template("profiles/charsheet-{}.svg".format(i), "profiles/result-{}.svg".format(i), context)
