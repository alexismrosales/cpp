package main

type ListNode struct {
	Val  int
	Next *ListNode
}

func hasCycle(head *ListNode) bool {
	// Creating a map to store the new directions
	values := make(map[*ListNode]struct{})
	for head != nil {
		_, directionExists := values[head]
		// In case the direction is already in the map it is a cycle
		if directionExists {
			return true
		}
		// Saving the value in the map
		values[head] = struct{}{}
		// Go to the next node
		head = head.Next
	}
	return false
}
