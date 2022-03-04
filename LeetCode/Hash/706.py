import collections


class MyHashMap:

    def __init__(self):
        self.hashmap = {}

    def put(self, key: int, value: int) -> None:
        self.hashmap[key] = value

    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1
        return self.hashmap.get(key)

    def remove(self, key: int) -> None:
        if key not in self.hashmap:
            return -1
        del self.hashmap[key]

# 개별 체이닝 방식
# 파이썬은 원래 오픈 어드레싱으로 해시를 구현함


class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None


class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.table = collections.defaultdict(ListNode)

    def put(self, key: int, value: int) -> None:
        # 나머지 모듈이용
        index = key % self.size
        # defaultdict로 선언해서 .value로 접근
        if self.table[index].value is None:
            self.table[index] = ListNode(key, value)
            return
        p = self.table[index]
        while p:
            if p.key == key:
                p.value = value
                return
            if p.next is None:
                break
            p = p.next
        p.next = ListNode(key, value)

    def get(self, key: int) -> int:
        index = key % self.size
        if self.table[index].value is None:
            return -1
        p = self.table[index]
        while p:
            if p.key == key:
                return p.value
            p = p.next
        return -1

    def remove(self, key: int) -> None:
        index = key % self.size
        if self.table[index].value is None:
            return
        p = self.table[index]
        if p.key == key:
            self.table[index] = ListNode() if p.next is None else p.next
            return
        # 노드 삭제
        prev = p
        while p:
            if p.key == key:
                prev.next = p.next
                return
            prev, p = p, p.next
