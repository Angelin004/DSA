
class Array:
  def __init__(self, capacity):
      self.capacity = capacity
      self.arr = [0] * capacity  # initializes a list of given capacity with default value 0
      self.size = 0

#Access an Elements using Index - get( i )
def get(self, index):
  if index < 0 or index >= self.size:
      print("Get failed: Invalid index")
      return -1
  return self.arr[index]

#Update an Elements using Index - set( i , x )
def set(self, index, value):
  if index < 0 or index >= self.size:
      print("Set failed: Invalid index")
      return False
  self.arr[index] = value
  return True

#Insert an Element at Index - insert( i , x )
def insert(self, index, element):
  if self.size >= self.capacity or index < 0 or index > self.size:
      print("Insert failed: Invalid index or array is full")
      return False
  for i in range(self.size, index, -1):
      self.arr[i] = self.arr[i - 1]
  self.arr[index] = element
  self.size += 1
  return True

#Delete an Element at Index - delete( i )
def delete(self, index):
  if index < 0 or index >= self.size:
      print("Delete failed: Invalid index")
      return False
  for i in range(index, self.size - 1):
      self.arr[i] = self.arr[i + 1]
  self.size -= 1
  return True

#Search an Element at Index - search( x )
def search(self, target):
  for i in range(self.size):
      if self.arr[i] == target:
          return i
  return -1
