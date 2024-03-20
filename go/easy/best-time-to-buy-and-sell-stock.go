func maxProfit(prices []int) int {
    if len(prices) < 1 {
        return 0
    }
    l, r := 0, 1
    bestDeal := 0
    for r < len(prices) {
        if prices[r] - prices[l] > bestDeal{
            bestDeal = prices[r] - prices[l]
        }
        if prices[r] < prices[l]{
            l = r
        }
        r++
    }

    return bestDeal
}
