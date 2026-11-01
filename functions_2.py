def add(a,b,c):
    res = a+b+c
    return res

def addition( *nums): # list
    """"
    returns sum of nums of all the numbers passed as arguments
    parameters:
     integers or floats or a mix of integers and floats
    returns:
     integers of floats
    """
    total = sum(nums)
    return total




def build_profile(**kwargs): #dict key-word args
    for k, w in kwargs.items():
        print(f"{k} : {w}")

# {"name": "Jerry", "age" :18}

# build_profile(age=25, name="Sofia",profession="lawyer",gender="female")

def fancy_function(x,*nums,**kwargs):
    print(name)
    print(nums)
    print(kwargs)

#anonymous == lambda
# def square(num):
#     return num*num

 # result = square(5)
 # print(result)

square = lambda num : num**2

print(square(5))

result = square(5)
print(result)

surface_area_cylinder = lambda r,h : 22/7 * r**2 *2 + 22/7 * 2* r*h
print(surface_area_cylinder(5,5))

people=[
    {"sofia":"", "age":25, "height":70, "weight":55},
    {"suheila":"", "age":10, "height":50, "weight":25},
    {"amir":"", "age":15, "height":70, "weight":35},
]

# lambda x : x["age"]
sorted_by_age = sorted(people, key= lambda x : x["age"] , reverse=True)
print(sorted_by_age)





# call function
# print(add(1,2,3))

# print(addition(1,2,3,6,6))
# print(addition(1,2,3,4,2,7,8))
# print(addition(1,2,3,4,5,9,1,5))
