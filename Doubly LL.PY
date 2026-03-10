class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
    
node1 = Node(3)
node2 = Node(5)
node3 = Node(13)
node4 = Node(2)

node1.next = node2

node2.prev = node1
node2.next = node3

node3.prev = node2
node3.next = node4

node4.prev = node3

print("\nTraversing forward:")
currentNode = node1
while currentNode:
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.next
print("null")

print("\nTraversing backward:")
currentNode = node4
while currentNode:
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.prev
print("null")

class Node:
  def __init__(self, data):
      self.data = data
      self.prev = None
      self.next = None

class DoublyLinkedList:
  def __init__(self):
      self.head = None

  def insert_at_beginning(self, data):
      new_node = Node(data)
      new_node.next = self.head
      if self.head:
          self.head.prev = new_node
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
      new_node.prev = temp

  def insert_at_index(self, index, data):
      if index < 0:
          return
      if index == 0:
          self.insert_at_beginning(data)
          return
      temp = self.head
      for _ in range(index - 1):
          if temp is None:
              return
          temp = temp.next
      if temp is None:
          return
      new_node = Node(data)
      new_node.next = temp.next
      new_node.prev = temp
      if temp.next:
          temp.next.prev = new_node
      temp.next = new_node

  def delete_by_value(self, key):
      temp = self.head
      while temp and temp.data != key:
          temp = temp.next
      if temp is None:
          return
      if temp.prev:
          temp.prev.next = temp.next
      else:
          self.head = temp.next  # deleting head
      if temp.next:
          temp.next.prev = temp.prev

  def delete_at_index(self, index):
      if index < 0 or self.head is None:
          return
      temp = self.head
      for _ in range(index):
          if temp is None:
              return
          temp = temp.next
      if temp is None:
          return
      if temp.prev:
          temp.prev.next = temp.next
      else:
          self.head = temp.next  # deleting head
      if temp.next:
          temp.next.prev = temp.prev

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
          print(temp.data, end=" <-> ")
          temp = temp.next
      print("null")


# Test code
if __name__ == "__main__":
  dll = DoublyLinkedList()
  dll.insert_at_beginning(10)
  dll.insert_at_end(20)
  dll.insert_at_index(1, 15)
  dll.display()  # 10 <-> 15 <-> 20 <-> null

  dll.delete_by_value(15)
  dll.display()  # 10 <-> 20 <-> null

  dll.delete_at_index(0)
  dll.display()  # 20 <-> null

  print("Search 20:", dll.search(20))  # True
  print("Search 10:", dll.search(10))  # False

