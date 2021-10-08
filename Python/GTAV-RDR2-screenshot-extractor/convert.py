import os
from datetime import datetime

JPEG_HEAD = b'\xff\xd8'
JPEG_TAIL = b'\xff\xd9'

def NewFolder(path):
    try:
        os.makedirs(path)
    except FileExistsError as e:
        if os.path.isfile(path):
            raise e
        else:
            print('Directory "%s" already exists.' %path)

# Create workspace directories.
NewFolder('Unprocessed')
NewFolder('Processed')
NewFolder('Output')

# Read in file list.
ls = os.listdir('Unprocessed')

# Filter the list.
for item in ls:
    # Exclude directories.
    if os.path.isdir(item):
        ls.remove(item)

# Process files in the list.
dateDict = {}
for pic_file in ls:
    with open('Unprocessed/%s' %pic_file, 'rb') as f:
        data = f.read()
        head = data.find(JPEG_HEAD)
        tail = data.find(JPEG_TAIL)

        # Check if there's jpeg inside the file (check if head and tail exist)
        if head + tail == -2:
            print('%s doesn\'t contain a jpeg' %pic_file)
            continue

        # Cut out the jpeg part of the file
        cut = bytearray(data[head:tail + 2])
        with open('./Output/%s.jpg' %pic_file, 'wb') as out:
            out.write(cut)

        # Extract picture taking date (Hex 0E to 2F) and convert to iso format.
        dateStr = datetime.strptime(str(data[14:48:2], encoding='UTF-8'), '%m/%d/%y %H:%M:%S') # example: 01/28/20 11:43:08
        dateStr = dateStr.isoformat()
        dateDict[pic_file] = dateStr

    # Set outputed jpeg with modification time of the original file.
    os.utime('Output/%s.jpg' %pic_file, (os.path.getatime('Unprocessed/%s' %pic_file), os.path.getmtime('Unprocessed/%s' %pic_file)))

    # Move processed file to processed folder
    os.rename('Unprocessed/%s' %pic_file, 'Processed/%s' %pic_file)

    print(pic_file)

# Append dates to dates.txt
with open('Output/dates.txt', 'a') as f:
    for filename, date in dateDict.items():
        d = filename + ' ' + date + '\n'
        f.write(d)

print('Done!')
