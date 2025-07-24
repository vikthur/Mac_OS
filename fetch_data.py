from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

# Authenticate and create PyDrive client
gauth = GoogleAuth()
gauth.LocalWebserverAuth()  # Opens browser for authentication
drive = GoogleDrive(gauth)

# Replace with your actual file ID from Google Drive shareable link
file_id = 'YOUR_FILE_ID_HERE'

# Fetch and download the file
file = drive.CreateFile({'id': file_id})
file_name = file['title']
file.GetContentFile(file_name)

print(f"File '{file_name}' downloaded successfully.")
