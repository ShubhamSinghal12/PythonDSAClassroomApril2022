def fn(age):
    print("In fn")
    if age < 0:
        raise Exception("Age is Negative")
    print(age)
        
    print("out fn")

def inpAge():
    print("In inputAge")
    fn(-20)
    print("Out inputAge")

print("Hi")
try:
    inpAge()
except Exception as e:
    print("Exception!!! - >",end= " ")
    print(e)

print("Bye")