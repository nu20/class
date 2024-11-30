class student : 
    def __init__(self,name,grade):
        self.grade = grade
        self.name = name
        
    def printinfo(self) :
        print("name : ", self.name)
        print("grade : ", self.grade)

    def __del__(self) :
        print("i am the destructer")      
            
student1 = student("Ishaan" , 8)
student1.printinfo()
        