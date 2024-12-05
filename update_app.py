import subprocess
import sys
import os
import stat

# Define the error message for incorrect usage
error_message = "Usage: update_app.py BASH_SCRIPT_FILE_NAME.sh BRANCH_NAME REPOSITORY_NAME"

# Check if we have the correct number of arguments
if len(sys.argv) != 4:
    print(error_message)
    sys.exit(1)


# Get the arguments from the command line
file_name = sys.argv[1]  # Bash script file
branch_name = sys.argv[2]  # Branch name
repository_name = sys.argv[3]  # Repository name

# Check if the file exists
if not os.path.isfile(file_name):
    print(f"Error: The file '{file_name}' does not exist.")
    print(error_message)
    sys.exit(1)

# Prepend './' to the file name if it's in the current directory
if not file_name.startswith('./'):
    file_name = f'./{file_name}'

# Check if the file has execution permission
file_stat = os.stat(file_name)
if not bool(file_stat.st_mode & stat.S_IXUSR):
    print(
        f"'{file_name}' does not have execution rights. Granting execution permission.")
    # Grant user execute (u+x) permission
    os.chmod(file_name, file_stat.st_mode | stat.S_IXUSR)

# Run the bash script using subprocess
try:
    result = subprocess.run([file_name, branch_name, repository_name], check=True,
                            text=True, capture_output=True)

    # Print the output of the bash script
    print(f"{file_name[2:]} script output:")
    print(result.stdout)

except subprocess.CalledProcessError as e:
    # Handle any errors that occur during the execution
    print(f"An error occurred while running the bash script: {e}")
    print(f"Error output: {e.stderr}")
