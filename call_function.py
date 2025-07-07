from google.genai import types

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info, schema_get_file_content, schema_run_python_file, schema_write_file
    ]
)


schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Lists content of a file, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path in which the content is listed from, relative to the working directory.",
            ),
        },
    ),
)



schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Lists content of a file, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path in which the content is listed from, relative to the working directory.",
            ),
        },
    ),
)


schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs a python file, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path in which the python file is being run from, relative to the working directory.",
            ),
        },
    ),
)



schema_write_file = types.FunctionDeclaration(
    name="get_file_content",
    description="Lists content of a file, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path in which the content is listed from, relative to the working directory.",
            ),
        },
    ),
)
