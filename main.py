from sorters import Sorters


arr: int = [5, 4, 3, 2, 1]

def main(): 
    print('bubble sort: ')
    print(Sorters.bubble_sort(arr))
    print('\nselection sort: ')
    print(Sorters.selection_sort(arr))

main()