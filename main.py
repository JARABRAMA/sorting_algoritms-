from sorters import Sorters


arr: int = [5, 4, 3, 2, 1]

def main(): 
    print('bubble sort: ',Sorters.bubble_sort(arr))
    print('\nselection sort: ', Sorters.insertion_sort(arr))

main()