func isPalindrome(s string) bool {
	l, r := 0, len(s)-1
	for l < r {
		for l < len(s) && !unicode.IsLetter(rune(s[l])) && !unicode.IsDigit(rune(s[l])) {
			l++
		}
		for r >= 0 && !unicode.IsLetter(rune(s[r])) && !unicode.IsDigit(rune(s[r])) {
			r--
		}
		if l >= len(s) || r < 0 {
			break
		}
		if unicode.ToLower(rune(s[l])) != unicode.ToLower(rune(s[r])) {
			return false
		}
		l++
		r--
	}
	return true
}
