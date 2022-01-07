class Node:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = data

    def get_next(self):
        return self.__next

    def set_next(self, next_node):
        self.__next = next_node


class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None

    def get_head(self):
        return self.__head

    def get_tail(self):
        return self.__tail

    def add(self, data):
        new_node = Node(data)
        if (self.__head is None):
            self.__head = self.__tail = new_node
        else:
            self.__tail.set_next(new_node)
            self.__tail = new_node

    def display(self):
        temp = self.__head
        while (temp is not None):
            print(temp.get_data())
            temp = temp.get_next()


    def find_node(self, data):
        # Remove pass and write the logic to find the node and return the node if found or return None.
        temp = self.__head
        while(temp is not None):
            if(temp.get_data() == data):
                return data
            temp = temp.get_next()
        return None

    def insert(self, data, data_before):
        # Remove pass and write the logic to insert an element.
        new_node = Node(data)
        if(data_before is None):
            new_node.set_next(self.__head)
            self.__head = new_node
        else:
            if(self.find_node(data_before) is not None):
                node_before = self.__head
                while (node_before.get_data() != data_before):
                    node_before = node_before.get_next()
                new_node.set_next(node_before.get_next())
                node_before.set_next(new_node)
                if (new_node.get_next() is None):
                    self.__tail = new_node
            else:
                print('The node for the given data is not present in the LinkedList')

    def delete(self, data):
        # Remove pass and write the logic to delete an element.
        if(self.find_node(data) is not None):
            if(self.__head == self.__tail):
                self.__head = None
            else:
                if(self.__head.get_data() == data):
                    self.__head = self.__head.get_next()
                    return
                temp = self.__head
                while((temp.get_next()).get_data() != data):
                    temp = temp.get_next()
                deleted_node = temp.get_next()
                temp.set_next(deleted_node.get_next())
                deleted_node = None
        else:
            print('Node not found to delete')







    # You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        temp = self.__head
        msg = []
        while (temp is not None):
            msg.append(str(temp.get_data()))
            temp = temp.get_next()
        msg = " ".join(msg)
        msg = "Linkedlist data(Head to Tail): " + msg
        return msg




list1 = LinkedList()
list1.add('Sugar')
list1.add('Tea')
list1.add('Coffee')
list1.delete('Coffee')
list1.display()
