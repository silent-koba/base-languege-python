import sys
def zarplata(x,y,z):
    result = int(x) * int(y) + (int(x) * int(y) * int(z) / 100)
    return result

if 'help' in sys.argv or 'h' in sys.argv:
    print('Введите выработку в часах, ставку в час и размер премии в % .')
else:
    _, hour, bet, bonus = sys.argv
    print(zarplata(hour, bet, bonus))