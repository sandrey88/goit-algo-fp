"""
Завдання 7. Використання методу Монте-Карло

"""

import random
import matplotlib.pyplot as plt

def simulate_dice_rolls(num_rolls):
    # Словник для зберігання кількості з’явлень кожної суми
    sums_count = {i: 0 for i in range(2, 13)}
    
    # Моделювання кидання кубиків num_rolls разів
    for _ in range(num_rolls):
        # Кидання двох кубиків
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        # Обчислення суми чисел на кубиках
        total = dice1 + dice2
        # Збільшення кількості з’явлень цієї суми
        sums_count[total] += 1
    
    # Обчислення ймовірності кожної суми у відсотках
    probabilities = {k: (v / num_rolls) * 100 for k, v in sums_count.items()}
    
    return probabilities

# Кількість кидків кубиків
num_rolls = 100000

# Моделювання кидання кубиків
probabilities = simulate_dice_rolls(num_rolls)

# Підготовка даних для графіку
sums = list(probabilities.keys())
prob_values = list(probabilities.values())

# Побудова графіку
plt.figure(figsize=(10, 6))
plt.bar(sums, prob_values, color='skyblue')
plt.xlabel('Сума')
plt.ylabel('Імовірність (%)')
plt.title('Ймовірність кожної суми при киданні двох кубиків\n(Метод Монте-Карл, 100000 кидків)')
plt.xticks(sums)


# Відображення значень ймовірностей над стовпчиками
for i in range(len(sums)):
    plt.text(sums[i], prob_values[i] + 0.2, f'{prob_values[i]:.2f}%', ha='center', va='bottom')

plt.show()
