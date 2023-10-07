func isValid(s string) bool {
	if len(s) <= 1 {
		return false
	}
	open := map[rune]rune{
		'(': ')',
		'{': '}',
		'[': ']',
	}
	stack := []rune{}

	for _, r := range s {
		if _, ok := open[r]; ok {
			stack = append(stack, r)
		} else if len(stack) == 0 || open[stack[len(stack)-1]] != r {
			return false
		} else {
			stack = stack[:len(stack)-1]
		}
	}

	return len(stack) == 0
}
