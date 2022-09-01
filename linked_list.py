class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

# A wrapper to help keep track of the head of a linked list
class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None

    # visualize linked list
    def print_ll(self):
        ll_string = ""
        node = self.head

        if node is None: # linked list is empty
            print(None)
        while node:
            ll_string += f" {str(node.data)} ->"
            node = node.next_node
        
        ll_string += " None"
        print(ll_string)
    
    def insert_beginning(self, data):
        if self.head is None:
            self.head = Node(data, None)
            self.last_node = self.head
        else:
            new_node = Node(data, self.head)
            self.head = new_node

    def insert_at_end(self, data):
        if self.head is None:
            self.insert_beginning(data)
        
        self.last_node.next_node = Node(data, None)
        self.last_node = self.last_node.next_node

    def to_list(self):
        lst = []
        if self.head is None:
            return lst

        node = self.head
        while node:
            lst.append(node.data)
            node = node.next_node
        return lst

    def get_user_by_id(self, user_id):
        node = self.head
        while node:
            if node.data["id"] is int(user_id):
                return node.data
            node = node.next_node
        return None

