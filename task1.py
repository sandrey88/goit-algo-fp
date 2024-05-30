"""
Завдання 1. Структури даних. Сортування. Робота з однозв'язним списком

"""

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()

    # Реверсування списку
    def reverse_list(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    # Сортування злиттям
    def merge_sort(self):
        self.head = self._merge_sort(self.head)

    def _merge_sort(self, h):
        if h is None or h.next is None:
            return h

        middle = self.get_middle(h)
        next_to_middle = middle.next

        middle.next = None

        left = self._merge_sort(h)
        right = self._merge_sort(next_to_middle)

        sorted_list = self.sorted_merge(left, right)
        return sorted_list

    def get_middle(self, head):
        if head is None:
            return head

        slow = head
        fast = head

        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow

    def sorted_merge(self, a, b):
        result = None

        if a is None:
            return b
        if b is None:
            return a

        if a.data <= b.data:
            result = a
            result.next = self.sorted_merge(a.next, b)
        else:
            result = b
            result.next = self.sorted_merge(a, b.next)

        return result

    # Об'єднання двох відсортованих списків в один відсортований
    def merge_two_sorted_lists(self, llist1, llist2):
        dummy = Node()
        tail = dummy

        while llist1 and llist2:
            if llist1.data <= llist2.data:
                tail.next = llist1
                llist1 = llist1.next
            else:
                tail.next = llist2
                llist2 = llist2.next
            tail = tail.next

        if llist1:
            tail.next = llist1
        elif llist2:
            tail.next = llist2

        return dummy.next

# Створення зв'язного списку та демонстрація функцій
llist = LinkedList()

# Вставка вузлів
llist.insert_at_beginning(5)
llist.insert_at_beginning(10)
llist.insert_at_beginning(15)
llist.insert_at_end(20)
llist.insert_at_end(25)

print("\nЗаданий список:")
llist.print_list()

# Реверсування списку
llist.reverse_list()
print("\nРеверсований список:")
llist.print_list()

# Сортування списку
llist.merge_sort()
print("\nВідсортований список (Список 1):")
llist.print_list()

# Два відсортовані списки для подальшої демострації їх об'єднання
llist1 = llist

llist2 = LinkedList()
llist2.insert_at_end(1)
llist2.insert_at_end(2)
llist2.insert_at_end(3)
llist2.insert_at_end(4)
llist2.insert_at_end(26)
llist2.insert_at_end(27)
llist2.insert_at_end(28)
llist2.insert_at_end(29)
llist2.insert_at_end(30)

print("\nДодатковий відсортований список (Список 2):")
llist2.print_list()

merged_list = LinkedList()
merged_list.head = merged_list.merge_two_sorted_lists(llist1.head, llist2.head)

print("\nОб'єднані списки 1 та 2:")
merged_list.print_list()
print()
