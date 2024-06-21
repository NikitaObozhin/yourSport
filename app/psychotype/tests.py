def set_result_psychotype(results):
    results = results.values()
    results = ''.join(results)

    data = [(results.count('A'), 'A'), (results.count('B'), 'B'), 
            (results.count('C'), 'C'), (results.count('D' ), 'D')]
            
    data.sort(reverse=True)
    if data[0][1] == 'A':
        temp = 'Флегматик'
    elif data[0][1] == 'B':
        temp = 'Меланхолик'
    elif data[0][1] == 'C':
        temp = 'Холерик'
    else:
        temp = 'Сангвиник'

    return f'По результатам тестирования ваш темперамент: {temp}'
