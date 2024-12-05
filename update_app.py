import subprocess

# Define the path to the bash script
bash_script = './updateApplication.sh'

# Run the bash script using subprocess
try:
    result = subprocess.run([bash_script], check=True,
                            text=True, capture_output=True)

    # Print the output of the bash script
    print("Bash script output:")
    print(result.stdout)

except subprocess.CalledProcessError as e:
    # Handle any errors that occur during the execution
    print(f"An error occurred while running the bash script: {e}")
    print(f"Error output: {e.stderr}")
