import subprocess

if __name__ == "__main__":
    result = subprocess.run(["pytest", "ETLtesting_automation_file.py"], capture_output=True, text=True)
    print(result.stdout)
    if result.returncode != 0:
        print("Tests failed!")
    else:
        print("All tests passed successfully!")
