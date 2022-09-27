## collections: Counter, namedtuple, OrderedDict, defaultdict, deque
from collections import Counter, namedtuple, OrderedDict, defaultdict, deque


text = "somedayiwillworkwithatopcompany"
counter = Counter(text)
print(f"counter: {counter}") #view counter: dict with freq for each char in input
print(f"MostCommon: {counter.most_common(1)}") # Most common value returns a list of tuples
print(f"Elements: {list(counter.elements())}") #iter over elements repeating as many times as their counts

#define a namedtuple of 2d-points
Coordinates = namedtuple("Point", "x, y")
cord = Coordinates(2, -8)
print(f"Coordinates: {cord.x}, {cord.y}, {cord}")

#ordered dictionary: current python version maintain order with normal dictionaries({})
ordered_dict = OrderedDict()
ordered_dict["b"] = 3
ordered_dict["a"] = 2
ordered_dict["d"] = 2
ordered_dict["c"] = 2
print(f"Ordered dict: {ordered_dict}")

## Default dict: similar to normal dict container.
## except it maintains a default value if a key has not been set yet
d = defaultdict(int) #return default int value if key not set
d["a"] = 2
d["b"] = 1
print(f"Default dict: {d}, {d['c']}")

## deque: double ended queue
