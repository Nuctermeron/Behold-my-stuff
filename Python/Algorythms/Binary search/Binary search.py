def binary_search(sequence, item):
    begin_index = 0
    end_index = len(sequence) - 1
    
    while begin_index <= end_index:
        midpoint = begin_index + (end_index- begin_index) //2
        midpoint_value = sequence[midpoint]
        if midpoint_value == item:
            return midpoint
        
        elif item < midpoint_value:
            end_index = midpoint - 1
            
        else: 
            begin_index = midpoint + 1
    return None

my_list = [*range(0,100)]
my_item = 17

print(binary_search(my_list,my_item))
            