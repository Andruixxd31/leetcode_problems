func countSeniors(details []string) int {
	var count int
	for _, senior := range details {
		age, _ := strconv.Atoi(senior[11:13])
		if age > 60 {
			count++
		}
	}
	return count
}
