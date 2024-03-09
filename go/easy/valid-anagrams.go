func isAnagram(s string, t string) bool {
	if len(s) != len(t) {
		return false
	}
	sM := make(map[rune]int)
	tM := make(map[rune]int)
	for _, v := range s {
		if _, ok := tM[v]; !ok {
			tM[v] = 1
		} else {
			tM[v]++
		}
	}
	for _, v := range t {
		if _, ok := sM[v]; !ok {
			sM[v] = 1
		} else {
			sM[v]++
		}
	}
	return reflect.DeepEqual(sM, tM)
}
