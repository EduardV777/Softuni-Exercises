n1=int(input()); n2=int(input()); n3=int(input())
def add_and_substract(a1,a2):
    def sum_numbers():
        sum=a1+a2
        return sum
    def substract(res,a3):
        result=res-a3
        return result
    print(substract(sum_numbers(),n3))
add_and_substract(n1,n2)
