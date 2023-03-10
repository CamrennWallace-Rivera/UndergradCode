# Implementation of an Unordered List ADT as a linked list.  The list
# is accessed through a reference to the first element, head.  
# Adopted from the textbook.

class Node:
    '''
    Create a Node object and initialize its data.  
    '''
    def __init__(self, init_data):
        self.data = init_data
        self.next = None
       
    '''
    Accessor for node data
    '''
    def get_data(self):
        return self.data
    
    '''
    Accessor for next reference
    '''
    def get_next(self):
        return self.next
    
    '''
    Mutator for node data
    '''
    def set_data(self, new_data):
            self.data = new_data
            
    '''
    Mutator for next reference
    '''
    def set_next(self, new_next):
            self.next = new_next   

class OrderedList:
    '''
    List is empty upon creation and the head reference is None
    '''
    def __init__(self):
        self.head = None    
        
    '''
    Returns True if list is empty, False otherwise
    '''
    def is_empty(self):
        return self.head == None 
    
    '''
    Add an element to head of the list
    '''
    def add(self, item):
         # keep track of current and previous elements
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            # if we have a match, stop
            if current.get_data() > item:
                stop = True
            # otherwise advance current and next references
            else:
                previous = current
                current = current.get_next()
           
        # Create a node using item as its data
        temp = Node(item)
        if previous == None:
            temp.set_next(current)
            self.head = temp
                # the element to be deleted is not the head
        else:
            temp.set_next(current)
            previous.set_next(temp)
                       
    '''
    Returns the size of the list
    '''
    def size(self):
        # start at the head of the list
        current = self.head
        count = 0
        # Traverse the list one element at a time.  We know
        # we reached the end when the next reference is None
        while current != None:
            count = count + 1
            current = current.get_next()
        return count

    '''
    Search for an item in the list.  Returns True if found, False otherise.  
    '''
    def search(self,item):
        current = self.head
        found = False
        stop=False
        # As long as the element is not found and we haven't 
        # reached the end of the list
        while current != None and not found and not stop:
            if current.get_data() == item:
                found = True
            else:
                if current.get_data()>item:
                    stop= True
                else:
                    # go to the next element
                    current = current.get_next()
        return found
    
    '''
    Remove the first occurrence of item from the list.  
    '''
    def remove(self, item):
        # keep track of current and previous elements
        current = self.head
        previous = None
        found = False
        # traverse the list 
        while current != None and not found:
            # if we have a match, stop
            if current.get_data() == item:
                found = True
            # otherwise advance current and next references
            else:
                previous = current
                current = current.get_next()
           
        # the element to be deleted is the head of the list     
        if found:
            if previous == None:
                self.head = current.get_next()
                # the element to be deleted is not the head
            else:
                previous.set_next(current.get_next())

    def print_list(self):

        current = self.head
        while(current):
            if(current.next):
                print(current.data,end=",")
            else:
                print(current.data)
            current = current.next

    def index(self,item):

        index=0

        current=self.head

        while current != None:

            if current.get_data()== item:

                 return index

            else:

                index= index+1

                current=current.get_next()
            

    def pop(self):

        previous = None
        current = False

        current=self.head

        while current.get_next() != None:

            previous = current
                
            current=current.get_next()

        previous.set_next(None) 
        return current

    def count(self):

        count=0

        current=self.head

        while current != None:

            current=current.get_next()

            count+=1

        return count


    def duplicate(self):

        items=[]
        unique_items=[]
        current=self.head

        while current != None:

            items.append(current.get_data())

            if current.get_data() not in unique_items:

                unique_items.append(current.get_data())

            current=current.get_next()

        current=self.head

        for item in unique_items:

            current.set_data(item)

            if item!= unique_items[-1]:
                current=current.get_next()

        current.set_next(None)

        return items





    def pop_pos(self,item):

        count=0
        previous=None
        current=self.head

        while current!= None and count != item:

            count +=1
            previous=current
            current=current.get_next()
        else:
            
            previous.set_next(current.get_next())
            return current
        
    

            


        
def main():
  # create a list and add some elements to it
    aList = OrderedList()
    print("Adding 15 random intergers ranging 1-5 to the list.")
    aList.add(1)
    aList.add(2)
    aList.add(3)
    aList.add(5)
    aList.add(1)
    aList.add(2)
    aList.add(3)
    aList.add(5)
    aList.add(1)
    aList.add(2)
    aList.add(3)
    aList.add(5)
    aList.add(1)
    aList.add(2)
    aList.add(3)
    aList.add(5)
    aList.print_list()
    print("the count for the list is:",aList.count())
    print("the popped number is:",aList.pop().get_data())
    print("the count for the list is:",aList.count())
    print("the popped pos is:",aList.pop_pos(2).get_data())
    aList.print_list()
    print("the index of 8 is:",aList.index(5))
    print("the duplicates of the list:",aList.duplicate())
    aList.print_list()
    
    
    
if __name__ == "__main__":
    main()


                 

             
            

            


          


