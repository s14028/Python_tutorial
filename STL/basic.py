array = [i for i in range(0, 11)]
array = filter(lambda x: x < 6, array)

'''
Could be replaced with.
'''
array = list(array)
array = [i for i in array if i < 6]
array = sorted(array)
r = sum(array)
