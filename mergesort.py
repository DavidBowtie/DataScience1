# Bereinigung 1: Imports an den Anfang
import matplotlib.pyplot as plt

# Bereinigung 2: list_to_sort_by_merge in arr umbenannt (zu)
# Bereinigung 3: mergeSort in merge_sort umbenannt (in snake_case nach PEP8)
def merge_sort(arr):
    # Bereinigung 4: Docstring hinzugefügt
    """Sortiert eine Liste mit dem Mergesort-Algorithmus"""
    # Bereinigung 5: IF Bedingung vereinfacht
    if len(arr) > 1:
        # Bereinigung 6: Bessere Variablennamen  (nicht mid, left, right)
        mid_index = len(arr) // 2
        left_half = arr[:mid_index]
        right_half = arr[mid_index:]

        merge_sort(left_half)
        merge_sort(right_half)

        # Bereinigung 7: Bessere Variablennamen (nicht l, r, i)
        left_index = 0
        right_index = 0
        main_index = 0

        while left_index < len(left_half) and right_index < len(right_half):
            if left_half[left_index] <= right_half[right_index]:
                # Bereinigung 8: Unnötige ASSIGNMENT-Methode entfernt
                arr[main_index] = left_half[left_index]
                left_index += 1
            else:
                # Bereinigung 9: Unnötige ASSIGNMENT-Methode entfernt
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


# Plotting

my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
original_list = list(my_list) 

plt.figure(figsize=(12, 5))

# Plot 1: Liste vor Sortierung
plt.subplot(1, 2, 1)
plt.bar(range(len(my_list)), original_list, color='skyblue')
plt.title("Vorher")
plt.xlabel("Index")
plt.ylabel("Wert")

merge_sort(my_list) # Sortiere die Liste

# Plot 2: Liste nach Sortierung
plt.subplot(1, 2, 2)
plt.bar(range(len(my_list)), my_list, color='lightcoral')
plt.title("Nachher")
plt.xlabel("Index")
plt.ylabel("Wert")

plt.tight_layout() # Passt Layout an
plt.show() # Zeigt die Plots an
