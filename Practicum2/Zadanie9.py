answer = input("Собака короткошерстной породы? ")

if answer == "да":
    answer = input("Рост собаки менее 50 см? ")
    if answer == "да":
        answer = input("У собаки короткий хвост? ")
        if answer == "да":
            breed = "Английский бульдог"
        else:
            breed = "Бигль"
    else:
        answer = input("Вес собаки более 50 кг? ")
        if answer == "да":
            breed = "Датский дог"
        else:
            breed = "Фоксхаунд"
else:
    answer = input("Рост собаки менее 50 см? ")
    if answer == "да":
        answer = input("У собаки доброжелательный характер? ")
        if answer == "да":
            breed = "Кокер-спаниэль"
        else:
            breed = "Ирландский сеттер"
    else:
        answer = input("У собаки рост менее 70 см? ")
        if answer == "да":
            answer = input("У собаки длинные уши? ")
            if answer == "да":
                breed = "Большой вандейский грифон"
            else:
                breed = "Колли"
        else:
            answer = input("Окрас рыжий с белыми отметинами? ")
            if answer == "да":
                breed = "Сенбернар"
            else:
                answer = input("Белоснежный окрас? ")
                if answer == "да":
                    breed = "Ирландский волкодав"
                else:
                    breed = "Ньюфаундленд"

print("Результат: определенная порода —", breed)