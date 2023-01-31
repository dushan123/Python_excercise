class CompositeObject:
  
  def __init__(self, object1=None, object2=None):
    self.object1 = object1
    self.object2 = object2

  def __add__(self, other):
    Composite = CompositeObject(self, other)
    return Composite

  def get_volume(self):
      composite_volume = 0
      objects = [self.object1.print_object_volume(),self.object2.print_object_volume()]

      for x in objects:
        
        composite_volume = composite_volume + x
        
      return print(composite_volume)

class WorkPeice:

  def __init__(self,material,shape,radius=None,length=None,width=None,height=None,base=None,height_p=None):

    self.material = material
    self.shape = shape
    self.radius = radius
    self.length = length
    self.width = width
    self.height = height
    self.base = base
    self.height_p = height_p
    
  def __add__(self, other):
    Composite = CompositeObject(self, other)
    return Composite

  def __mul__(self, other):
    Composite2 = CompositeObject(self,other)
    return Composite2

  def print_object_volume(self):
    if self.shape == 'Cylider':
      Volume = 3.14 * self.radius**2 * self.height
      return Volume

    elif self.shape == 'Cubic':
      Volume = self.length * self.width * self.height
      return Volume

    elif self.shape == 'Prism':
      Volume = self.base * self.height_p * self.height * 0.5
      return Volume

    else:
      print("Shape Error")

  def total_cost(self):
    if self.material == 'wood':
      cost = self.print_object_volume() * 200  #UnitCost of Wood
      return cost
      
    elif self.material == 'steel':
      cost = self.print_object_volume() * 2200  #UnitCost of steel
      return cost


wooden_top = WorkPeice(material='wood', shape='Cylider', radius=1, height=0.1)
metal_leg = WorkPeice(material='steel', shape='Cylider', radius=0.1, height=3)
metal_cubic = WorkPeice(material='steel',shape='Cubic',length=1,width=3,height=2)
prism_shape = WorkPeice(material='steel',shape='Prism',base=2,height_p=3,height=10)

wooden_top_cost = wooden_top.total_cost()
metal_leg_cost = metal_leg.total_cost()

print(wooden_top.print_object_volume())
print(metal_leg.print_object_volume())
print(metal_cubic.print_object_volume())
print(prism_shape.print_object_volume())

composite1 = wooden_top + metal_leg
chair= wooden_top + metal_leg*4
composite2= composite1 + prism_shape
composite3 = composite1 + composite2

print(composite1)
print(composite2)
print(composite3)

composite1.get_volume()
#composite2.get_volume()    cant find this volume

