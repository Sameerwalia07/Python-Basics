def total_gap(blocks):
    #sorting the blocks in ascending order
    blocks.sort()
    
    #initialize
    total_gap = 0
    
    #iteration
    for i in range(1,len(blocks)):
        #calculating the gap 
        gap = blocks[i] - blocks[i-1]
        total_gap += gap 
    return total_gap 

blocks = [7,1,4,3,2,1,8]

total_gap = total_gap(blocks) 
print("Total gap between the blocks is", total_gap)    