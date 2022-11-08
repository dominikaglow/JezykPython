import math

d1 = {(1,1): 1, (1,2): 3, (1,3): 2, (2,1): -1, (2,2): 2, (2,3): 6,(3,1): 4, (3,2): 6,(3,3): -8}
d2 = {(1,1): 3, (1,2): 9, (1,3): 8, (2,1): 1, (2,2): 0, (2,3): -1,(3,1): 2, (3,2): 7,(3,3): 8}

def fillZeros(sparse, sparseForSize):
    sparse = sparseForSize
    sparse = dict.fromkeys(sparse, 0)
    return sparse

def add_sparse(sparse1, sparse2):
    res = {}
    for keys1 in sparse1:
        for keys2 in sparse2:
            if keys2 == keys1:
                sumElem = sparse1[keys1] + sparse2[keys2]
                res.update({keys1: sumElem})
    return res

def sub_sparse(sparse1, sparse2):
    res = {}
    for keys1 in sparse1:
        for keys2 in sparse2:
            if keys2 == keys1:
                sumElem = sparse1[keys1] - sparse2[keys2]
                res.update({keys1: sumElem})
    return res

def sizeMat(sparse):
    sizeTab = int(math.sqrt(len(sparse)))
    return sizeTab

def mul_sparse(sparse1, sparse2):
    res = {}
    # res = fillZeros(res, sparse1)
    for keys1 in sparse1:
        for keys2 in sparse2:
            if keys1[1] == keys2[0]:
                kr = (keys1[0], keys2[1])
                val = res.get((keys1[0], keys2[1]), 0) + sparse1[keys1] * sparse2[keys2]
                res.update({kr: val})
    return res



# print("Sum: ", add_sparse(d1, d2))
# print("Substraction: ", sub_sparse(d1, d2))
print("Multiply: ", mul_sparse(d1, d2))