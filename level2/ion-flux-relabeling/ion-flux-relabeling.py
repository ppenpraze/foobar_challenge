def findParentNode(topNode,num,lowerNode):
  lowerNode=int(lowerNode/2)
  leftNode=topNode-1-lowerNode
  rightNode=topNode-1
  if num in (leftNode,rightNode):
      return(topNode)
  if num<leftNode:
    return findParentNode(leftNode,num,lowerNode)
  else:
    return findParentNode(rightNode,num,lowerNode)

def solution(h, q):
  topNode=(2**h)-1
  return([ findParentNode(topNode,num,topNode-1) if num>=1 and num<topNode else -1 for num in q ])
