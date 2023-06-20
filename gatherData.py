# Helper script for getting data from gDrive folder specified in the readme
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LocalWebserverAuth() # client_secrets.json need to be in the same directory as the script
drive = GoogleDrive(gauth)

fileList = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
for file in fileList:
  print('Title: %s, ID: %s' % (file['title'], file['id']))
  # Get the folder ID that you want
  if(file['title'] == "To Share"):
      fileID = file['id']
	  

driveFolder = '1YYTOxT2lOmt63dbXkWlwy7lpjygEYse5'
#down.downloadFolder(driveFolder, destinationFolder = outputDir)