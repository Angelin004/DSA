#resize array
def resize(self):
  self.capacity *= 2
  new_arr = [0] * self.capacity
  for i in range(self.size):
      new_arr[i] = self.arr[i]
  self.arr = new_arr

#dynamic array as ADT
class DynamicArray:
  def __init__(self, capacity):
      self.capacity = capacity
      self.arr = [0] * capacity
      self.size = 0

  def insert(self, index, element):
      if index < 0 or index > self.size:
          print("Can't insert: Invalid Index")
          return False
      if self.size >= self.capacity:
          self.resize()
      for i in range(self.size, index, -1):
          self.arr[i] = self.arr[i - 1]
      self.arr[index] = element
      self.size += 1
      return True

  def get(self, index):
      if index < 0 or index >= self.size:
          print("Invalid Index")
          return -9999
      return self.arr[index]

  def set(self, index, element):
      if index < 0 or index >= self.size:
          print("Invalid Index")
          return
      self.arr[index] = element

  def display(self):
      for i in range(self.size):
          print(self.arr[i], end=" ")
      print()

  def search(self, element):
      for i in range(self.size):
          if self.arr[i] == element:
              return i
      return -1

  def delete(self, index):
      if index < 0 or index >= self.size:
          print("Can't delete: Invalid Index")
          return False
      for i in range(index, self.size - 1):
          self.arr[i] = self.arr[i + 1]
      self.size -= 1
      return True

  def resize(self):
      self.capacity *= 2
      new_arr = [0] * self.capacity
      for i in range(self.size):
          new_arr[i] = self.arr[i]
      self.arr = new_arr


# Test
if __name__ == "__main__":
  arr = DynamicArray(5)

  arr.insert(0, 5)
  arr.insert(1, 4)
  arr.insert(1, 67)
  arr.insert(1, 7)
  arr.insert(1, 87)
  arr.insert(2, 45)  # Triggers resize

  print(arr.capacity)
  arr.display()

  print("get:", arr.get(0))
  arr.set(1, 78)
  arr.delete(1)
  arr.display()

  print("search:", arr.search(78))
