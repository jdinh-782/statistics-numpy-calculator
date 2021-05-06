import numpy as np


def calculate(list):
    if len(list) < 9:
        print("list must only have 9 elements")
        raise ValueError

    """
        return: dictionary in following format...
        {
            'mean': [axis1, axis2, flattened],
            'variance': [axis1, axis2, flattened],
            'standard deviation': [axis1, axis2, flattened],
            'max': [axis1, axis2, flattened],
            'min': [axis1, axis2, flattened],
            'sum': [axis1, axis2, flattened]
        }
    """

    matrix = [[], [], []]
    index = 0

    for i in range(0, len(list)):
        matrix[index].append(list[i])
        if len(matrix[index]) == 3:
            index += 1

    # copy list to matrix
    matrix = np.copy(matrix)
    # print(matrix)

    calculations = dict()
    calculation_list = [[], [], []]

    # convert numpy arrays to floats
    # mean
    for i in np.nditer(matrix.mean(0)):
        calculation_list[0].append(float(i))

    for i in np.nditer(matrix.mean(1)):
        calculation_list[1].append(float(i))

    calculation_list[2] = float(matrix.mean())

    calculations['mean'] = calculation_list
    calculation_list = [[], [], []]

    # variance
    for i in np.nditer(matrix.var(0)):
        calculation_list[0].append(float(i))

    for i in np.nditer(matrix.var(1)):
        calculation_list[1].append(float(i))

    calculation_list[2] = float(matrix.var())

    calculations['variance'] = calculation_list
    calculation_list = [[], [], []]

    # standard deviation
    for i in np.nditer(matrix.std(0)):
        calculation_list[0].append(float(i))

    for i in np.nditer(matrix.std(1)):
        calculation_list[1].append(float(i))

    calculation_list[2] = float(matrix.std())

    calculations['standard deviation'] = calculation_list
    calculation_list = [[], [], []]

    # max
    for i in np.nditer(np.amax(matrix, axis=0)):
        calculation_list[0].append(int(i))

    for i in np.nditer(np.amax(matrix, axis=1)):
        calculation_list[1].append(int(i))

    calculation_list[2] = np.amax(matrix)

    calculations['max'] = calculation_list
    calculation_list = [[], [], []]

    # min
    for i in np.nditer(np.amin(matrix, axis=0)):
        calculation_list[0].append(int(i))

    for i in np.nditer(np.amin(matrix, axis=1)):
        calculation_list[1].append(int(i))

    calculation_list[2] = np.amin(matrix)

    calculations['min'] = calculation_list
    calculation_list = [[], [], []]

    # sum
    for i in np.nditer(matrix.sum(0)):
        calculation_list[0].append(int(i))

    for i in np.nditer(matrix.sum(1)):
        calculation_list[1].append(int(i))

    calculation_list[2] = matrix.sum()

    calculations['sum'] = calculation_list
    calculation_list = [[], [], []]

    # print('\n')
    # for key in calculations:
    #     print(f"{key:>18} : {calculations[key]},")

    return calculations


if __name__ == '__main__':
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    calculate(numbers)
