class Sort_Algorithms(object):
    def __repr__(self):
        sort_me = [64654, 90, 0, -5, 232, -8, 46, 65, 2, 31, 2]
        result = str("\t[ Sorting Algorithms in Python ]\n"
                     f"Bubble Sort:             {self.bubble_sort(sort_me)}\tBig-O:     O(n^2)\n"
                     f"Selection Sort:          {self.selection_sort(sort_me)}\tBig-O:  O(n^2)\n"
                     f"Insertion Sort:          {self.insertion_sort(sort_me)}\tBig-O:  O(n^2)\n"
                     f"Heap Sort:               {self.heap_sort(sort_me)}\tBig-O:       O(nlog(n))\n"
                     f"Merge Sort:          {self.merge_sort(sort_me)}\tBig-O:          O(nlog(n))\n"
                     f"Quick Sort:          {self.quick_sort(sort_me)}\tBig-O:          O(n)\n")
        return result

    def bubble_sort(self, nums):
        swapped = True
        while swapped:
            swapped = False
            for i in range(len(nums) - 1):
                if nums[i] > nums[i+1]:
                    nums[i], nums[i+1] = nums[i+1], nums[i]
                    swapped = True
        return nums

    def selection_sort(self, nums):
        for i in range(len(nums)):
            lowest_value_index = i
            for j in range(i+1, len(nums)):
                if nums[j] < nums[lowest_value_index]:
                    lowest_value_index = j
            nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]
        return nums

    def insertion_sort(self, nums):
        for i in range(1, len(nums)):
            item_to_insert = nums[i]
            j = i - 1
            while j >= 0 and nums[j] > item_to_insert:
                nums[j+1] = nums[j]
                j -= 1
            nums[j+1] = item_to_insert
        return nums

    def heap_sort(self, nums):
        def heapify(nums, heap_size, root_index):
            largest = root_index
            left_side = (2 * root_index) + 1
            right_side = (2 * root_index) + 2

            if left_side < heap_size and nums[left_side] > nums[largest]:
                largest = left_side

            if right_side < heap_size and nums[right_side] > nums[largest]:
                largest = right_side

            if largest != root_index:
                nums[root_index], nums[largest] = nums[largest], nums[root_index]
                heapify(nums, heap_size, largest)

        def heap_sorter(nums):
            n = len(nums)

            for i in range(n, -1, -1):
                heapify(nums, n, i)

            for i in range(n-1, 0, -1):
                nums[i], nums[0] = nums[0], nums[i]
                heapify(nums, i, 0)
        heap_sorter(nums)
        return nums

    def merge_sort(self, nums):
        def merge(left_side, right_side):
            sorted_nums = []
            left_side_idx = right_side_idx = 0
            left_side_length, right_side_length = len(
                left_side), len(right_side)

            for _ in range(left_side_length + right_side_length):
                if left_side_idx < left_side_length and right_side_idx < right_side_length:
                    if left_side[left_side_idx] <= right_side[right_side_idx]:
                        sorted_nums.append(left_side[left_side_idx])
                        left_side_idx += 1
                    else:
                        sorted_nums.append(right_side[right_side_idx])
                        right_side_idx += 1
                elif left_side_idx == left_side_length:
                    sorted_nums.append(right_side[right_side_idx])
                    right_side_idx += 1
                elif right_side_idx == right_side_length:
                    sorted_nums.append(left_side[left_side_idx])
                    left_side_idx += 1
            return sorted_nums

        def merge_sorter(nums):
            if len(nums) <= 1:
                return nums
            mid = len(nums) // 2
            left_side = merge_sorter(nums[:mid])
            right_side = merge_sorter(nums[mid:])
            return merge(left_side, right_side)
        merge_sorter(nums)
        return nums

    def quick_sort(self, nums):
        def partition(nums, low, high):
            pivot = nums[(low + high) // 2]
            i = low - 1
            j = high + 1
            while True:
                i += 1
                while nums[i] < pivot:
                    i += 1
                j -= 1
                while nums[j] > pivot:
                    j -= 1
                if i >= j:
                    return j
                nums[i], nums[j] = nums[j], nums[i]

        def quick_sorter(nums):
            def _quick_sorter(items, low, high):
                if low < high:
                    split_index = partition(items, low, high)
                    _quick_sorter(items, low, split_index)
                    _quick_sorter(items, split_index+1, high)

            _quick_sorter(nums, 0, len(nums) - 1)
        quick_sorter(nums)
        return nums


print(Sort_Algorithms())
