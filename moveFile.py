import shutil

# screenshot number
start = 297
end = 317
targetFolder = "C:/Users/Dell/Desktop/Kihajar STEM 2023 Basic"

for i in range(start, end + 1):
    # i will be the screenshot number
    source = "C:/Users/Dell/Pictures/Screenshots/Screenshot (" + str(i) + ").png"

    # move the file
    shutil.move(source, targetFolder)
