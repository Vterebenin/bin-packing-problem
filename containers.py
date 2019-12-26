import random


class Container(object):
    """ Контейнер с сохранением его суммы """
    def __init__(self):
        self.items = []
        self.sum = 0

    def append(self, item):
        self.items.append(item)
        self.sum += item

    def __str__(self):
        """ Представление для печати """
        return 'Контейнер(сумма=%s, предметы=%s)' % (self.sum, str(self.items))


def pack(values, max_value):
    values = sorted(values, reverse=True)
    containers = []

    for item in values:
        # Попытка влезть в контейнер
        for container in containers:
            if container.sum + item <= max_value:
                container.append(item)
                break
        else:
            # Предмет не влез ни в 1 контейнер, создаем новый контейнер
            container = Container()
            container.append(item)
            containers.append(container)
    return containers


def pack_and_show(a_list, max_value):
    """ Упаковать предметы в контейнеры и показать результат """
    print(f'Список с суммой {sum(a_list)} требует минимально {(sum(a_list)+max_value-1)/max_value} контейнеров')

    containers = pack(a_list, max_value)

    print(f'Решение получено, необходимо контейнеров -- {len(containers)}')
    for container in containers:
        print(container)


random_list = [random.uniform(0, 1) for i in range(100)]
pack_and_show(random_list, 1)

non_random_list = [0.1, 0.3, 0.4, 0.7, 0.2, 0.1]
pack_and_show(non_random_list, 1)
