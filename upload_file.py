import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload
from utils import get_cred


#uploading a file
def upload_basic(creds, filename, mimetype='image/jpg'):
    try:
        # create drive api client
        service = build('drive', 'v3', credentials=creds)

        file_metadata = {'name': filename}

        media = MediaFileUpload(filename=filename,mimetype=mimetype)
        # pylint: disable=maybe-no-member
        file = service.files().create(body=file_metadata, media_body=media,fields='id').execute()
        print(F'File ID: {file.get("id")}')
    except HttpError as error:
        print(F'An error occurred: {error}')
        file = None

    return file.get('id')


if __name__ == '__main__':
    creds=get_cred()
    print(creds)
    upload_basic(creds)