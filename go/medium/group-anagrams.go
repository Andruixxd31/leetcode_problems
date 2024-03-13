func SortString(w string) string {
	s := strings.Split(w, "")
	sort.Strings(s)
	return strings.Join(s, "")
}

func groupAnagrams(strs []string) [][]string {
	res := [][]string{}
	anagrams := make(map[string][]string)
	for _, v := range strs {
		wordSorted := SortString(v)
		if _, ok := anagrams[wordSorted]; ok {
			anagrams[wordSorted] = append(anagrams[wordSorted], v)
		} else {
			anagrams[wordSorted] = []string{v}
		}
	}

	for _, v := range anagrams {
		res = append(res, v)
	}

	return res
}
