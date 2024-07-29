#number range of 1 to n:-
n=int(input())
digits=len(str(n))
total=0
for i in range(1,digits):
    commas_per_number=(i-1)//3
    how_many_nums=9*(10**(i-1))
    total +=commas_per_number*how_many_nums

commas_per_number=(digits-1)//3
how_many_nums=(n-(10**(digits-1)))+1
total +=commas_per_number*how_many_nums
print(total)
