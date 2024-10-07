package main

func maxProfit(prices []int) int {
	// In case there is only one day
	if len(prices) == 1 {
		return 0
	}

	m, n := 0, 1
	bestProfit := -1
	// Iterating until n reach the end of the array
	for n < len(prices) {
		profit := prices[n] - prices[m]
		// If there is not profit, pointer will go to next day
		if profit < 0 {
			m++
			n = m + 1
			// In case the profit is the best profit we assign it and go to the next day
		} else if profit > bestProfit {
			bestProfit = profit
			n++
			// If it is not any of the other cases, we just go to the other day
		} else {
			n++
		}
	}
	if bestProfit == -1 {
		return 0
	}
	return bestProfit
}
