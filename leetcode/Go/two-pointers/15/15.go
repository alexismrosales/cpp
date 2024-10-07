package main

func twoSum(numbers []int, target int) []int {
	// Two pointers, one at the beggining and at the end of the array
	i, j := 0, len(numbers)-1
	for range len(numbers) {
		// Sum of two digits
		sum := numbers[i] + numbers[j]
		// In case the sum is smaller than the target left pointer go next
		if sum < target {
			i++
		} else if sum > target {
			j--
		} else {
			// In case the sum is equal to target
			break
		}
	}
	return []int{i, j}
}
