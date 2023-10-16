import pickle

def dump_list_of_lists_to_file(data, file_path):
    with open(file_path, 'wb') as file:
        pickle.dump(data, file)

my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
file_path = 'data.bin'

dump_list_of_lists_to_file(my_list, file_path)
