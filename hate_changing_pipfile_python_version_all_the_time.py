import sys
import subprocess

# get python version number. Thank you google
python_version = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}" 

try:
    # using python to read and write pipfile
    with open("Pipfile", 'r') as file:
        content = file.readlines()

    with open("Pipfile", 'w') as file:
        for line in content:
            # startswith() string methods
            if line.startswith("python_full_version"):
                file.write(f'python_full_version = "{python_version}"\n')
            else:
                file.write(line)
        print("Changed python version in pipfile to installed version \n ************************")
        print("Running pipenv install && pipenv shell now \n ******** You are welcome *******")
        # playing around with try except againx
        try:
            subprocess.run(["pipenv", "install"])
            subprocess.run(["pipenv", "shell"])
        except Exception as error:
            print("Ooops, An error occurred:" , error)

except FileNotFoundError:
    print("Pipfile not found. Creating my own")
    subprocess.run(["pipenv", "install"])
    subprocess.run(["pipenv", "shell"])