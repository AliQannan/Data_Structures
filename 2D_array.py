class TwoDArray:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.array = [[None for _ in range(cols)] for _ in range(rows)]

    def set(self, row, col, value):
        """وضع قيمة في موقع معين"""
        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.array[row][col] = value
        else:
            raise IndexError("Row or Column out of bounds")

    def get(self, row, col):
        """الوصول إلى عنصر"""
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return self.array[row][col]
        else:
            raise IndexError("Row or Column out of bounds")

    def search(self, target):
        """البحث عن قيمة عبر الصفوف والأعمدة"""
        for r in range(self.rows):
            for c in range(self.cols):
                if self.array[r][c] == target:
                    return (r, c)
        return (-1, -1)

    def display(self):
        """عرض المصفوفة"""
        for row in self.array:
            print(row)


# === استخدام الكلاس ===
tda = TwoDArray(3, 3)
tda.set(0, 0, 1)
tda.set(1, 1, 2)
tda.set(2, 2, 3)
tda.display()
print("Search 2 at position:", tda.search(2))
