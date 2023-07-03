
def additon(*args):
    print(*args)
    print(type(args))
    sum= 0
    for i in args:
        sum = sum+i

    return (sum)

a= float(input("entr the firdst digit to add"))
b=int(input("enter the seconf digit"))
abc = input("enetr the string")
abcd = abc.split("$")
abcde = "#".join(abcd)

print("addition of thwo no. is ",additon(a,b))
print(f'additon of no. is {additon(a,b)} is this the correct ')
print(abc)
print(abcd)
print(abcde)


