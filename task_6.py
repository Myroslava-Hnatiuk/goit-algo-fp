# Adjusting the code to use a dictionary for items instead of a list of tuples.

# Define the items with their cost and calorie value.
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}


# Greedy approach
def greedy_algorithm(items, budget):
    total_calories = 0
    remaining_budget = budget
    chosen_items = []
    sortred_items = sorted(items.items(), key=lambda x: x[1]["calories"], reverse=True)
    for item, details in sortred_items:
        if details["cost"] <= remaining_budget:
            total_calories += details["calories"]
            remaining_budget -= details["cost"]
            chosen_items.append(item)

    return total_calories, budget - remaining_budget, chosen_items


# Dynamic Programming approach
def dynamic_programming(items, budget):
    item_names = list(items.keys())
    n = len(item_names)

    # Створюємо таблицю динамічного програмування
    dp_table = [
        [0 for x in range(budget + 1)]
        for y in range(n + 1)
    ]

    # Побудова таблиці
    for i in range(1, n + 1):
        name = item_names[i - 1]
        cost = items[name]["cost"]
        calories = items[name]["calories"]

        for current_budget in range(budget + 1):

            # Якщо страва не поміщається в бюджет
            if cost > current_budget:
                dp_table[i][current_budget] = dp_table[i - 1][current_budget]

            else:
                # Порівнюємо варіант із додаванням страви
                # та варіант без її додавання
                dp_table[i][current_budget] = max(
                    dp_table[i - 1][current_budget],
                    dp_table[i - 1][current_budget - cost] + calories
                )

    # Відновлення оптимального набору страв
    chosen_items = []
    temp_budget = budget

    for i in range(n, 0, -1):
        if dp_table[i][temp_budget] != dp_table[i - 1][temp_budget]:

            name = item_names[i - 1]
            chosen_items.append(name)

            temp_budget -= items[name]["cost"]

    chosen_items.reverse()
    return dp_table[n][budget], budget - temp_budget, chosen_items



if __name__ == '__main__':
    # Execute both algorithms
    budget = 100

    greedy_result = greedy_algorithm(items, budget)
    dp_result = dynamic_programming(items, budget)

    print(greedy_result, dp_result)
