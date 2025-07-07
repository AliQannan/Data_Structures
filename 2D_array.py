import ctypes
class DynamicArray : 
    def __init__(self): 
        self._n =0 
        self._capacity =1
        self._arr = self._make_array(self._capacity)

    """create darray"""
    def _make_array(self, c) : 
        return (c* ctypes.py_object)()
    """add values """
    def append(self , obj:object)->None: 
        if self._n == self._capacity: 
            self.resize(2*self._capacity)
        self._arr[self._n] = obj
        self._n +=1
    """resize my array"""
    def resize(self, c) : 
        B = self._make_array(c) 
        for k in range(self._n): 
            B[k] = self._arr[k]
        self._arr = B 
        self._capacity =c 
    """delete spacific value"""
    def delete (self ,index :int)->None: 
        if not 0 <= index < self._n : 
            raise IndexError ('invalid index')
        for k in range(index ,self._n-1 ) : 
            self._arr[k] = self._arr[k+1]
        self._arr[self._n -1] = None
        self._n -=1
        """search or find value"""
    def search (self, value) : 
        for k in range(self._n) : 
            if self._arr[k] == value :
                return k
        return -1 
    """size of array"""
    def __len__ (self) : 
        return self._n 
    """set item"""
    def  __setitem__(self , index ,value) : 
        if not 0 <= index < self._n : 
            raise IndexError
        self._arr[index ] =value
    """get item"""
    def __getitem__ (self, index) : 
        if not 0 <= index < self._n : 
            raise IndexError ("invalid index" )
        return self._arr[index]
    """display entier object"""
    def __str__ (self) : 
        return str([self._arr[k] for k in range(self._n)])
     




array = DynamicArray() 
array.append(1)
array.append([1,2,3,34,23,4,234])
print(array)
print(len(array))
print(array[1])

array[1] = 'array'
print(array)

