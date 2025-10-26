def descend_insertion_sort(my_list):
    for i in range(1, len(my_list)):
        temp = my_list[i]
        j = i-1
        while temp > my_list[j] and j < -1:
            my_list[j+1] = my_list[j]
            my_list[j] = temp
            j -= 1
        return my_list

def ascend_insertion_sort(my_list):
    for i in range(1, len(my_list)):
        temp = my_list[i]
        j = i-1
        while temp < my_list[j] and j > -1:
            my_list[j+1] = my_list[j]
            my_list[j] = temp
            j -= 1
        return my_list
    
def descend_selection_sort(my_List):
    for i in range(len(my_List)):
        min_index = i
        for j in range(i+1, len(my_List)):
            if my_List[j] > my_List[min_index]:
                min_index = j
        my_List[i], my_List[min_index] = my_List[min_index], my_List[i]
    return my_List

def ascend_selection_sort(my_List):
    for i in range(len(my_List)):
        min_index = i
        for j in range(i+1, len(my_List)):
            if my_List[j] < my_List[min_index]:
                min_index = j
        my_List[i], my_List[min_index] = my_List[min_index], my_List[i]
    return my_List

list_angka = [4,2,6,5,1,3]

while True:
        print("\nMenu")
        print("1. Input Data")
        print("2. Sorting Ascending (Insertion Sort)")
        print("3. Sorting Descending (Insertion Sort)")
        print("4. Sorting Ascending (Selection Sort)")
        print("5. Sorting Descending (Selection Sort)")
        print("6. Keluar Program")

        menu = input("Pilih Menu: ")
        if menu == '1':
            insert_angka = input("Masukkan Angka yang mau di sorting : ")
            insert_angka = list_angka
        elif menu == '2':
            print(descend_insertion_sort(list_angka))
        elif menu == '3':
            print(ascend_insertion_sort(list_angka))
        elif menu == '4':
            print(ascend_selection_sort(list_angka))
        elif menu == '5':
            print(descend_selection_sort(list_angka))
        elif menu == '6':
            print("Terima Kasih")
            exit()
        else:
            print("Menu Tidak Ada")
