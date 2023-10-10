func search(nums []int, target int) int {
	return binarySearch(nums[:], 0, len(nums), target)
}

func binarySearch(nums []int, l int, r int, target int) int {
	if l >= r {
		return -1
	}

	m := l + (r-l)/2
	if nums[m] > target {
		return binarySearch(nums[:], l, m, target)
	} else if nums[m] < target {
		return binarySearch(nums[:], m+1, r, target)
	} else {
		return m
	}
}
