package main

type ListNode struct {
	Val  int
	Next *ListNode
}

func reverseBetween(head *ListNode, left int, right int) *ListNode {
	var ptr, prev, next *ListNode = head, nil, nil
	count := 1
	for ptr != nil {
		if left <= count && count <= right {
			next = ptr.Next
			ptr.Next = prev
			prev = ptr
			ptr = next
		} else {
			ptr = ptr.Next
		}
		count++
	}
	return ptr
}
