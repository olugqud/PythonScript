import zipfile

def crack_zip(zip_file, wordlist):
    """Cracks a zip file using a wordlist"""
    with open(wordlist, 'r') as f:
        passwords = f.readlines()
    zip_file = zipfile.ZipFile(zip_file)
    for password in passwords:
        password = password.strip()
        try:
            zip_file.extractall(pwd=password.encode())
            print(f"[+] Password found: {password}")
            return True
        except:
            pass
    print("[-] Password not found")
    return False
