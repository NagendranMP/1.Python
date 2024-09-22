class nagendran():
    def Subfields():
        list1=["Machine Learning","Neural Network","Vision","Robotics",
               "Speech Processing","Natural Language Processing"]
        print("Sub-fields in AI are:")
        for i in list1:
            print(i)
    def OddEven():
        n=int(input("Enter the number:"))
        if n%2==0:
            print(f"{n} is Even number")
        else:
            print(f"{n} is Odd number")
    def Elegible():
        gen=input("Your Gender:")
        age=int(input("Your Age:"))
        if gen=="Male" and age>21:
            print("ELEGIBLE")
        elif gen=="Female" and age>18:
            print("ELEGIBLE")
        else:
            print("NOT ELEGIBLE")
    def Percentage():
        list1=[98,87,95,95,93]
        for i in range(len(list1)):
            print(f"Subject{i+1}=",list1[i])
        Total=0
        for i in list1:
            Total=Total+i
        print("Total:",Total)
        percentage=Total/len(list1)
        print("Percentage:",percentage)
    def Triangle():
        height=int(input("Height:"))
        breadth=int(input("Breadth:"))
        formula=(height*breadth)/2
        print("Area of formula: (height*breadth)/2")
        print("Area of Triangle:",formula)
        height1=int(input("Height1:"))
        height2=int(input("Height2:"))
        breadth=int(input("Breadth1:"))
        formula1=height1+height2+breadth
        print("Perimeter formula: Height1+Height2+Breadth")
        print("Perimeter of triangle:",formula1)