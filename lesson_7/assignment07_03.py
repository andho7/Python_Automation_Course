# Згенерувати, за допомогою list comprehension, послідовність
# цілих чисел 0..N де будуть відсутні кожний  K-ий елемент
#
# N, K запитати у користувача
# K повинно бути менша за N (строго), дозволити ввод К більшого
# за N але відмасштабувати його до розмірів менших за N (%)
#
# підказка:
#  %= N  # compound assignment

N = 14
K = 4
print(K%N)

a = [value for value in (range(N + 1))if value not in range(N + 1)[K % N -1::K % N]]
print(a)

c = list(range(N + 1))
del c[K % N -1::K % N]
print(c)
