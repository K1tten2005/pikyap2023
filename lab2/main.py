from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square

def main():
    rec = Rectangle(2, 4, "красного")
    cir = Circle(4, "жёлтого")
    squ = Square(4, "зелёного")
    print(rec)
    print(cir)
    print(squ)

if __name__ == "__main__":
    main()