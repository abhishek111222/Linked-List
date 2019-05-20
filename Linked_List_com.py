class Node:
    def __init__(self, data):
        self.data = data
        self.link = None

class LinkedList:
    def __init__(self):
        self.head = None

    def create_list(self):
        n = int(input('Enter the size of the List : '))
        if n == 0:
            print('The list is Empty')
            return
        else:
            p = self.head
            for i in range(n):
                data = int(input('Print the number to be inserted : '))
                self.insert_at_the_end(data)

    def insert_at_the_end(self, data):
        temp = Node(data)
        if self.head is None:
            self.head = temp
            return
        else:
            p = self.head
            while p.link is not None:
                p = p.link
            p.link = temp

    def display_list(self):
        if self.head is None:
            print('The list is Empty')
        else:
            p = self.head
            print('The List Is : ')
            while p is not None:
                print(p.data, " ", end = " ")
                p =  p.link
        print()

    def insert_at_the_beginning(self,data):
        temp = Node(data)
        temp.link = self.head
        self.head = temp

    def Search(self,x):
        if self.head is None:
            print('The List is Empty')
            return
        else:
            p = self.head
            pos = 1
            while p.link is not None:
                if p.data == x:
                    print(x, " is at the position : ", pos)
                    return
                p = p.link
                pos = pos + 1
            else:
                print('The number is not in the List')

    def Successor(self,x):
        if self.head is None:
            print('The List is Empty')
        else:
            p = self.head
            while p.link is not None:
                if p.data == x:
                    print('The Successor of', x, ' is ', p.link.data)
                    return
                p = p.link
            else:
                p = self.head
                while p.link is not None:
                    p = p.link
                if p.data == x:
                    print('The number is the last number...thus no Successor')
                else:
                    print('The number is not in the List')

    def predecessor(self,x):
        if self.head is None:
            print('The List is Empty')
        else:
            p = self.head
            while p.link is not None:
                if p.link.data == x:
                    print('The predecessor of', x,' is ',p.data)
                    return
                p = p.link
            else:
                p = self.head
                if p.data == x:
                    print('The number is the First Number...thus no predecessor')
                else:
                    print('The number is not in the list')

    def last_node(self):
        if self.head is None:
            print('The list is Empty')
        else:
            p = self.head
            while p.link is not None:
                p = p.link
            print('The last Node is', p.data)

    def first_node(self):
        if self.head is None:
            print('The list is Empty')
        else:
            p = self.head
            print('The first node is ', p.data)

    def node_at_particular_position(self, pos):
        if self.head is None:
            print('The List is Empty')
        else:
            p = self.head
            for i in range(pos-1):
                p = p.link
            print('The node at position ',pos, 'is ',p.data)

    def insert_before_the_given_positio(self,pos,x):
        temp = Node(x)
        if self.head is None:
            print('The list is Empty')
        else:
            p = self.head
            for i in range(pos-1):
                p = p.link
            temp.link = self.head
            self.head = temp

    def insert_after_the_given_pos(self,pos,x):
        temp = Node(x)
        if self.head is None:
            print("The List is Empty")
        else:
            p = self.head
            for i in range(pos-1):
                p = p.link
            temp.link = p.link
            p.link = temp

    def count_nodes(self):
        if self.head is None:
            print('The Node is Empty')
        else:
            p = self.head
            count = 0
            while p is not None:
                p = p.link
                count = count + 1
            print('The number of Nodes in the List is : ',count)

    def deletion_of_the_first_node(self):
        if self.head is None:
            print("The List is Empty")
        else:
            self.head = self.head.link

    def deletion_of_the_last_node(self):
        if self.head is None:
            print("The List is Empty")
        else:
            p = self.head
            while p.link.link is not None:
                p = p.link
            p.link = None

    def reversing_list(self):
        if self.head is None:
            print("The List is Empty")
        else:
            prev  = None
            p = self.head
            while p is not None:
                next = p.link
                p.link = prev
                prev = p
                p = next
            self.head = prev




list = LinkedList()
list.create_list()

print()
print("1. Display List")
print("2. Insert at the End")
print("3. Insert at the Beginning")
print("4. Search")
print("5. Successor")
print("6. Predecessor")
print("7. Last Node")
print("8. First Node")
print("9. The Node at Particuar Position")
print("10. Insert before the Given Position")
print("11. Insert after the Given Position")
print("12. Count the number of Nodes")
print("13. Deletion of the First Node")
print("14. Deletion of the Last Node")
print("15. Deletion In The Between")
print("16. Reversing the List")

while True:
    choice = int(input("Enter your Choice : "))
    if choice == 1:
        list.display_list()
    elif choice == 2:
        data = int(input('What number you want to Insert : '))
        list.insert_at_the_end(data)
    elif choice == 3:
        data = int(input('What number you want to Insert : '))
        list.insert_at_the_beginning(data)
    elif choice == 4:
        data = int(input('Enter the Element you want to Search : '))
        list.Search(data)
    elif choice == 5:
        data = int(input('Enter the elemenet of which you want to know the Successor'))
        list.Successor(data)
    elif choice == 6:
        data = int(input("Enter the elemenet of which you want to know the Predecessor"))
        list.predecessor(data)
    elif choice == 7:
        list.last_node()
    elif choice == 8:
        list.first_node()
    elif choice == 9:
        pos = int(input('Enter the poition of the Node you want to know : '))
        list.node_at_particular_position(pos)
    elif choice == 10:
        pos = int(input('Enter the position before you want to Insert the Node : '))
        x = int(input('Enter the Value : '))
        list.insert_before_the_given_positio(pos,x)
    elif choice == 11:
        pos = int(input('Enter the position after you want to Insert the Node : '))
        x = int(input('Enter the Value : '))
        list.insert_after_the_given_pos(pos,x)
    elif choice == 12:
        list.count_nodes()
    elif choice == 13:
        list.deletion_of_the_first_node()
    elif choice == 14:
        list.deletion_of_the_last_node()
    elif choice == 15:
        pos = int(input("Enter the Position of the number you want to delete : "))
        list.deletion_in_between(pos)
    elif choice == 16:
        list.reversing_list()
    else:
        print("Exit")
        break
