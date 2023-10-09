class Base:
# TODO: there's code missing in one or more lines below
  
  def __init__(self,x1,y1,size1):
    self.x=x1
    self.y=y1
    self.size=size1

class Circle(Base):
  def __init__(self,x,y, size):
      super().__init__(x, y, size)
  def shape():
     return "This is a circle."

  def draw(self):
      return f"""
({self.x}, {self.y})\n{self.size}
         , - ~ ~ ~ - ,
     , '               ' ,
   ,                       ,
  ,                         ,
 ,                           ,
 ,                           ,
 ,                           ,
  ,                         ,
   ,                       ,
     ,                  , '
       ' - , _ _ _ ,  '
               """
def main():
    c = Circle(1,2,3)
    print(c.shape())
    print(c.draw())

main()