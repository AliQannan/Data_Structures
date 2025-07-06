import ctypes

class DynamicArray:
    def __init__(self):
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)

    def _make_array(self, c):
        """إنشاء مصفوفة من الذاكرة"""
        return (c * ctypes.py_object)()

    def append(self, obj):
        """إضافة عنصر في نهاية المصفوفة"""
        if self._n == self._capacity:
            self.resize(2 * self._capacity)
        self._A[self._n] = obj
        self._n += 1

    def resize(self, c):
        """توسيع المصفوفة عند الحاجة"""
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c

    def delete(self, index):
        """حذف عنصر من موقع معين"""
        if not 0 <= index < self._n:
            raise IndexError("Index out of bounds")
        for i in range(index, self._n - 1):
            self._A[i] = self._A[i + 1]
        self._A[self._n - 1] = None
        self._n -= 1

    def update(self, index, value):
        """تحديث قيمة عنصر موجود"""
        if not 0 <= index < self._n:
            raise IndexError("Index out of bounds")
        self._A[index] = value

    def get(self, index):
        """الوصول إلى عنصر"""
        if not 0 <= index < self._n:
            raise IndexError("Index out of bounds")
        return self._A[index]

    def search(self, target):
        """البحث الخطي عن عنصر"""
        for i in range(self._n):
            if self._A[i] == target:
                return i
        return -1

    def __len__(self):
        return self._n

    def display(self):
        print([self._A[i] for i in range(self._n)])


# === استخدام الكلاس ===
da = DynamicArray()
da.append(10)
da.append(20)
da.append(30)
da.display()  # [10, 20, 30]
print("Index of 20:", da.search(20))  # 1
da.update(1, 25)
da.delete(0)
da.display()  # [25, 30]
