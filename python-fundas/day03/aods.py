# Advanced Python Objects and Data Structures

from collections import namedtuple, deque, defaultdict, Counter, OrderedDict
import heapq
import array
import queue
from enum import Enum
from dataclasses import dataclass
import weakref

Employee = namedtuple("Employee", ["id", "name", "salary"])
e1 = Employee(101, "Sonu", 50000)
print(e1.name, e1.salary)

dq = deque([1, 2, 3])
dq.appendleft(0)
dq.append(4)
print(dq)

dd = defaultdict(int)
dd["a"] += 1
print(dd)

cnt = Counter("banana")
print(cnt)
print(cnt.most_common(1))

od = OrderedDict()
od["a"] = 1
od["b"] = 2
print(od)

nums = [5, 1, 8, 3]
heapq.heapify(nums)
heapq.heappush(nums, 0)
print(heapq.heappop(nums))

s = {1, 2, 3}
fs = frozenset([3, 4, 5])
print(s | fs)

arr = array.array("i", [1, 2, 3])
arr.append(4)
print(arr)

q = queue.Queue()
q.put(10)
q.put(20)
print(q.get())


class Status(Enum):
    PENDING = 1
    SUCCESS = 2
    FAILED = 3


print(Status.SUCCESS, Status.SUCCESS.name)


@dataclass
class EmployeeData:
    id: int
    name: str
    salary: float


emp = EmployeeData(102, "Monu", 60000)
print(emp)

data = bytearray(b"Hello")
mv = memoryview(data)
mv[0] = 90
print(data)
