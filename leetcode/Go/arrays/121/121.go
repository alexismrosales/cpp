package main

func maxProfit(prices []int) int {
	// Buying the first day and selling the first day
	dayToBuy, dayToSell := 0, 1
	profit := 0
	if len(prices) == 1 {
		return 0
	}

	for dayToSell < len(prices) {
		// In case we have a lost when selling on the dayToSell day
		if prices[dayToBuy] <= prices[dayToSell] {
			newProfit := prices[dayToSell] - prices[dayToBuy]
			if newProfit > profit {
				profit = newProfit
			}
			// After selling, we check if we have a better profit
			dayToSell++
		} else {
			// In case we have no profit we move to the next day
			dayToBuy++
		}
	}
	return profit
}
