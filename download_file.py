from apiclient import errors
from apiclient import http
from googleapiclient.discovery import build
from utils import get_cred
# ...

def print_file_metadata(service, file_id):
  """Print a file's metadata.

  Args:
    service: Drive API service instance.
    file_id: ID of the file to print metadata for.
  """
  try:
    file = service.files().get(fileId=file_id).execute()
    # print(file)
    print ('Title: ',file['name'])
    print ('MIME type: ', file['mimeType'])
    return file
  except errors.HttpError as error:
    print ('An error occurred:', error)


def print_file_content(service, file_id):

  try:
    print (service.files().get_media(fileId=file_id).execute())
  except errors.HttpError as error:
    print ('An error occurred: %s' , error)


def download_file(service, file_id, local_fd):
  #Download a Drive file's content to the local filesystem.

  request = service.files().get_media(fileId=file_id)
  media_request = http.MediaIoBaseDownload(local_fd, request)

  while True:
    try:
      download_progress, done = media_request.next_chunk()
    except errors.HttpError as  error:
      print ('An error occurred:' , error)
      return
    if download_progress:
      print ('Download Progress: %d%%' , int(download_progress.progress() * 100))
    if done:
      print ('Download Complete')
      return




if __name__ == '__main__':
    creds=get_cred()
    print(creds)
    file_id='1-0Wg6n8pjyCTsgVZHOnKeu8U4ylUabJl'
    service = build('drive', 'v3', credentials=creds)
    file=print_file_metadata(service,file_id)
    if file:
        f = open(file.get('name','file'), 'wb')
        download_file(service, file_id, f)
    else:
        print('File not found')