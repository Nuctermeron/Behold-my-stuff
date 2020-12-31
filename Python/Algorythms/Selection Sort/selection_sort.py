def selection_sort(list_a):
    
    for i in range(len(list_a)-1): #i stands for how many elements have been sorted

        min_index = i #assume first object is minimum

        for j in range(i+1, len(list_a)-1): #j loop through rest of items
            if list_a[j] < list_a[min_index]: #find out if j is lower than min
                min_index = j #update of variablee
        # After finding the lowest item of the unsorted regions, swap with the first unsorted item
        list_a[i], list_a[min_index] = list_a[min_index], list_a[i]
        
        
list_a = [7,8,3,3,4,6,1,2,4,7,8,5,3,1,7,9,0,2,4,6,7,3,2,1,6,4,7,3,2]
selection_sort(list_a)


print(list_a)