FILEPATH = 'todos.txt'


def get_todo(filename=FILEPATH):
    """ Read a Text File and Return the list of to-do items. """
    with open(filename, 'r') as local_file:
        local_todos = local_file.readlines()
    return local_todos


def write_todo(todo_args, filename=FILEPATH):
    """ Write the list of to-do items in the text file. """
    with open(filename, 'w') as file_local:
        file_local.writelines(todo_args)


print(__name__)
if __name__ == "__main__":
    print("Hello")
    print(get_todo())