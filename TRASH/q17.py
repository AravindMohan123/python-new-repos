dictionary={}
b = int(input("Enter the limit for dictionary"))
for i in range(b):
    dictionary[i] = input("Enter the values")

print("the sorted elements in dictionary are")
print(sorted(dictionary.items()))
print(sorted(dictionary.items(),reverse=True))
