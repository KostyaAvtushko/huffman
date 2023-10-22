import heapq
from collections import Counter, namedtuple

# Определение класса Node для внутренних узлов дерева Хаффмана
class Node(namedtuple('Node', ['left', 'right'])):
    # Метод для обхода дерева и построения кодов символов
    def walk(self, code, acc):
        self.left.walk(code, acc + '0')  # Проход влево добавляет '0' к текущему коду
        self.right.walk(code, acc + '1') # Проход вправо добавляет '1' к текущему коду

# Определение класса Leaf для листьев дерева Хаффмана
class Leaf(namedtuple('Leaf', ['char'])):
    # Метод для установки кода символа в словаре code
    def walk(self, code, acc):
        code[self.char] = acc or '0'  # Устанавливает код символа в словаре или '0', если пусто

# Функция для кодирования строки методом Хаффмана
def huffman_encode(s):
    h = []
    # Создание списка кортежей (частота, индекс, Leaf(символ)) для каждого символа в строке s
    for ch, freq in Counter(s).items():
        h.append((freq, len(h), Leaf(ch)))
    heapq.heapify(h)  # Преобразование списка в мин-кучу
    count = len(h)
    # Построение дерева Хаффмана
    while len(h) > 1:
        freq1, _count1, left = heapq.heappop(h)
        freq2, _count2, right = heapq.heappop(h)
        # Создание нового узла, объединяя left и right, и добавление его в кучу
        heapq.heappush(h, (freq1 + freq2, count, Node(left, right)))
        count += 1
    code = {}  # Словарь для хранения кодов символов
    if h:
        [(_freq, _count, root)] = h  # Извлечение корня дерева из кучи
        root.walk(code, '')  # Построение кодов символов с помощью метода walk
    return code  # Возвращение словаря с беспрефиксными кодами

# Главная функция программы
def main():
    s = input()  # Ввод строки от пользователя
    code = huffman_encode(s)  # Построение кодов символов для введенной строки
    encoded = ''.join(code[ch] for ch in s)  # Кодирование строки с использованием полученных кодов
    print(len(code), len(encoded))  # Вывод количества уникальных символов и длины закодированной строки
    for ch in sorted(code):
        print('{}: {}'.format(ch, code[ch]))  # Вывод символа и соответствующего ему кода
    print(encoded)  # Вывод закодированной строки

# Проверка, является ли данный файл исполняемым
if __name__ == "__main__":
    main()  # Вызов главной функции программы
