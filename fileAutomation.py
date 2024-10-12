import shutil
import os
import img2pdf
from PIL import Image

def movingPicts():
    # screenshot number
    start = 297
    end = 317
    targetFolder = "C:/Users/Dell/Desktop/Kihajar STEM 2023 Basic"

    for i in range(start, end + 1):
        # i will be the screenshot number
        source = "C:/Users/Dell/Pictures/Screenshots/Screenshot (" + str(i) + ").png"

        # move the file
        shutil.move(source, targetFolder)

def copyFile():
    basePath = "C:/Users/Dell/Documents/TPB 2024-2025/WI1102/Latihan13102024/"

    # folder analisis kasus, there's 4 file
    # fileCount = 4
    # for i in range(1, fileCount + 1):
    #     source = f"C:/Users/Dell/Documents/Tech-Design/git-github/Berpikir Komputasional K25/TugasKasusPengulangan_13102024/AnalisisKasus/latihan{i}.py"
    #     destination = basePath + f"AnalisisKasus/Latihan{i}/16524069.py"

    #     shutil.copyfile(source, destination)

    # folder pengulangan, there's 6 files
    fileCount = 6
    for j in range(1, fileCount + 1):
        source = f"C:/Users/Dell/Documents/Tech-Design/git-github/Berpikir Komputasional K25/TugasKasusPengulangan_13102024/Pengulangan/latihan{j}.py"
        destination = basePath + f"Pengulangan/Latihan{j}/16524069.py"

        shutil.copyfile(source, destination)

    print("Files Copied!")

def pngToPDF():
    basePath = "C:/Users/Dell/Documents/TPB 2024-2025/WI1102/Latihan13102024/"
    # folder pengulangan, there's 6 image
    fileCount = 6
    for i in range(1, fileCount + 1):
        if i == 4:
            # special case for latihan4, because there's 2 screenshot file
            img_path = basePath + f"Pengulangan/Latihan{i}/screenshotProgram2.png"
            pdf_path = basePath + f"Pengulangan/Latihan{i}/screenshotProgram2.pdf"

            image = Image.open(img_path)
            pdf_bytes = img2pdf.convert(image.filename)

            file = open(pdf_path, "wb")

            file.write(pdf_bytes)

            image.close()

            file.close()

            print("PDF Created!")
        
        img_path = basePath + f"Pengulangan/Latihan{i}/screenshotProgram.png"
        pdf_path = basePath + f"Pengulangan/Latihan{i}/screenshotProgram.pdf"

        image = Image.open(img_path)
        pdf_bytes = img2pdf.convert(image.filename)

        file = open(pdf_path, "wb")

        file.write(pdf_bytes)

        image.close()

        file.close()

        print("PDF Created!")

def removeFile():
    basePath = "C:/Users/Dell/Documents/TPB 2024-2025/WI1102/Latihan13102024/"
    
    fileCount = 6
    for i in range(1, fileCount + 1):
        imagePath = basePath + f"AnalisisKasus/Latihan{i}/screenshotProgram.png"
        if os.path.exists(imagePath):
            os.remove(imagePath)
            print("File Deleted")
        else:
            print("File D.N.E")

def moveFile():
    basePath = "C:/Users/Dell/Documents/TPB 2024-2025/WI1102/Latihan13102024/"

    fileCount = 6
    for i in range(1, fileCount + 1):
        source = basePath + f"flowchart/Pengulangan/Latihan{i}-Pengulangan.pdf"
        destination = basePath + f"Pengulangan/Latihan{i}/pseudocode-flowchart-latihan1.pdf"
        shutil.move(source, destination)
