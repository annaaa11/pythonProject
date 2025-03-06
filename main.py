# Використовуючи класи з практичної реалізуйте клас Shop з
# трьома чергами до кас. Кожна черга реалізується через
# двозв’язний список
# Атрибути
#  queue1, queue2, queue3 – черги до кас
# Методи
#  add_buyer(name, idx) – додає покупця в кінець черги
# номер idx
#  serve_buyer(idx) – обслуговує покупця з черги
# idx(вивести повідомлення та видалити покупця з черги)
# Якщо черга стала порожньою, то викликати _reorder(idx)
#  _reorder(idx) – з усіх черг останній покупець переходить
# в чергу з номером idx
#  display_info() – виводить на екран 3 черги

class Node:
    def __init__(self, data):
        self.data = data  # Значення вузла
        self.next = None  # Посилання на наступний вузол
        self.prev = None  # Посилання на попередній вузол

    def __str__(self):
        return f"{self.data} -> {self.next}"

#двозв’язний список
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):

            return f"{self.head}"

    def push_end(self, data): #додає new_node в кінець self.tail
        new_node = Node(data)
        if self.head is None: # Перевірка чи список порожній
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    def pop_start(self): # удаляем начало

        if self.head is None:
            print("список порожній")
            return

        if self.head.next is None:
            self.head = None
            self.tail = None
            return

        self.head = self.head.next
        self.head.prev = None

    def pop_end(self): # удаляем последнего

        if self.tail is None:
            print("список порожній")
            return
        if self.tail.prev is None: # 1 node
            self.head = None
            self.tail = None
            return

        self.tail = self.tail.prev
        self.tail.next = None

class Shop:
    def __init__(self):
       # queue1, queue2, queue3 – черги         до         кас
        self.queue1 = DoublyLinkedList()
        self.queue2 = DoublyLinkedList()
        self.queue3 = DoublyLinkedList()

    def display_info(self):

        print(f"черга 1: {self.queue1}")
        print(f"черга 2: {self.queue2}")
        print(f"черга 3: {self.queue3}")


    def add_buyer(self, name, idx):
        if idx == 1:
            self.queue1.push_end(name)
        elif idx == 2:
            self.queue2.push_end(name)
        elif idx == 3:
            self.queue3.push_end(name)
        else:
            print("черги до кас: 1,2,3!")

    def _reorder(self, idx): # з усіх черг останній покупець переходить
# в чергу з номером idx
        last_buyer = None
        for queue in [self.queue3, self.queue2, self.queue1]:
            if queue.tail:
                last_buyer = queue.tail
                queue.pop_end()
                #print(last_buyer)
                break

        if last_buyer:
            self.add_buyer(last_buyer, idx)

    def serve_buyer(self, idx): #oбслуговує покупця з черги idx
        if idx == 1:
            if self.queue1.head:
                print(f"oбслуговує покупця {self.queue1.head.data} з черги1")
                self.queue1.pop_start() # видалити покупця з черги
                if self.queue1.head is None: # Якщо черга стала порожньою, то викликати _reorder(idx)
                    self._reorder(1)
        elif idx == 2:
            if self.queue2.head:
                print(f"oбслуговує покупця {self.queue2.head.data} з черги2")
                self.queue2.pop_start()
                if not self.queue2.head:
                    self._reorder(2)
        elif idx == 3:
            if self.queue3.head:
                print(f"oбслуговує покупця {self.queue3.head.data} з черги3")
                self.queue3.pop_start()
                if not self.queue3.head:
                    self._reorder(3)
        else:
            print("черги до кас: 1,2,3!")

# Приклад використання
shop = Shop()
shop.add_buyer("Олег", 1)
shop.add_buyer("Марина", 2)
shop.add_buyer("Марія", 2)
shop.add_buyer("Андрій", 3)
shop.add_buyer("Ірина", 1)
shop.add_buyer("Василь", 2)
shop.add_buyer("Тетяна", 3)
shop.add_buyer("Сергій", 3)
shop.add_buyer("Анна", 3)
print("Черги:")
shop. display_info()

shop.serve_buyer(1)
shop.serve_buyer(2)
shop.serve_buyer(3)
print("Після обслуговування покупців:")
shop. display_info()

shop.serve_buyer(1)
print("Покупці перейшли до вільної каси:")
shop.display_info()

