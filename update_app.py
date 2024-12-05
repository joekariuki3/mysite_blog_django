import subprocess
import sys

# Check if we have the correct number of arguments
if len(sys.argv) != 4:
    print("Usage: python run_bash_script.py FILE_NAME BRANCH_NAME REPOSITORY_NAME")
    sys.exit(1)


# Get the arguments from the command line
file_name = sys.argv[1]  # Bash script file
branch_name = sys.argv[2]  # Branch name
repository_name = sys.argv[3]  # Repository name

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
