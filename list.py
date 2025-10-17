## creat a list
list=["Apple","banana","cherrry"] 
print(list)  
print(len(list)) 
print(type(list)) 
### allow to dublicate 
lst=["apple","banana","chherry","apple","banana","banana"] 
print(lst) 
print(len(lst)) 
print(type(lst)) 
### list item data type 
list1=["apple","banana","cherry"] 
list2=[1,2,3,4,] 
list3=[True,False,False]
print(len(list1)) 
print(type(list1))
print(list2)
print(list3)  
## list "str" int boolen 
lst=["apple",7,True,40,"male"] 
print(lst) 
print(type(lst)) 
print(len(lst))
## list indexed 
list=["apple", "banana", "cherry"] 
print(list[2]) 
lst=["apple", "banana", "cherry"] 
print(lst[-2]) 
## range of indexed 
list=["apple", "banana", "cherry", "orange", "kiwi", "mango"] 
print(list[2:5])
lst=["apple", "banana", "cherry", "orange", "melon", "mango"] 
print(list[:4]) 
list=["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(list[::4]) 
lst=["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"] 
print(lst[4::])
## append   
lst=["apple", "banana", "cherry", "orange"] 
s=lst.append("mango")
print(s)
###replase  
lst=["apple","banana","cherry"]
lst[1]="mango" 
print(lst)
##replace range items
thislist=["apple","banana","cherry","kiwi","papaya"]
thislist[1:3]=["watermelon","mango"]
print(thislist) 
###list.insert() 
thislist=["apple","papaya","kiwi","mango"] 
thislist.insert(1,"watermelon") 
print(thislist) 
#### apprnd()
lst=["apple","banana","papaya","kiwi"] 
lst.append("cherry") 
print(lst) 
### extend()
list=["apple","banana","cherry","papaya"] 
list2=["painapple","grapes","watermelon","mango"] 
list.extend(list2) 
print(list)