while True:
    print('1-выдать информацию, хранящиюся в файле\n2- перезапистаь данные в текстовом файле\n3-дописать данные в текстовом файле\n4-выписать n предложение\n5-THE END')
    comand = input('Введите номер операции: ')
    if comand == '1':
        name_file = input('Введите название файла: ')
        try:
            with open(name_file) as f:
                print(f.readlines())
        except:
            print('Ошибка ввода\n\n')
    elif comand == '2':
        name_file = input('Введите название файла: ')
        with open(name_file, 'w') as f:
            inforamtion = input('Введите, что нужно записать в файл: ')
            f.write(inforamtion)
    elif comand == '3':
        name_file = input('Введите название файла: ')
        with open(name_file, 'a') as f:
            inforamtion = input('Введите, что нужно записать в файл')
            f.write(inforamtion)
    elif comand == '4':
        name_file = input('Введите название файла: ')
        with open(name_file, 'a') as f:
            f.readline(int(input('Введите номер страницы')))
    else:
        exit()