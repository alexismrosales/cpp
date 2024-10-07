package main

func containsDuplicate(nums []int) bool {
	m := make(map[int]bool)
	// Traversing the array and saving in a map if it doesn't exists.
	for i := 0; i < len(nums); i++ {
		// Checking if the number is already in the map
		_, exists := m[nums[i]]
		// If the number is in the map then there is a repeated number
		if exists {
			return true
		} else {
			m[nums[i]] = false
		}
	}
	return false
}
