func findMaxConsecutiveOnes(nums []int) int {
	count := 0
	left := 0
	for idx, val := range nums {
		if val == 1 {
			count = max(count, idx-left+1)
		} else {
			left = idx + 1
		}
	}
	return count
}
