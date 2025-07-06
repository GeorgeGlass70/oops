import os



def write_file(working_directory, file_path, content):



    working_dir_abs = os.path.abspath(working_directory)

    abs_file_path = os.path.abspath(os.path.join(working_dir_abs, file_path))

    if not abs_file_path.startswith(working_dir_abs):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'


    dir_name = os.path.dirname(abs_file_path)
    if not os.path.exists(dir_name):
        try:
            os.makedirs(dir_name)
        except Exception as e:
            return f'Error: Could not create directory {dir_name} ({str(e)})'

    try:
        with open(abs_file_path, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f'Error: {str(e)}'
