package main

func minSubArrayLen(target int, nums []int) int {
	if len(nums) == 1 {
		if nums[0] == target {
			return target
		} else {
			return 0
		}
	}
	max := 10001
	lp, rp, sum, min := 0, 1, 0, max
	size := len(nums) - 1

	// In case we got two pointers at the end
	for rp <= size {
		if lp+1 == rp {
			if nums[lp] == target || nums[rp] == target {
				return 1
			}
			sum = nums[lp] + nums[rp]
		}
		// In case we match the target
		if sum >= target {
			if rp-lp+1 < min {
				min = rp - lp + 1
			}
		}
		if sum < target {
			rp++
			if rp > size {
				break
			}
			sum += nums[rp]
		} else {
			sum -= nums[lp]
			lp++
			if lp+1 > size {
				break
			}
		}

	}
	if min == max {
		return 0
	}
	return min
}
