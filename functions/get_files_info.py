import os



def get_files_info(working_directory, directory=None):
    try:
        if directory is None:
           directory = "."

        full_path = os.path.join(working_directory, directory)
        
        if not os.path.abspath(full_path).startswith(os.path.abspath(working_directory)):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        
        if not os.path.isdir(full_path):
            return f'Error: "{directory}" is not a directory'

        results = []
        for item in os.listdir(full_path):
            item_path = os.path.join(full_path, item)
            is_dir = os.path.isdir(item_path)
            try:
                file_size = os.path.getsize(item_path)
            except Exception as e:
                return f"Error: Could not get size of '{item}':{str(e)}"


            results.append(f"- {item}: file_size={file_size} bytes, is_dir={is_dir}")

        return "\n".join(results)


    except Exception as e:
        return f"Error: {str(e)}"
