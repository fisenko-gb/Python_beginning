# 07. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def proverka(x, y, z):
    print(f"¬({x} ⋁ {y} ⋁ {z}) = ¬{x} ⋀ ¬{y} ⋀ ¬{z} is {(not (x or y or z)) == (not x and not y and not z)}")
    return (not (x or y or z)) == (not x and not y and not z)

if (proverka(0, 0, 0) and proverka(0, 0, 1) and proverka(0, 1, 0) and 
proverka(0, 1, 1) and proverka(1, 0, 0) and proverka(1, 0, 1) and
proverka(1, 1, 0) and proverka(1, 1, 1)):
    print("Утверждение истинно")
else:
    print("Утверждение ложно")