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
    "dxn-cocozhi",
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
    # "dxn-virgin-oil"
]

for folder in folderList:
    renameAllFiles(folder)


files = os.listdir("dxn-2in1")


# tempPath = "https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/dxnproductsimages/Dxn%20Spirulina.png"
# tempPath = "https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/dxnproductsimages/dxn-2in1/"
# for fileName in files:
#     print(f"{tempPath}{fileName};")







# https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/dxnproductsimages/dxn-2in1/file_34.png
# https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/dxnproductsimages/dxn-2in1/file_35.jpeg
# https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/dxnproductsimages/dxn-2in1/file_36.png
# https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/dxnproductsimages/dxn-2in1/file_37.png
# https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/dxnproductsimages/dxn-2in1/file_38.png
# https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/dxnproductsimages/dxn-2in1/file_39.png
# https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/dxnproductsimages/dxn-2in1/file_4.png
# https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/dxnproductsimages/dxn-2in1/file_40.png
# https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/dxnproductsimages/dxn-2in1/file_41.png
# https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/dxnproductsimages/dxn-2in1/file_42.png
# https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/dxnproductsimages/dxn-2in1/file_43.png
# https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/dxnproductsimages/dxn-2in1/file_44.png
# https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/dxnproductsimages/dxn-2in1/file_45.jpeg
# https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/dxnproductsimages/dxn-2in1/file_46.jpeg
# https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/dxnproductsimages/dxn-2in1/file_47.png
# https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/dxnproductsimages/dxn-2in1/file_48.jpeg
# https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/dxnproductsimages/dxn-2in1/file_49.png
# https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/dxnproductsimages/dxn-2in1/file_5.png
# https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/dxnproductsimages/dxn-2in1/file_50.png
# https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/dxnproductsimages/dxn-2in1/file_51.png
# https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/dxnproductsimages/dxn-2in1/file_52.jpeg
# https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/dxnproductsimages/dxn-2in1/file_53.jpeg
# https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/dxnproductsimages/dxn-2in1/file_54.png
# https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/dxnproductsimages/dxn-2in1/file_55.jpeg
# https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/dxnproductsimages/dxn-2in1/file_56.png
# https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/dxnproductsimages/dxn-2in1/file_57.jpeg
# https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/dxnproductsimages/dxn-2in1/file_58.png
# https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/dxnproductsimages/dxn-2in1/file_59.jpeg
# https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/dxnproductsimages/dxn-2in1/file_6.png
# https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/dxnproductsimages/dxn-2in1/file_60.png
# https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/dxnproductsimages/dxn-2in1/file_61.png
# https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/dxnproductsimages/dxn-2in1/file_62.png
# https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/dxnproductsimages/dxn-2in1/file_63.jpg
# https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/dxnproductsimages/dxn-2in1/file_64.png
# https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/dxnproductsimages/dxn-2in1/file_65.jpeg
# https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/dxnproductsimages/dxn-2in1/file_66.png
# https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/dxnproductsimages/dxn-2in1/file_67.png
# https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/dxnproductsimages/dxn-2in1/file_68.jpeg
# https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/dxnproductsimages/dxn-2in1/file_69.png
# https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/dxnproductsimages/dxn-2in1/file_7.png
# https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/dxnproductsimages/dxn-2in1/file_70.jpeg
# https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/dxnproductsimages/dxn-2in1/file_71.png
# https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/dxnproductsimages/dxn-2in1/file_72.jpeg
# https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/dxnproductsimages/dxn-2in1/file_73.png
# https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/dxnproductsimages/dxn-2in1/file_74.png
# https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/dxnproductsimages/dxn-2in1/file_75.jpeg
# https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/dxnproductsimages/dxn-2in1/file_76.jpeg
# https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/dxnproductsimages/dxn-2in1/file_77.jpeg
# https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/dxnproductsimages/dxn-2in1/file_78.png
# https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/dxnproductsimages/dxn-2in1/file_79.jpeg
# https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/dxnproductsimages/dxn-2in1/file_8.png
# https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/dxnproductsimages/dxn-2in1/file_80.jpg
# https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/dxnproductsimages/dxn-2in1/file_81.jpeg
# https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/dxnproductsimages/dxn-2in1/file_82.jpeg
# https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/dxnproductsimages/dxn-2in1/file_83.jpeg
# https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/dxnproductsimages/dxn-2in1/file_84.png
# https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/dxnproductsimages/dxn-2in1/file_85.png
# https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/dxnproductsimages/dxn-2in1/file_86.png
# https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/dxnproductsimages/dxn-2in1/file_87.png
# https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/dxnproductsimages/dxn-2in1/file_88.png
# https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/dxnproductsimages/dxn-2in1/file_89.png
# https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/dxnproductsimages/dxn-2in1/file_9.jpeg
# https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/dxnproductsimages/dxn-2in1/file_90.png
# https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/dxnproductsimages/dxn-2in1/file_91.png
# https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/dxnproductsimages/dxn-2in1/file_92.png
# https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/dxnproductsimages/dxn-2in1/file_93.png
# https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/dxnproductsimages/dxn-2in1/file_94.png
# https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/dxnproductsimages/dxn-2in1/file_95.jpeg
# https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/dxnproductsimages/dxn-2in1/file_96.jpeg
# https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/dxnproductsimages/dxn-2in1/file_97.png
# https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/dxnproductsimages/dxn-2in1/file_98.png
# https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/dxnproductsimages/dxn-2in1/file_99.jpeg