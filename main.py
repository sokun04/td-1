from collections import namedtuple
Point1D=namedtuple("Point1D",['x'])
print(Point1D)

p_04=Point1D(0.4)
print(p_04)
p_05=Point1D(0.5)

#ce qu'on voudrait
#p_04+p_05
#Ce que l'on a
#(0.4,0.5)

def ajout_point(point1, point2):
  x=point1[0] + point2[0]
  print(x)
  return Poind1D(x)

print(f"Addition ok: {ajout_point(p_04,p_05)}")