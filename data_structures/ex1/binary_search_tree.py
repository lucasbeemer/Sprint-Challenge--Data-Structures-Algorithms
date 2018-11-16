class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def depth_first_for_each(self, cb):
    def search(self):
      if self.left is not None:
        cb(self.left.value) # cb on left of tree
        search(self.left)
      
      if self.right is not None:
        cb(self.right.value) # cb on right side
        search(self.right)

    cb(self.value)
    search(self)

  def breadth_first_for_each(self, cb):
    def search(self):
      if self.left is not None:
        cb(self.left.value)
      if self.right is not None:
        cb(self.right.value)
      if self.left is not None:
        search(self.left)
      if self.right is not None:
        search(self.right)

    cb(self.value)
    search(self)


  def insert(self, value):
    new_tree = BinarySearchTree(value)
    if (value < self.value):
      if not self.left:
        self.left = new_tree
      else:
        self.left.insert(value)
    elif value >= self.value:
      if not self.right:
        self.right = new_tree
      else:
        self.right.insert(value)

  def contains(self, target):
    if self.value == target:
      return True
    if self.left:
      if self.left.contains(target):
        return True
    if self.right:
      if self.right.contains(target):
        return True
    return False

  def get_max(self):
    if not self:
      return None
    max_value = self.value
    current = self
    while current:
      if current.value > max_value:
        max_value = current.value
      current = current.right
    return max_value
