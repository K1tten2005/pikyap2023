import sys
import math

def get_koeff(index):
    if index == 1:
        letter = 'A'
    elif index == 2:
        letter = 'B'
    else:
        letter = 'C'
    try:
        koeff_str = sys.argv[index]
    except:
        while True:
            print('Введите коэффициент {}: '.format(letter))
            koeff_str = input()
            try:
                koeff = float(koeff_str)
                return koeff
            except ValueError:
                print('Введено неверное значение. Попробуйте снова.\n')

def get_roots(a, b, c):
    result = []
    D = b* b - 4 * a * c
    if D == 0.0:
        root = math.sqrt(-b / (2.0 * a))
        if (root == 0.0):
            result.append(abs(root))
        else:
            result.append(root)
            result.append(-root)
    elif D > 0.0:
        sqD = math.sqrt(D)
        r1 = (-b + sqD) / (2.0 * a)
        r2 = (-b - sqD) / (2.0 * a)
        if r1 == 0.0:
            result.append(r1)
        if r2 == 0.0 and r1 != 0.0:
            result.append(r2)
        if r1>0.0:
            root1 = math.sqrt(r1)
            result.append(root1)
            result.append(-root1)
        if r2>0.0:
            root2 = math.sqrt(r2)
            result.append(root2)
            result.append(-root2)
    return result


def main():
    a = get_koeff(1)
    b = get_koeff(2)
    c = get_koeff(3)

    roots = get_roots(a, b, c)

    len_roots = len(roots)
    if len_roots == 0:
        print('Нет корней')
    elif len_roots == 1:
        print('Один корень: {}'.format(roots[0]))
    elif len_roots == 2:
        print('Два корня: {} и {}'.format(roots[0], roots[1]))
    elif len_roots == 3:
        print('Три корня: {}, {} и {}'.format(roots[0], roots[1], roots[2]))
    elif len_roots == 4:
        print('Четыре корня: {}, {}, {} и {}'.format(roots[0], roots[1], roots[2], roots[3]))


# Если сценарий запущен из командной строки
if __name__ == "__main__":
    main()