class WorkPeice():
    def __init__(self, material, shape, radius=None, length=None, width=None, height=None, base=None, height_P=None):
        
        self.material = material
        self.shape = shape
        self.radius   = radius
        self.length  = length
        self.width = width
        self.height=height
        self.base=base
        self.height_P=height_P
        

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
metal_cubic=WorkPeice(material='steel',shape='Cubic', length=1, width=3,height=2)
prism_shape= WorkPeice(material='steel', shape= 'Prism', base=2, height_P=3,height=10)

#chair=wooden_top.__add__(metal_leg)
#print (wooden_top.radius)

wooden_top_volume=wooden_top.print_material_volume_breakdown()
metal_leg_volume=metal_leg.print_material_volume_breakdown()

wooden_top_cost=wooden_top.Total_cost()
metal_leg_cost=metal_leg.Total_cost()

print(metal_cubic.print_material_volume_breakdown())
print(wooden_top_cost)
print(metal_leg_cost)
print(wooden_top_volume)
print(metal_leg_volume)
print(chair)

#print_material_volume_breakdown()

#wooden_top = WorkPiece(material="Wood", shape="Cylinder", radius=1, height=0.1)
#metal_leg = WorkPiece(material="Steel", shape="Cylinder", radius=0.1, height=2)
#chair = wooden_top + 4 * metal_leg

#chair.print_material_volume_breakdown()
#chair.print_total_cost()
