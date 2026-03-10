class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
node1 = Node(3)
node2 = Node(5)
node3 = Node(13)
node4 = Node(2)

node1.next = node2
node2.next = node3
node3.next = node4

currentNode = node1
while currentNode:
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.next
print("null")

class Linkedlist:
  def __init__(self, data):
      self.data = data
      self.next = None
  
  def insert_at_beginning(self, data):
      new_node = Node(data)
      new_node.next = self.head
      self.head = new_node

  def insert_at_end(self, data):
      new_node = Node(data)
      if self.head is None:
          self.head = new_node
          return
      temp = self.head
      while temp.next:
          temp = temp.next
      temp.next = new_node

  def insert_at_index(self, index, data):
      if index < 0:
          return
      if index == 0:
          self.insert_at_beginning(data)
          return
      new_node = Node(data)
      temp = self.head
      for _ in range(index - 1):
          if temp is None:
              return
          temp = temp.next
      if temp is None:
          return
      new_node.next = temp.next
      temp.next = new_node

  def delete_by_value(self, key):
      if self.head is None:
          return
      if self.head.data == key:
          self.head = self.head.next
          return
      temp = self.head
      while temp.next and temp.next.data != key:
          temp = temp.next
      if temp.next:
          temp.next = temp.next.next

  def delete_at_index(self, index):
      if index < 0 or self.head is None:
          return
      if index == 0:
          self.head = self.head.next
          return
      temp = self.head
      for _ in range(index - 1):
          if temp is None:
              return
          temp = temp.next
      if temp is None or temp.next is None:
          return
      temp.next = temp.next.next

  def search(self, key):
      temp = self.head
      while temp:
          if temp.data == key:
              return True
          temp = temp.next
      return False

  def display(self):
      temp = self.head
      while temp:
          print(temp.data, end=" -> ")
          temp = temp.next
      print("null")

# Test code
if __name__ == "__main__":
  ll = LinkedList()
  ll.insert_at_beginning(10)
  ll.insert_at_end(20)
  ll.insert_at_index(1, 15)
  ll.display()  # 10 -> 15 -> 20 -> null

  ll.delete_by_value(15)
  ll.display()  # 10 -> 20 -> null

  ll.delete_at_index(0)
  ll.display()  # 20 -> null

  print("Search 20:", ll.search(20))  # True
  print("Search 10:", ll.search(10))  # False
