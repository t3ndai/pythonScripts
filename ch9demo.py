#! /usr/bin/env python3.4

#use lambda with filter 
filter_me = [1,2,3,4,5,6,7,8,11,12,14,15,19,22]
#This will only return true for even numbers (becasue x%2 is 0 or false 
#for odd numbers)
result = filter(lambda x: x%2 == 0, filter_me)
print(*result)

