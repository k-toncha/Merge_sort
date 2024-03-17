
def merge(a : list, b : list):
    res_mass = []
    i = 0  # указатель 1 списка
    j = 0  # указатель 2 списка

    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            res_mass.append(a[i])
            i = i + 1
        else:
            res_mass.append(b[j])
            j = j + 1

    while i < len(a):  # проверка остатка 1 списка
        res_mass.append(a[i])
        i = i + 1

    while j < len(b):  # проверка остатка 2 списка
        res_mass.append(b[j])
        j = j + 1

    return res_mass

def merge_sort(s):

    if len(s) == 1:  # условие выхода из рекурсии
        return s

    middle = len(s) // 2  # индекс середины списка

    #рекурсивный вызов merge_sort
    left = merge_sort(s[:middle])
    right = merge_sort(s[middle:])

    return merge(left, right)


if __name__ == "__main__":

    a = [-1, 0, 56, 66, 3, 2, 2, 3, 63, 9]

    print(merge_sort(a))






