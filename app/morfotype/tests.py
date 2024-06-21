def morfotype_test(data):
    try:
        height = int(data['height'])
        weight = int(data['weight'])
        chest = int(data['chest'])
    except:
        return 'Не все данные представлены числами.\nНачните прохождение теста сначала.'
    
    index = height - (weight + chest)

    if index > 30: morfotype_result = 'Астенический'
    elif index < 10: morfotype_result =  'Гиперстенический'
    else: morfotype_result =  'Нормостенический'

    return f'Ваша длина тела: {height} см.\nВаша масса тела: {weight} кг.\nВаш охват груди: {chest} см.\n\nВаш индекс пинье: {index}\nВаш морфотип: {morfotype_result}'