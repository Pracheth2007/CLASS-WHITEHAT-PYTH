import dropbox

class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token
    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        f=open(file_from,'rb')
        dbx.files_upload(f.read(),file_to)

def main():
    access_token='sl.AmW8u8aIs-TjRRIoExU7EdSYTeKrRqa-V7PVHc1oaEY_1LjV93tPxyokNmTkb3tcKkG0BtuOa6DMGpXsaCWBahaojk-wtJWA05ZiEJji9dYxzFzQ-h__HNZiDacK4Wk5zxmgn4k'
    transferData=TransferData(access_token)

    file_from=input("Enter File Path")
    file_to=input("Enter The File Path Of DropBox")

    transferData.upload_file(file_from,file_to)
    print("File Has Been Moved Successfully! Congratulations!")

main()
