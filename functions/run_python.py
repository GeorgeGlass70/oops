import os
import subprocess


def run_python_file(working_directory, file_path):

    working_dir_abs = os.path.abspath(working_directory)

    file_abs_path = os.path.abspath(os.path.join(working_dir_abs, file_path))

    if not file_abs_path.startswith(working_dir_abs):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if not os.path.isfile(file_abs_path):
        return f'Error: File "{file_path}" not found.'

    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'

    try:

        result = subprocess.run(
            ['python', file_path],
            cwd = working_directory,
            timeout = 30,
            capture_output = True,
            text = True
        )


        stdout = result.stdout.strip()
        stderr = result.stderr.strip()

        output = []
        if stdout:
            output.append(f"STDOUT: {stdout}")
        if stderr:
            output.append(f"STDERR: {stderr}")

        
        if result.returncode != 0:
            output.append(f"Process exited with code {result.returncode}")

        if not output and result.returncode == 0:
            return "No output produced."

        return "\n".join(output)


    except subprocess.TimeoutExpired:
        return f"Error: executing Python file: Timeout expired after 30 seconds."

    except Exception as e:
        return f"Error: executing Python file: {e}"
