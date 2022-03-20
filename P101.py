import dropbox
import os

class TranferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self,file_from, file_to):
        dbx= dropbox.Dropbox(self.access_token)

        for root, dirs, files in os.walk(file_from):
            
            for filename in files:
                local_path = os.path.join(root, filename)
            
                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)

                with open(file_from, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode= WriteMode('overwrite'))

def main():
    access_token = 'sl.BEJDkwZQ9FMYbqoELpUbZJnV4RS51F-6jKSkTKI0ct-5WO2bXeYq7peVUWwNh-FVzFGzLRwbni38HWIjDiAWewTHYYBP9uHe8aOWVOB9hbc7Mp0jMOgFad1VP-wXgnZDsrC9-nTmBDKq'
    tranferData = TranferData(access_token)

    file_from = input('Enter a file upload: ')
    file_to = input('Enter the path to dropbox: ')

    tranferData.upload_file(file_from, file_to)
    print('It is a success')

main()