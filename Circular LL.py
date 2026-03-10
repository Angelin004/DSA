#CLL
class Node:
  def __init__(self, data):
      self.data = data
      self.next = None

class CircularLinkedList:
  def __init__(self):
      self.tail = None

  def insert_at_beginning(self, data):
      new_node = Node(data)
      if self.tail is None:
          new_node.next = new_node
          self.tail = new_node
      else:
          new_node.next = self.tail.next
          self.tail.next = new_node

  def insert_at_last(self, data):
      new_node = Node(data)
      if self.tail is None:
          new_node.next = new_node
          self.tail = new_node
      else:
          new_node.next = self.tail.next
          self.tail.next = new_node
          self.tail = new_node

  def delete_at_beginning(self):
      if self.tail is None:
          print("Empty List")
          return
      if self.tail.next == self.tail:
          self.tail = None
      else:
          self.tail.next = self.tail.next.next

  def delete_at_last(self):
      if self.tail is None:
          print("Empty List")
          return
      if self.tail.next == self.tail:
          self.tail = None
      else:
          temp = self.tail.next
          while temp.next != self.tail:
              temp = temp.next
          temp.next = self.tail.next
          self.tail = temp

  def display(self):
      if self.tail is None:
          print("List is empty")
          return
      temp = self.tail.next
      while True:
          print(temp.data, end=" -> ")
          temp = temp.next
          if temp == self.tail.next:
              break
      print()

# Example usage
cll = CircularLinkedList()
cll.insert_at_beginning(7)
cll.insert_at_beginning(5)
cll.insert_at_beginning(1)
cll.insert_at_last(8)

cll.delete_at_last()

cll.display()

#singly CLL
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
node4.next = node1

currentNode = node1
startNode = node1
print(currentNode.data, end=" -> ") 
currentNode = currentNode.next 

while currentNode != startNode:
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.next

print("...")

#Double CLL
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
node1.prev = node4

node2.prev = node1
node2.next = node3

node3.prev = node2
node3.next = node4

node4.prev = node3
node4.next = node1

print("\nTraversing forward:")
currentNode = node1
startNode = node1
print(currentNode.data, end=" -> ")
currentNode = currentNode.next

while currentNode != startNode:
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.next
print("...")

print("\nTraversing backward:")
currentNode = node4
startNode = node4
print(currentNode.data, end=" -> ")
currentNode = currentNode.prev

while currentNode != startNode:
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.prev
print("...")


