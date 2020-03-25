class Vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def __str__(self):
        return "{"+str(self.x)+","+str(self.y)+","+str(self.z)+"}"
    def ponderacion_de_vector(self,n):
        self.x=(self.x)*n
        self.y=(self.y)*n
        self.z=(self.z)*n
def suma_de_vectores(vector1,vector2):
    x=vector1.x+vector2.x
    y=vector1.y+vector2.y
    z=vector1.z+vector2.z
    v=vector(x,y,z)
    return v
x=input()
y=input()
z=input()
v=Vector(x,y,z)
v.print_vector()

