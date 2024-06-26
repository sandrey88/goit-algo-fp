# goit-algo-fp
Final project

**Завдання 1. Структури даних. Сортування. Робота з однозв'язним списком**
======================================================================================
**Тестові результати**
--------------------------------------------------------------------------------------

Заданий список:
15 10 5 20 25 

Реверсований список:
25 20 5 10 15 

Відсортований список (Список 1):
5 10 15 20 25 

Додатковий відсортований список (Список 2):
1 2 3 4 26 27 28 29 30 

**************************************************************************************
**************************************************************************************

**Завдання 2. Рекурсія. Створення фрактала “дерево Піфагора” за допомогою рекурсії**
======================================================================================
**Тестовий результат**
--------------------------------------------------------------------------------------

![Pythagoras tree](images/pythagoras-tree.jpg)

Рівень рекурсії: 8

**************************************************************************************
**************************************************************************************

**Завдання 3. Дерева, алгоритм Дейкстри**
======================================================================================
**Тестовий результат**
--------------------------------------------------------------------------------------

Візуалізація зваженого графу
![Weighted graph](images/graph.png)

Візуалізація найкоротшого шляху від вершини 0 до вершини 4
![An example of the shortest path](images/nodes-path-0-4.png)

**Найкоротші шляхи від вершини 0 до інших вершин**

* Найкоротший шлях від 0 до 0: 0
* Найкоротший шлях від 0 до 2: 3
* Найкоротший шлях від 0 до 1: 4
* Найкоротший шлях від 0 до 3: 9
* Найкоротший шлях від 0 до 4: 5

**************************************************************************************
**************************************************************************************

**Завдання 4. Візуалізація піраміди**
======================================================================================
**Тестовий результат**
--------------------------------------------------------------------------------------

Візуалізація бінарної купи
![Binary heap](images/binary-heap.png)

**************************************************************************************
**************************************************************************************

**Завдання 5. Візуалізація обходу бінарного дерева**
======================================================================================
**Тестовий результат**
--------------------------------------------------------------------------------------

Візуалізація обходу дерева в глибину
![Bypass in depth](images/depth.png)

Візуалізація обходу дерева в ширину
![Bypass in breadth](images/breadth.png)

**************************************************************************************
**************************************************************************************

**Завдання 6. Жадібні алгоритми та динамічне програмування**
======================================================================================
**Тестові результати**
--------------------------------------------------------------------------------------

1. **Заданий бюджет: 30**

Жадібний алгоритм:

* Вибрані страви: ['cola', 'pepsi']
* Загальна кількість калорій: 320

Динамічне програмування:

* Вибрані страви: ['potato']
* Загальна кількість калорій: 350

2. **Заданий бюджет: 100**

Жадібний алгоритм:

* Вибрані страви: ['cola', 'potato', 'pepsi', 'hot-dog']
* Загальна кількість калорій: 870

Динамічне програмування:

* Вибрані страви: ['potato', 'cola', 'pepsi', 'pizza']
* Загальна кількість калорій: 970

3. **Заданий бюджет: 139**

Жадібний алгоритм:

* Вибрані страви: ['cola', 'potato', 'pepsi', 'hot-dog', 'hamburger']
* Загальна кількість калорій: 1120

Динамічне програмування:

* Вибрані страви: ['potato', 'cola', 'pepsi', 'hot-dog', 'pizza']
* Загальна кількість калорій: 1170

**************************************************************************************
**************************************************************************************

**Завдання 7. Використання методу Монте-Карло**
======================================================================================
**Тестовий результат**
--------------------------------------------------------------------------------------

![Probability plot](images/probability.png)

| Сума | Аналітична ймовірність (%) | Ймовірність за Монте-Карло (%) |
|------|----------------------------|--------------------------------|
|  2   |           2.78             |             2.78               |
|  3   |           5.56             |             5.50               |
|  4   |           8.33             |             8.37               |
|  5   |           11.11            |             11.03              |
|  6   |           13.89            |             13.83              |
|  7   |           16.67            |             16.73              |
|  8   |           13.89            |             14.10              |
|  9   |           11.11            |             11.00              |
|  10  |           8.33             |             8.31               |
|  11  |           5.56             |             5.57               |
|  12  |           2.78             |             2.79               |

**Висновки**

* Результати, отримані за допомогою методу Монте-Карло, дуже близькі до аналітичних розрахунків ймовірності випадання кожної суми при киданні двох кубиків. Розбіжності між двома наборами даних мінімальні, що свідчить про високу точність методу Монте-Карло в цьому випадку (100000 кидків кубиків).

* Метод Монте-Карло може бути ефективним інструментом для моделювання ймовірностей у широкому спектрі задач.
