package main

type ListNode struct {
	Val  int
	Next *ListNode
}

func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {
	ptr1, ptr2 := list1, list2
	var mergedList ListNode
	tmp := &mergedList

	// In case there is an empty list
	if list1 == nil {
		return list2
	}
	if list2 == nil {
		return list1
	}

	// Mixing the nodes in order
	for ptr1 != nil && ptr2 != nil {
		if ptr1.Val < ptr2.Val {
			tmp.Next = ptr1
			ptr1 = ptr1.Next
		} else {
			tmp.Next = ptr2
			ptr2 = ptr2.Next
		}
		tmp = tmp.Next
	}

	// In case there is a list that is bigger than other the rest is added to the end
	if ptr1 != nil {
		tmp.Next = ptr1
	}
	if ptr2 != nil {
		tmp.Next = ptr2
	}
	return mergedList.Next
}
