# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy = ListNode(None,head)
        seeker = head
        seekerPrev = dummy
        holder = dummy
        while seeker:
            if seeker.val < x and seekerPrev is not holder:
                temp = holder.next
                holder.next = seeker
                seekerPrev.next = seeker.next
                seeker.next = temp
                holder = seeker
                seeker = seekerPrev.next
            elif seeker.val >= x:
                seekerPrev = seeker
                seeker = seeker.next
            else:
                seekerPrev = seeker
                holder = holder.next
                seeker = seeker.next
        return dummy.next