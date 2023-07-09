from typing import List


class SegmentTree:
    def __init__(self, arr: List[int]) -> None:
        self.arr = arr
        self.tree = [0] * (len(arr) * 4)

    def build(self, node: int, start: int, end: int) -> None:
        """ 세그멘트 트리를 만드는 함수
        node: 
            현재 노드의 세그멘트 트리 안에서의 위치 계산하기 쉽게 루트노드를 1부터 시작

        start, end:
            현재 노드의 담당 범위
        """
        if start == end:    # 리프 노드
            self.tree[node] = self.arr[start]
        else:
            mid = (start + end) // 2
            # 루트노드를 1부터 시작하면 노드의 왼쪽자식은 2n, 오른쪽자식은 2n + 1로 나타낼수있음
            self.build(node * 2, start, mid)
            self.build(node * 2 + 1, mid + 1, end)
            self.tree[node] = self.tree[node * 2] + \
                self.tree[node * 2 + 1]  # 자식노드들을 합침

    def qeury(self, node: int, start: int, end: int, left: int, right: int) -> int:
        """ 세그멘트 트리에서 값을 구하는 함수
        node: 
            현재노드의 인덱스

        start, end:
            구하고 싶은 인덱스 범위

        left, right:
            현재 노드가 담당하고있는 범위
        """
        if end < left or right < start:  # 담당 구역이 아니므로 0반환
            return 0
        elif left <= start and end <= right:
            return self.tree[node]
        else:
            mid = (start + end) // 2
            total_left = self.qeury(node * 2, start, end, left, mid)
            total_right = self.qeury(node * 2 + 1, start, end, mid + 1, right)
            return total_left + total_right

    def update(self, node: int, start: int, end: int, value: int, index: int) -> None:
        """ 배열의 특정 인덱스의 원소를 업데이트하는 함수
        node:
            바꾸려고하는 원소의 인덱스

        start, end:
            현재 노드의 담당 범위

        value:
            업데이트하는 값

        index:
            업데이트하는 원소의 인덱스
        """
        if start == end:    # 리프노드
            self.tree[node] = value
        else:
            mid = (start + end) // 2
            if start <= index <= mid:
                self.update(node * 2, start, mid, value, index)
            else:
                self.update(node * 2 + 1, mid + 1, end, value, index)
            self.tree[node] = self.tree[node * 2] + \
                self.tree[node * 2 + 1]  # 값 업데이트


tree = SegmentTree([1, 2, 3, 4, 5, 6, 7])
tree.build(1, 0, 6)
print(tree.tree)
