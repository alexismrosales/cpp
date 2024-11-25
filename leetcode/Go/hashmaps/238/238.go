package main

func productExceptSelf(nums []int) []int {
	ans := make([]int, len(nums))
	zeroes := 0 // [index];
	counter := 1
	// Getting all numbers multiplied
	for _, num := range nums {
		if num == 0 {
			zeroes++
		} else {
			counter *= num
		}
	}

	for i, num := range nums {
		if num != 0 {
			// If at least one zero exists
			if zeroes >= 1 {
				ans[i] = 0
			} else {
				ans[i] = counter / num
			}
		} else {
			// If more than one zero exists
			if zeroes > 1 {
				ans[i] = 0
			} else {
				ans[i] = counter
			}
		}
	}
	return ans
}
