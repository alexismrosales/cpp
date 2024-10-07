package main

import "sort"

func longestConsecutive(nums []int) int {
	if len(nums) == 0 {
		return 0
	}
	if len(nums) == 1 {
		return 1
	}

	// Ordering array
	sort.Ints(nums)
	counter := 1
	longest := 1

	for i := 1; i < len(nums); i++ {
		if nums[i] == nums[i-1] {
			// Ignoring duplicates
			continue
		}
		if nums[i] == nums[i-1]+1 {
			// Incrementing counter if consecutives
			counter++
		} else {
			// Restarting counter
			counter = 1
		}
		if counter > longest {
			longest = counter
		}
	}
	return longest
}
