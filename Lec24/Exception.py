def fn(age):
    print("In fn")
    if age < 0:
        raise Exception("Age is Negative")
    print(age)
    
    print("out fn")

def inpAge():
    try:
        print("In inputAge")
        fn(20)
        print("Out inputAge")
        return
    
    except Exception as e:
        print("Exception!!! - >",end= " ")
        print(e)
    
    finally:
        print("Bye IN !!!")


print("Hi")
inpAge()
print("Bye")