import zipfile

def extractFile(zfile, password):
    try:
        zfile.extractall(pwd= bytes(password, 'utf=8'))
        return password
    except Exception as e:
        print(f'Failed to extract with password "{password}": {e}')
        return None

def main():
    zfile = zipfile.ZipFile('test.zip')
    with open('passlist.txt', 'r', encoding='utf-8') as passFile:
        for line in passFile:
            password = line.strip()
            guess = extractFile(zfile, password)
            if guess:
                print(f'Password: {password}')
                break
        else:
            print('Password not found in the list.')

if __name__ == '__main__':
    main()