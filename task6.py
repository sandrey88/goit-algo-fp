"""
Завдання 6. Жадібні алгоритми та динамічне програмування

"""

items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

def greedy_algorithm(items, budget):
    # Створення списку страв з їхніми співвідношеннями калорій до вартості
    items_ratio = [(name, data['cost'], data['calories'], data['calories'] / data['cost']) for name, data in items.items()]
    # Сортування страв за співвідношенням калорій до вартості в спадному порядку
    items_ratio.sort(key=lambda x: x[3], reverse=True)
    
    total_cost = 0
    total_calories = 0
    selected_items = []
    
    for name, cost, calories, ratio in items_ratio:
        if total_cost + cost <= budget:
            selected_items.append(name)
            total_cost += cost
            total_calories += calories
    
    return selected_items, total_calories

def dynamic_programming(items, budget):
    n = len(items)
    item_list = list(items.keys())
    cost = [items[item]["cost"] for item in item_list]
    calories = [items[item]["calories"] for item in item_list]
    
    # Створення DP таблиці
    dp = [[0] * (budget + 1) for _ in range(n + 1)]
    
    # Заповнення DP таблиці
    for i in range(1, n + 1):
        for w in range(1, budget + 1):
            if cost[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - cost[i - 1]] + calories[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]
    
    # Відновлення вибраних предметів
    selected_items = []
    w = budget
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(item_list[i - 1])
            w -= cost[i - 1]
    
    return selected_items, dp[n][budget]

while True:
    budget = int(input("\nЗадайте бюджет (від 10 до 180): "))

    # Перевірка бюджету в межах діапазону
    if 10 <= budget <= 180:
        # Жадібний алгоритм
        selected_items_greedy, total_calories_greedy = greedy_algorithm(items, budget)
        print("\nЖадібний алгоритм:")
        print("Вибрані страви:", selected_items_greedy)
        print("Загальна кількість калорій:", total_calories_greedy)

        # Динамічне програмування
        selected_items_dp, total_calories_dp = dynamic_programming(items, budget)
        print("\nДинамічне програмування:")
        print("Вибрані страви:", selected_items_dp)
        print("Загальна кількість калорій:", total_calories_dp)
        break
    else:
        print("Вказаний бюджет не знаходиться у зазначеному діапазоні.")
