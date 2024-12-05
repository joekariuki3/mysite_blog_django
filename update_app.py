import subprocess
import sys
import os
import stat
from dotenv import load_dotenv

load_dotenv()

# Define the error message for incorrect usage
error_message = "Usage: update_app.py BASH_SCRIPT_FILE_NAME.sh BRANCH_NAME REPOSITORY_NAME"


# Get the file name, branch name and repository name from environment variables
environment = os.environ.get('ENVIRONMENT')
file_name = os.getenv('BASH_SCRIPT_FILE_NAME',
                      'updateApplication.sh')  # Bash script file
repository_name = os.environ.get('REPOSITORY_NAME')  # Repository name
if environment == 'testing':
    branch_name = os.environ.get(
        'TESTING_BRANCH_NAME', 'testing')  # Branch name
else:
    branch_name = os.environ.get('MAIN_BRANCH_NAME')  # Branch name

# make sure file_name, branch_name and repository_name are provided in the environment file else exit with error and ask user to provide
if not file_name or not branch_name or not repository_name:
    print("Error: BASH_SCRIPT_FILE_NAME, BRANCH_NAME and REPOSITORY_NAME environment variables are required.")
    print(error_message)
    sys.exit(1)

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
