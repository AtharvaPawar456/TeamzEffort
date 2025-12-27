import os


def renameAllFiles(folderPath):
    """
    Renames all files inside a folder sequentially.

    Input:
        folderPath (str): Target directory path

    Working:
        - Iterates through all files
        - Renames each file to file_<number> with original extension
    """
    try:
        files = sorted(os.listdir(folderPath))
        fileCounter = 1
        # fileCounter = 112

        for fileName in files:
            oldPath = os.path.join(folderPath, fileName)

            if not os.path.isfile(oldPath):
                continue

            _, extension = os.path.splitext(fileName)
            newFileName = f"file_{fileCounter}{extension}"
            newPath = os.path.join(folderPath, newFileName)

            os.rename(oldPath, newPath)
            fileCounter += 1

        print(f"Renamed {fileCounter - 1} files in '{folderPath}' successfully.")

    except Exception as error:
        print(f"Error: {error}")


folderList = [
    "kadam",
    "kadam/kadam-ai-avatar/avatar-1-imgs",
    "kadam/kadam-ai-avatar/avatar-1-shorts",
    "kadam/kadam-ai-avatar/avatar-2-shorts",

]

# for folder in folderList:
#     renameAllFiles(folder)



folderName = folderList[0]
files = os.listdir(folderName)





tempPath = "https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/ai-profile-imgs/kadam/"

# tempPath = "https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/ai-profile-imgs/kadam/kadam-ai-avatar/avatar-1-imgs/"
# tempPath = "https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/ai-profile-imgs/kadam/kadam-ai-avatar/avatar-1-shorts/"

# tempPath = "https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/ai-profile-imgs/kadam/kadam-ai-avatar/avatar-2-imgs/"


for fileName in files:
    print(f"{tempPath}{fileName};")
    # print(f"'{tempPath}{fileName}',")



"""
https://raw.githubusercontent.com/AtharvaPawar456/HandMadeProjects/refs/heads/main/siteimages/teampics/AakashShinde.png;https://raw.githubusercontent.com/AtharvaPawar456/HandMadeProjects/refs/heads/main/siteimages/teampics/YashChavan.jpg;https://raw.githubusercontent.com/AtharvaPawar456/HandMadeProjects/refs/heads/main/siteimages/teampics/AtharvaPawar.jpg
"""