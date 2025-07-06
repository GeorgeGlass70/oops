import os

MAX_CHARS = 10000

def get_file_content(working_directory, file_path):
    
    try:
        working_dir_abs = os.path.abspath(working_directory)

        file_abs_path = os.path.abspath(os.path.join(working_dir_abs, file_path))

        if not file_abs_path.startswith(working_dir_abs):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(file_abs_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        file_size = os.path.getsize(file_abs_path)

        with open(file_abs_path, "r") as f:
            file_content = f.read(MAX_CHARS)
            if file_size > MAX_CHARS:
                file_content += f'[... File "{file_path}" truncated at {MAX_CHARS} characters]'

        return file_content


    except Exception as e:
        return f"Error: {str(e)}"
