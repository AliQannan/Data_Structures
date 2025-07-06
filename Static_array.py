class StaticArray:
    def __init__(self, size):
        self.size = size
        self.array = [None] * size

    def set(self, index, value):
        """تحديث أو إدخال عنصر في موقع معين"""
        if 0 <= index < self.size:
            self.array[index] = value
        else:
            raise IndexError("Index out of bounds")

    def get(self, index):
        """الوصول إلى عنصر"""
        if 0 <= index < self.size:
            return self.array[index]
        else:
            raise IndexError("Index out of bounds")

    def linear_search(self, target):
        """البحث الخطي عن عنصر"""
        for i in range(self.size):
            if self.array[i] == target:
                return i
        return -1

    def delete(self, index):
        """حذف عنصر من خلال استبداله بـ None"""
        if 0 <= index < self.size:
            self.array[index] = None
        else:
            raise IndexError("Index out of bounds")

    def display(self):
        print(self.array)


# === استخدام الكلاس ===
sa = StaticArray(5)
sa.set(0, 10)
sa.set(1, 20)
sa.display()  # [10, 20, None, None, None]
sa.delete(0)
print("After deletion:", sa.get(0))  # None
