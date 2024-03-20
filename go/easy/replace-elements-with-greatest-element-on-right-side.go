func replaceelements(arr []int) []int {
   maxnum := -1
   for i := len(arr) - 1; i >= 0; i--{
    arr[i], maxnum = maxnum, max(maxnum, arr[i])
   }
   return arr
