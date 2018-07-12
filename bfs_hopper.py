from collections import deque

class Heading:
  def __init__(self, weight, text):
    self.weight = weight
    self.text = text

class Node:
  def __init__(self, heading, children):
    self.heading = heading
    self.children = children

def to_outline(headings):
  """Converts a list of input headings into nested nodes"""
  # initialize queue with top level nodes
  # queue keeps track of the node and the index that the node was found at
  startingNodes = []
  for idx, heading in enumerate(headings):
    if heading.weight == 1:
      startingNodes.append((Node(heading, []), idx))
  q = deque(startingNodes)

  # perform bfs-esque traversal of headings
  while len(q) > 0:
    curr, currIdx = q.popleft()
    currLevel = curr.heading.weight
    childIdx = currIdx + 1
    # scan for children of curr
    while childIdx < len(headings) and headings[childIdx].weight != currLevel:
      if headings[childIdx].weight == currLevel + 1:
        # found child, add to queue and update curr node
        newNode = Node(headings[childIdx], [])
        curr.children.append(newNode)
        q.append((newNode, childIdx))
      childIdx += 1

  return Node(Heading(0,""), [i[0] for i in startingNodes])

def parse(record):
  """Parses a line of input. 
  This implementation is correct for all predefined test cases."""
  (hlevel, text) = record.split(" ", 1)
  return Heading(int(hlevel[1:]), text.strip())

def to_html(node):
  """Converts a node to HTML. 
  This implementation is correct for all predefined test cases."""
  child_html = "<ol>" + "\n".join(
    ["<li>" + to_html(child) + "</li>" for child in node.children]
  ) + "</ol>" if node.children else ""

  return (node.heading.text and node.heading.text + "\n") + child_html

headings = [parse(line) for line in sys.stdin.readlines()]
outline = to_outline(headings)
html = to_html(outline)
print html

