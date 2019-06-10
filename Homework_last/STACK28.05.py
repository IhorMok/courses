# ==============================================
# Уточнення, стек має мати такий функціонал як добавляння, видалення у стек, провірку чи він порожній та мати атрибут, який містить глибину стека. Постійний розмір.  *Підсказка: придивіться до такого типу данних у пайтоні як список

# append
# pop
# empty
# depth

class Stack:
    stack_number = [1, 2, 3]
    counter = 0

    def __init__(self, elements=[], depth=5):
        self.stack_number = self.stack_number + elements
        self.depth = depth  # Глубина стека

    def pop(self):
        return self.stack_number.pop()  # Для удаления и возврата  элемента стека

    def isEmpty(self):  # Проверяем полный ли стек или нет
        return len(self.stack_number) == 0

    def append(self, elements):  # Проверяем глубину стека
        if len(self.stack_number) < self.depth:
            self.stack_number.append(elements)
            return self.stack_number
        else:
            raise Exception('Стек переполненный element не добавленный')


mystack = Stack()
print(mystack.append(4))
print(mystack.append(5))
print(mystack.isEmpty())
print(mystack.pop())

# try:
#   assert type(mystack) == Stack
#   assert mystack.stack_number == [1, 2, 3]
#   assert mystack.isEmpty() == False
#   assert mystack.pop()
#   assert mystack.stack_number == [1, 2]
#   assert mystack.pop()
#   assert mystack.pop()
#   assert mystack.stack_number == []
#   assert mystack.isEmpty() == True
#   assert mystack.append(6) == [6]
#   assert mystack.stack_number == [6]
#   assert mystack.depth == 5
#   mystack.append(5)
#   mystack.append(4)
#   mystack.append(3)
#   mystack.append(2)
#   assert len(mystack.stack_number) == 5
#   mystack.append(1) # Тут функция append добавляем элемент
#   #mystack.append(1)  # ignore 6th element
#   assert len(mystack.stack_number) == 5
#   assert mystack.stack_number == [6, 5, 4, 3, 2]
# except Exception as e:
#   print(e)
