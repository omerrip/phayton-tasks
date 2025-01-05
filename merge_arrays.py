def merge_arrays (arrayA,arrayB):
  return sorted(set(arrayA+arrayB))

a=[1,4,7,9,3,6]
b=[2,1,7,11,19]
c=merge_arrays(a,b)
print(c)





def merge_arrays(arrayA, arrayB):
    return sorted(set(arrayA + arrayB))

a = list(map(int, input("Birinci liste elemanlarini aralarinda boşluk birakarak girin: ").split()))

b = list(map(int, input("İkinci liste elemanlarini aralarinda boşluk birakarak girin: ").split()))

c = merge_arrays(a, b)

print("Birleştirilmiş ve siralanmiş liste:", c)
