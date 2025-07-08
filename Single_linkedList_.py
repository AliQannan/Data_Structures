from typing import List
class Node : 
    def __init__(self , val , next = None)->None:
        self.val = val 
        self.next = next
        

class SingleLinkedList: 
    def __init__(self):
        self.head = None
        self.tail = None
    


    def Traversel(self)->List[object] : 
        pointer = self.head
        result = list()
        while pointer : 
            result.append(pointer.val)
            pointer = pointer.next
        return result
    
    def append(self , value:object)->None:
        new_node = Node(value) 
        if not self.head : 
           self.tail = new_node
           return self.preappend(value)
        pointer = self.head
        while pointer.next : 
            pointer = pointer.next
        pointer.next = new_node
        
        self.tail = new_node

    def preappend(self ,value:object)->None: 
        new_node = Node(value)
        if not self.head :
            self.head = new_node
            return 
        new_node.next = self.head
        self.head = new_node
        return
    """ """
    def insert_after(self,key,value:object)->None : 
        new_node = Node(value)
        pointer = self.head 

        while pointer and pointer.val != key : 
            pointer = pointer.next

        temp= pointer.next 
        pointer.next = new_node
        new_node.next = temp
    def insert_before(self,key,value:object)->None : 
        new_node = Node(value)
        pointer = self.head 
        while pointer and pointer.next.val != key : 


            pointer = pointer.next 

        prev = pointer.next
        pointer.next  = new_node
        new_node.next = prev
        
    def remove (self , index:int)->None: 
        if index == 0 : 
            self.head = self.head.next
            return 
        pointer = self.head 

        idx =0 
        while pointer and idx < index : 
            prev = pointer
            pointer = pointer.next 
            idx +=1
       
        prev.next = pointer.next
    
    def delete_by_value (self , value:object)->None : 
        pointer = self.head 
        while pointer and pointer.val != value : 
            prev = pointer
            pointer = pointer.next 
        if not pointer : 
            raise ValueError ("value not found ")
        prev.next = pointer.next


    def pop(self) : 

        pointer = self.head 
        while pointer.next : 
            prev = pointer
            pointer = pointer.next 

        prev.next = None 

    def reverse(self ) : 
        prev = None 
        pointer = self.head 
        while pointer : 
            nex_node = pointer.next # save next node 

            pointer.next = prev # make next pointer (next node = prev node ) 
            prev =  pointer  # make (prev = current node)

            pointer = nex_node # move pointer to move to next node
        self.head = prev # make head prev 
        return prev # return new obj

        


        
        
            
   


slist = SingleLinkedList()

slist.append(1)
slist.append(0)




slist.append(43)
slist.append(123)
slist.append(4)
slist.append(12)
slist.append(4)
slist.append(2)
slist.append(-1)
slist.insert_after(-1,100)
slist.insert_before(-1,300)
print(len(slist.Traversel()))
slist.delete_by_value(43)

# slist.pop()
print(len(slist.Traversel()))
print(slist.Traversel())

slist.reverse()
print(slist.Traversel())

