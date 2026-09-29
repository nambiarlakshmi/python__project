def insert(heap, value):
    heap.append(value)
    return heap


def build_heap(values):
    heap = []

    for value in values:
        insert(heap, value)

    return heap

values = [10, 3, 7, 1, 8]
heap = build_heap(values)
print("Fibonacci Heap:", heap)
insert(heap, 2)
print("After inserting 2:", heap)