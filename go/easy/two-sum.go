func twoSum(nums []int, target int) []int {
	dict := map[int]int{}
	for idx, num := range nums {

		if _, ok := dict[target-num]; ok {
			return []int{idx, dict[target-num]}
		}
		dict[num] = idx
	}
	fmt.Println(dict)
	return []int{}
}
