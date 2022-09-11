from ast import Delete
from apiclient import errors
from utils import get_cred
from googleapiclient.discovery import build
def delete_file(service, file_id):
  """Permanently delete a file, skipping the trash.

  Args:
    service: Drive API service instance.
    file_id: ID of the file to delete.
  """
  try:
    service.files().delete(fileId=file_id).execute()
  except errors.HttpError as error:
    print ('An error occurred: {error}')

if __name__ == '__main__':
    creds=get_cred()
    print(creds)
    file_id='16w2PRqstAjMV1yIopS5Sn44nAioPQG21'
    service = build('drive', 'v3', credentials=creds)
    delete_file(service,file_id)
    print('item Delete')