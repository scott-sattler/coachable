# no imports

class Sort:

    @staticmethod
    def insertion_sort(arr: list) -> list:
        n = len(arr)
        for i in range(1, n):
            key = arr[i]
            j = i - 1
            while j > -1 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key

        return arr

    @staticmethod
    def selection_sort(arr: list) -> list:

        n = len(arr)
        for i in range(0, n):

            min_index = i
            j = i + 1
            while j < n:
                if arr[j] < arr[min_index]:
                    min_index = j
                j += 1

            arr[i], arr[min_index] = arr[min_index], arr[i]

        return arr

