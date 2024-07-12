from math import ceil


def calc_runes(level):
    term_1 = 0.02 * (level ** 3)
    term_2 = 3.06 * (level ** 2)
    term_3 = 105.6 * level
    return ceil(term_1 + term_2 + term_3 - 895)


initial_level = int(input('Enter the initial level: '))

while initial_level <= 0:
    initial_level = int(input('Enter valid level: '))

final_level = int(input('Enter the final level: '))

while final_level <= 0:
    final_level = int(input('Enter valid level: '))

total_runes = 0
for level in range(initial_level + 1, final_level + 1):
    total_runes += calc_runes(level)

print(f'Total runes: {total_runes}')
print(f"Total time: {total_runes/110000:.2f} min")
