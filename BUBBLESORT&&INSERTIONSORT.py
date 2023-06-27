#Nama  : Syarif Mohammad Syakur
#NIM   : F55121020
#Kelas : A

import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def print_iteration(iteration, arr):
    print(f"Iterasi ke-{iteration}: {arr}")

def print_before_after(sort_type, arr):
    print(f"\nSebelum pengurutan ({sort_type}):")
    print(arr)
    sorted_arr = sorted(arr)
    print(f"Sesudah pengurutan ({sort_type}):")
    print(sorted_arr)

def compute_sorting_time(sort_type, arr):
    start_time = time.time()
    if sort_type == "bubble":
        bubble_sort(arr)
    elif sort_type == "insertion":
        insertion_sort(arr)
    end_time = time.time()
    return end_time - start_time

def main():
    arr = [12, 99, 62, 15, 20, 95, 39, 48, 3, 24, 8, 43, 74, 19, 97, 33, 49, 68, 55, 33, 90, 90, 7, 26, 85, 46, 39, 40, 9, 36, 60, 64, 89, 31, 25, 71, 21, 23, 63, 84, 32, 5, 3, 44, 21, 10, 21, 17, 50, 2, 36, 53, 79, 54, 19, 88, 1, 32, 31, 15, 6, 3, 1, 40, 22, 43, 18, 1, 77, 9, 59, 40, 7, 41, 81]
    print("Nama     : Syarif Mohammad Syakur")
    print("Nim      : F55121020")
    print("Kelas    : A")
    print("=== Program Sorting Menggunakan Bubble Sort dan Insertion Sort ===")
    print("Pilihan: ")
    print("1. Insertion Sort")
    print("2. Bubble Sort")
    choice = input("Silahkan pilih operasi pengurutan yang ingin dilakukan (1 atau 2): ")

    if choice == "1":
        sort_type = "Bubble Sort"
    elif choice == "2":
        sort_type = "Insertion Sort"
    else:
        print("Pilihan tidak tersedia. Harap masukkan pilihan dengan tepat.")
        return

    print_before_after("Sebelum pengurutan", arr)
    sorting_time = compute_sorting_time(sort_type, arr)
    print_before_after("Setelah pengurutan", arr)

    print("\nHasil 5 iterasi pertama:")
    for i in range(5):
        print_iteration(i + 1, arr)
        if sort_type == "Bubble Sort":
            bubble_sort(arr)
        elif sort_type == "Insertion Sort":
            insertion_sort(arr)

    print("\nHasil 5 iterasi terakhir:")
    for i in range(len(arr) - 5, len(arr)):
        print_iteration(i + 1, arr)

    print(f"\nWaktu komputasi pengurutan: {sorting_time:.6f} detik")

main()