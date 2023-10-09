import itertools

def has_element(tuple: tuple, elements: list) -> bool:
    for element in elements:
        if element in tuple:
            return True
    return False

def get_elements_in_tuples(tuple_list: list) -> tuple:
    return (element for tuple in tuple_list for element in tuple)

def is_valid(pair: tuple, combination: list) -> bool:
    elementos = get_elements_in_tuples(combination)
    return not has_element(pair, elementos)

def find_combinations(numbers: tuple) -> list:

    # se obtiene la lista de parejas de combinaciones posibles de la entrada incial de números
    # por ejemplo: para la entrada (1,2,3,4) se obtendría:
    #       [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
    # por ejemplo: para la entrada (1,2,3,4,5,6) se obtendría:
    #       [(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 3), (2, 4), (2, 5), (2, 6), (3, 4),
    #       (3, 5), (3, 6), (4, 5), (4, 6), (5, 6)]
    pairs = list(itertools.combinations(numbers, 2))

    # FUNCION RECURSIVA
    def find_combination(start: int, target_long: int, combination: list) -> list:

        # combinacion encontrada
        if target_long == 0:
            combinations.append(combination[:])
            print(str(len(combinations))+": "+str(combination))
            return

        # no hay combinacion
        if start == len(pairs):
            return

        # backtrack
        for index in range(start, len(pairs)):

            if not is_valid(pairs[index], combination):
                continue

            if index > start and pairs[index] == pairs[index - 1]:
                continue

            combination.append(pairs[index])
            find_combination(index + 1, target_long - 1, combination)
            combination.pop()

    combinations = []
    find_combination(0, len(numbers) / 2, [])
    return combinations


numbers = (1,2,3,4,5,6,7,8)
find_combinations(numbers)
