/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Next *Node
 *     Random *Node
 * }
 */

func copyRandomList(head *Node) *Node {
	if head == nil {
		return nil
	}
	var nodes = make(map[*Node]*Node)

	curr := head
	for curr != nil {
		nodes[curr] = &Node{Val: curr.Val}
		curr = curr.Next
	}

	curr = head
	for curr != nil {
		nodes[curr].Next = nodes[curr.Next]
		nodes[curr].Random = nodes[curr.Random]
		curr = curr.Next
	}

	return nodes[head]

	return head
}
