class Sorters:
    @staticmethod
    def insertion_sort(arr: list[int]) -> list[int]:
        for i in range(len(arr)):
            p = arr[i]
            j = i - 1
            while j > -1 and p < arr[j]:
                arr[j + 1] = arr[j]
                j = j - 1
            arr[j + 1] = p
        return arr

    # build an algorithm that sort from mayor to minor
    @staticmethod
    def reverse_insertion_sort(arr: list[int]) -> list[int]:
        for i in range(len(arr)):
            p = arr[i]
            j = i - 1
            while j > -1 and p > arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = p
        return arr

    @staticmethod
    def selection_sort(arr: list[int]) -> list[int]:
        for i in range(len(arr)):
            minimum = i
            for j in range(i, len(arr)):
                if arr[minimum] > arr[j]:
                    minimum = j
            arr[i], arr[minimum] = arr[minimum], arr[i]
        return arr
    
    @staticmethod 
    def bubble_sort(arr: list[int]) -> list[int]:
        for i in range(len(arr)):
            for j in range(i, len(arr) - 1): 
                if arr[j] > arr[j + 1]: 
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr 