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
        # fileCounter = 1
        fileCounter = 112

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
    # "dxn-2in1",
    # "dxn-butterfly-pea",
    # "dxn-cocozhi",
    # "dxn-cordi-coffee",
    # "DXN-Cow-Ghee",
    # "dxn-jaggery",
    # "dxn-kiwi-drink-bottle",
    # "dxn-lemonzhi",
    # "dxn-massage-oil",
    # "DXN-Material",
    # "dxn-shampo",
    # "dxn-soap",
    # "dxn-spirulina",
    # "dxn-spirulina-cereal",
    # "dxn-tailam",
    # "dxn-tooth-paste",
    # "dxn-virgin-oil",
    "dxn-2in1-v2"
]

for folder in folderList:
    renameAllFiles(folder)


# files = os.listdir("dxn-2in1")
# files = os.listdir("dxn-cocozhi")
# files = os.listdir("dxn-tooth-paste")


# tempPath = "https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/dxnproductsimages/Dxn%20Spirulina.png"
# tempPath = "https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/dxnproductsimages/dxn-2in1/"
# tempPath = "https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/dxnproductsimages/dxn-cocozhi/"
# tempPath = "https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/dxnproductsimages/dxn-tooth-paste/"
# for fileName in files:
#     print(f"'{tempPath}{fileName}',")





