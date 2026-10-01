def middleNode(head: ListNode | None) -> ListNode | None:
    count = 0 
    temp = head 
    while temp:
        count += 1
        temp = temp.next 
    mid_ind = count // 2
    temp = head
    for i in range(mid_ind):
        temp = temp.next 
    return temp