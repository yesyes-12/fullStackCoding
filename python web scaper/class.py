#상속inheritence
class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed= breed
        self.age= age
    
    def sleep(self):
        print("zzzzzzzzzzzzzz...")
class GuardDog(Dog):
    def __init__(self, name, breed):
        super().__init__(name, breed, 5,)
    def rrrr(self):
        print("stay away!")
        
'''python class method 규칙
1. class 내부에서 정의되어야한다.
2. 1번째로 받는 argument는 언제나 자기자신을 참조하는 self라는 값이다.'''
class Puppy(Dog):
    def __init__(self, name, breed):
        super().__init__(name, breed, 0.1,) #super은 부모 class를 참조
        
    def woof_woof(self):
        print("woof woof!")

ruffus = Puppy(
    name="Ruffus", 
    breed="beagle"
    )
bibi = GuardDog(
    name="bibi", 
    breed="dalmatian"
    )

#print(ruffus) #<__main__.Puppy object at 0x000001D60A193A88> => ruffus는 puppy의 객체
ruffus.woof_woof()
bibi.rrrr()
