
class Node():
    def __init__(self, _value):
        self.value = _value

    def Node(self, _value, _left, _right):
        self.value = _value
        self.left = _left
        self.right = _right

    @public
    def setLeft(left):
        self.left = left

    @public
    def getLeft():
        return self.left

    @public
    def getRight():
        return self.right

    @public
    def setRight(right):
        self.right = right

    @public
    def getValue():
        return self.value
    

    @Override
    def toString():
        return Integer.toString(this.value)
    
    
    
    