def myzip(arrnames, arrnumbers):
    return list(zip(arrnames, arrnumbers))

def paz_myzip():
    arr_names = ['Paz', 'Eyal', 'Soli']
    arr_numbers = [1, 2, 3]

    expected_result = [('Paz', 1), ('Eyal', 2), ('Soli', 3)]
    zipped_list = myzip(arr_names, arr_numbers)
    assert zipped_list == expected_result
    print("Shalom Eyal you passed the test!", str(zipped_list))

if __name__ == "__main__":
    paz_myzip()
