# Guido van Rossum <guido@python.org>

def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()


def step2_umbrella():
    print('Утка решила взять зонтик, чтобы не намочить перья.')
    print('Но погода ей всё равно не понравилась,')
    print('поэтому она решила улететь на юг :)')


def step2_no_umbrella():
    print('Утка-маляр попала под проливной дождь.')
    print('Вся промокла, не смогла дойти до бара')
    print('И осталась без заслуженного пива в конце рабочего дня :(')


if __name__ == '__main__':
    step1()
