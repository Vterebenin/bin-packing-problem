"""
Генетический алгоритм решения задачи об упаковке в контейнеры
1) Сначала создаем первую случайную популяцию
...
"""
import operator
import random
import numpy as np


class Container(object):
    """ Контейнер(особь) с сохранением его суммы """
    def __init__(self):
        self.fitted_items = []
        self.current_items = []
        self.sum = 0
        self.chromosome = []
        self.activation = 0

    def set_params(self):
        indexes = []
        for gen_index, gen in enumerate(self.chromosome):
            if gen == 1:
                indexes.append(gen_index)
        self.fitted_items = [item for i, item in enumerate(self.current_items) if i in indexes]
        self.sum = sum(self.fitted_items)
        self.activation = len(self.fitted_items)

    def mutate(self):
        self.chromosome = [np.logical_not(gen).astype(int) for gen in self.chromosome]
        self.set_params()

    def limitation(self):
        self.set_params()
        return self.sum <= 1

    def __str__(self):
        """ Представление для печати """
        return 'Контейнер(сумма=%s, хромосома=%s предметы=%s)' % (self.sum, str(self.chromosome), str(self.fitted_items))


def generate_first_population(values):
    """
    генерация первой, случайной, популяции
    возвращает список контейнеров
    """
    containers = []
    population_count = 50

    for _ in range(population_count):
        container = Container()
        container.current_items = values
        container.chromosome = [random.randrange(2) for _ in values]
        containers.append(container)

    containers = [container for container in containers if container.limitation()]
    containers = sort_population(containers)
    return containers


def crossbreeding(containers):
    for key, container in enumerate(containers):
        try:
            parent_1 = container
            parent_2 = containers[key + 1]
            child_1 = Container()
            child_1.chromosome = parent_1.chromosome[:len(parent_1.chromosome)//2] + \
                    parent_2.chromosome[len(parent_2.chromosome) // 2:]
            child_2 = Container()
            child_2.chromosome = parent_2.chromosome[:len(parent_2.chromosome)//2] + \
                      parent_1.chromosome[len(parent_1.chromosome) // 2:]
            containers.append(child_1)
            containers.append(child_2)
            if key % 10 == 0:
                container.mutate()
            containers = sort_population(containers)
            containers = containers[:50]
        except IndexError:
            pass
    containers = [container for container in containers if container.limitation()]
    containers = sort_population(containers)
    return containers


def sort_population(population):
    population.sort(key=operator.attrgetter('activation'), reverse=True)
    return population


def run_generations(a_list):
    """ Упаковать предметы в контейнеры и показать результат """
    generations = 30

    best_containers = []
    for generation in range(generations):
        containers = generate_first_population(a_list)
        containers = crossbreeding(containers)
        best_container = containers[:50][0] if containers else 0

        if best_container == 0:
            break
        best_containers.append(best_container)
        indexes = []
        for gen_index, gen in enumerate(best_container.chromosome):
            if gen == 1:
                indexes.append(gen_index)
        a_list = [item for i, item in enumerate(a_list) if i not in indexes]
        if not a_list:
            break

    print(f'Получилось {len(best_containers)} контейнеров:')
    for container in best_containers:
        print(container)


random_list = [random.uniform(0, 0.004) for i in range(1000)]
run_generations(random_list)

