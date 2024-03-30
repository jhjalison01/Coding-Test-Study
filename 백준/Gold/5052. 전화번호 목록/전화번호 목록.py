#백준 5052번 전화번호 목록
import sys
input=sys.stdin.readline

class Node(object):
  def __init__(self, key, data=None):
    self.key=key
    self.data=data
    self.children={}

class Trie(object):
  def __init__(self):
    self.head = Node(None)

  def insert(self, string):
    curr_node = self.head
    
    for s in string:
      #현재 노드 자식에 해당 글자가 없다면 추가
      if s not in curr_node.children:
        curr_node.children[s] = Node(s)
      #다음 노드로 이동
      curr_node=curr_node.children[s]
    # 반복 종료 후 단어의 끝 표시
    curr_node.data=string

  #접두어인지 확인
  def search_prefix(self, string):
    curr_node = self.head
    
    for s in string:
      curr_node = curr_node.children[s]
    #자식 노드가 있을 경우 현재 노드가 다른 전화번호의 끝에 도달하지 않았다는 의미 -> 현재 문자열이 다른 전화번호의 접두어로 사용될 수 있음
    if curr_node.children:
      return False
    else:
      return True
    
#테스트 케이스
t=int(input())

for i in range(t):
  #전화번호의 수
  n=int(input())
  #전화번호 입력받기
  trie = Trie()
  nums=[]
  for _ in range(n):
    num = input().rstrip()
    nums.append(num)
    trie.insert(num)
  
  flag = True
  nums.sort()
  for num in nums:
    if not trie.search_prefix(num):
      flag=False
      break
  if flag:
    print("YES")
  else:
    print("NO")