import filecmp
import sys
import os
from googleapiclient.discovery import build

from upload_file import upload_basic, get_cred
from delete_file import delete_file
from download_file import print_file_metadata
from download_file import download_file
from list_file import main


print(sys.argv)
if len(sys.argv)==2:
    argument= sys.argv[1]
    if argument =='--file':
        main()


elif len(sys.argv) ==3:
    argument= sys.argv[1]
    filepath = sys.argv[2]
    mimes = {
        '.doc':'application/msword',
        '.gif':'image/gif',
        '.html':'text/html',
        '.jpg':'image/jpg',
        '.js':'text/javascript',
        '.mp3':'audio/mpeg',
        '.mp4':'video/mp4',
        '.pdf':'application/pdf',
        '.png':'image/png',
        '.ppt':'application/vnd.ms-powerpoint'

        }
    cred = get_cred()
    name,ext = os.path.splitext(filepath)
    mime = mimes.get(ext,None)
    if argument =='--upload':  
        if mime:
            upload_basic(cred, filepath, mime)
            print('File uploaded sucessfully')
        else:
            print('File Extension not found')
    elif argument=='--download':
        service = build('drive', 'v3', credentials=cred)
        file=print_file_metadata(service,filepath)
        if file:
           f = open(file.get('name','file'), 'wb')
           download_file(service, filepath, f)
        else:
           print('File not found')
    
    elif argument=='--delete':
        service = build('drive', 'v3', credentials=cred)
        delete_file(service, filepath)
        print('file deleted successfully')
    else:
        print('not a valid argument')

else:
    print('no argument provided')
    print('--upload filename: used to upload file to google drive')
    print('--file: used to list all the files in google drive')
    print('--download filename: used to download file to google drive ')
    print('--delete filename: used to delete file from google drive')

