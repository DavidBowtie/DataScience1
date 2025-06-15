#Bereinigung 1: Imports an den Anfang
import matplotlib.pyplot as plt

#Bereinigung 2: list_to_sort_by_merge in arr umbenannt (zu)
def mergeSort(arr):
    #Bereinigung 3: IF Bedingung vereinfacht
    if len(arr) > 1:
        #Bereinigung 4: Bessere Variablennamen  (nicht mid, left, right)
        mid_index = len(arr) // 2
        left_half = arr[:mid_index]
        right_half = arr[mid_index:]

        mergeSort(left_half)
        mergeSort(right_half)

        #Bereinigung 5: Bessere Variablennamen (nicht l, r, i)
        left_index = 0
        right_index = 0
        main_index = 0

        while left_index < len(left_half) and right_index < len(right_half):
            if left_half[left_index] <= right_half[right_index]:
                #Bereinigung 6: Unnötige ASSIGNMENT-Methode entfernt
                arr[main_index] = left_half[left_index]
                left_index += 1
            else:
                #Bereinigung 7: Unnötige ASSIGNMENT-Methode entfernt
                arr[main_index] = right_half[right_index]
                right_index += 1
            main_index += 1

        while left_index < len(left_half):
            arr[main_index] = left_half[left_index]
            left_index += 1
            main_index += 1

        while right_index < len(right_half):
            arr[main_index] = right_half[right_index]
            right_index += 1
            main_index += 1


my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
x = range(len(my_list))
plt.plot(x, my_list)
plt.show()
mergeSort(my_list)
x = range(len(my_list))
plt.plot(x, my_list)
plt.show()
