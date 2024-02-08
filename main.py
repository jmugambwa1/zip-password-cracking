import zipfile

def crack_password(password_list, zip_file):
    with open(password_list, 'r') as file:
        for line in file:
            password = line.strip()  # Remove any leading/trailing whitespace
            try:
                with zipfile.ZipFile(zip_file, 'r') as zf:
                    zf.extractall(pwd=password.encode())
                print("Password found:", password)
                return True
            except Exception as e:
                # If the password is wrong go to the next one
                continue
    return False

password_list = input("Enter the location of the password list: ")
zip_file = input("Enter the name and path of the .ZIP file: ")

if crack_password(password_list, zip_file):
    print("Password found!")
else:
    print("Password not found!")

