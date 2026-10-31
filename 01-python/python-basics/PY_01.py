name = "unaid-abdullah"
age = 23
skills = ["docker","python","kubernetes","aws","linux"]
          
print(f"my name is {name} and my age is {age} years old, and my skilks are {skills}")


if age > 18:
    print("Adult")
else:
    print("Minor")

for i in range(5):
    print("Loop index:", i)


squares = [i*i for i in range(10)]
print("Squares:", squares)

def add(a, b):
    return a + b

print("Sum:", add(10, 20))

student = {"name": "Shareh", "marks": [90, 85, 88]}
print(student["name"], "has marks", student["marks"])