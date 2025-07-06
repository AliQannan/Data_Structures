import ctypes
class Dynamic: 
    def __init__(self):
        self._n = 0 
        self._capacity =1
        self._A = self._make_array(self._capacity)
    def _make_array (self, c) : 
        """انشاء مصفوفة في الذاكرة"""
        return  (c * ctypes.py_object)()
    def append(self, obj) : 
        """أضافة العنصر في نهاية المصفوفة"""
        if self._n == self._capacity: 
            self.resize(2*self._capacity)
        self._A[self._n] = obj
        self._n +=1
    def resize(self ,c) : 
        """توسيع المصفوفة عند الحاجة"""
        B =self._make_array(c)
        for k in range(self._n): 
            B[k] =self._A[k]
        self._A = B 
        self._capacity =c
    def delete (self, index) : 
        """حذف عنصر معين"""
        if not 0 <= index < self._n : 
            raise IndexError("index out of range")
        for i in range(index ,self._n-1):
            self._A[i]=self._A[i+1]
        self._A[self._n -1] = None 
        self._n -=1
    def __getitem__ (self, index) : 
        if not 0 <= index < self._n : 
            raise IndexError("index out of range")
    def __setitem__(self, index, value):
        """تحديث عنصر معين"""
        if not 0 <= index < self._n: 
            raise IndexError("index out of range")
        self._A[index] = value


    def search (self ,value) : 
        """البحث عن عناصر"""
        for i in range(self._n) : 
            if self._A[i] == value : 
                return i 
        return -1
    
    def __len__(self) : 
        """عدد العناصر"""
        return self._n 
    def __str__(self):
        """عرض العناصر مع دعم الكائنات المتداخلة"""
        result = []
        for i in range(self._n):
            if isinstance(self._A[i], Dynamic):
                result.append(str(self._A[i]))  # طباعة المصفوفة بداخل مصفوفة
            else:
                result.append(str(self._A[i]))
        return str(result)

    



array = Dynamic()


array.append('ali')
array.append('mofida')
array.append('mofida')
array.append('salma')


print(len(array))
array.delete(1)
array.append('ali')
array[0] = 'ahmed'
array[1] = 'ibrhem qannan'


array2 = Dynamic()
array2.append([x for x in range(100)])


array.append(array2)
print(array)