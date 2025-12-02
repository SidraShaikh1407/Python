class shape:
  length=0
  width=0
  def __init__(self,l,w):
    self.length=l
    self.width=w
  def __str__(self):
    return str(self.length)+","+str(self.width) 
  def area(self):
    return self.length*self.width
  def perimeter(self):
    return 2*(self.length+self.width)   

class box(shape):
  height=0
  def __init__(self,l,w,h):
    shape.__init__(self,l,w)
    self.height=h
  def volume(self):
    return self.length*self.width*self.height
  def perimeter(self):
    return 4*(self.length+self.width+self.height)   
