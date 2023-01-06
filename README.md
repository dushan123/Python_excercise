# Python_excercise
class WorkPeice(): def init(self, material, shape, radius=None, length=None, width=None, height=None, base=None, height_P=None):

    self.material = material
    self.shape = shape
    self.radius   = radius
    self.length  = length
    self.width = width
    self.height=height
    

def __add__(self, other):
  Volume= self.height + other.height
  return Volume
   

def print_material_volume_breakdown(self):
  if self.shape == 'Cylider':
    Volume= 3.14* self.radius**2*self.height
    return  Volume 
     
  elif self.shape == 'Cubic':
    Volume= self.length*self.width*self.height
    return  Volume
    
  elif self.shape == 'Prism':
    Volume= self.base*self.length*self.height_P*self.height*0.5
    return  Volume
  else:
    print("Shape Error")

def Total_cost(self):
  if self.material == 'wood':
    cost= WorkPeice.print_material_volume_breakdown(self)*200 #UnitCost_of_Wood
    return  cost
  elif self.material == 'steel':
    cost= WorkPeice.print_material_volume_breakdown(self)*2200 #UnitCost_of_steel
    return  cost
    
wooden_top = WorkPeice(material='wood',shape='Cylider', radius=1, height=0.1) 
metal_leg = WorkPeice(material='steel',shape='Cylider', radius=0.1, height=2) 
metal_cubic=WorkPeice(material='steel',shape='Cube', length=1, width=3,height=2) 
chair=wooden_top.add(metal_leg)

wooden_top_volume=wooden_top.print_material_volume_breakdown() 
metal_leg_volume=metal_leg.print_material_volume_breakdown()

wooden_top_cost=wooden_top.Total_cost() 
metal_leg_cost=metal_leg.Total_cost()

print(wooden_top_cost) 
print(metal_leg_cost) 
print(wooden_top_volume) 
print(metal_leg_volume) print(chair)
