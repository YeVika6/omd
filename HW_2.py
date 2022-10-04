def hierarchy(file_name: str) -> dict:  # сюда ещё аргументы дописать
    '''Выводим иерархию'''
    with open(file_name, 'r', encoding='utf8') as file:
        next(file)
        dep_team = {}
        for line in file:
            seperated_line = line.split(';')
            department = seperated_line[1]
            team = seperated_line[2]
            if department not in dep_team:
                dep_team[department] = set()
            dep_team[department].add(team)
        for department, teams in dep_team.items():
            print(department, ':')
            for team in teams:
                print('-', team)


def salary_range(file_name: str) -> dict:  # сюда ещё аргументы дописать
    '''Найдем численность сотрудников в вилку вилку зарплат'''
    with open(file_name, 'r', encoding='utf8') as file:
        next(file)
        dep_workers = {}
        dep_salary = {}
        for line in file:
            seperated_line = line.split(';')
            department = seperated_line[1]
            salary = seperated_line[5]
            if department not in dep_workers:
                dep_workers[department] = 0
            dep_workers[department] += 1
            if department not in dep_salary:
                dep_salary[department] = list()
            dep_salary[department].append(int(salary))
        for department in dep_salary.keys():
            salaries = dep_salary[department]
            num_workers = dep_workers[department]
            print(department, ':')
            print('Количество сотрудников:', num_workers)
            print('Минимальная зарплата:', min(salaries))
            print('Максимальная зарплата:', max(salaries))
            print('Средняя зарплата:', sum(salaries)/len(salaries), '\n')


def report(file_name: str, report_filename: str):
    '''Составим отчет'''
    dep_workers = {}
    dep_salary = {}
    with open(file_name, 'r', encoding='utf8') as file:
        next(file)
        for line in file:
            seperated_line = line.split(';')
            department = seperated_line[1]
            salary = seperated_line[5]
            if department not in dep_workers:
                dep_workers[department] = 0
            dep_workers[department] += 1
            if department not in dep_salary:
                dep_salary[department] = list()
            dep_salary[department].append(int(salary))
    with open(report_filename, "w+", encoding='utf8') as report_file:
        print('Департамент', 'Количество сотрудников', 'Минимальная зарплата', 'Максимальная зарплата', 'Средняя зарплата', file=report_file, sep=';')
        for department in dep_salary.keys():
            salaries = dep_salary[department]
            num_workers = dep_workers[department]
            print(department, num_workers, min(salaries), max(salaries), sum(salaries)/len(salaries), file=report_file, sep=';')


def menu(some_answer: int):
    input_file = 'Corp_Summary.csv'
    output_file = 'Report_file.csv'
    if some_answer == 1:
        hierarchy(input_file)
    elif some_answer == 2:
        salary_range(input_file)
    else:
        report(input_file, output_file)


def main():
    print(
        '1 - Иерархия команд\n'
        '2 - Сводный ответ по департаментам\n'
        '3 - Сохранить сводный отчет в файл\n'
        )
    answer = int(input())
    menu(answer)


if __name__ == '__main__':
    main()
