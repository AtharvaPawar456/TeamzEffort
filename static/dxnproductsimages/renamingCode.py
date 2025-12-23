import os


def renameMediaFiles(folderPath):
    """
    Renames image (.png, .jpg, .jpeg) files to img_<number>.<ext>
    and video (.mp4) files to vid_<number>.mp4 inside the given folder.

    Input:
        folderPath (str): Path to the target folder

    Working:
        - Iterates through all files
        - Renames images and videos with separate counters
        - Skips unsupported files
    """
    try:
        if not os.path.isdir(folderPath):
            raise FileNotFoundError("Provided path is not a valid directory")

        files = sorted(os.listdir(folderPath))
        imgCounter = 1
        vidCounter = 1

        for fileName in files:
            oldPath = os.path.join(folderPath, fileName)

            if not os.path.isfile(oldPath):
                continue

            name, extension = os.path.splitext(fileName)
            extension = extension.lower()

            if extension in [".png", ".jpg", ".jpeg"]:
                newFileName = f"img_{imgCounter}{extension}"
                imgCounter += 1

            elif extension == ".mp4":
                newFileName = f"vid_{vidCounter}.mp4"
                vidCounter += 1

            else:
                continue

            newPath = os.path.join(folderPath, newFileName)

            if os.path.exists(newPath):
                raise FileExistsError(f"File already exists: {newFileName}")

            os.rename(oldPath, newPath)

        print("Files renamed successfully.")

    except Exception as error:
        print(f"Error: {error}")


# Example usage
renameMediaFiles("your_folder_path_here")



folderList = [
    "dxn-2in1",
    "dxn-butterfly-pea",
    "dxn-cocozhi",
    "dxn-cordi-coffee",
    "DXN-Cow-Ghee",
    "dxn-jaggery",
    "dxn-kiwi-drink-bottle",
    "dxn-lemonzhi",
    "dxn-massage-oil",
    "DXN-Material",
    "dxn-shampo",
    "dxn-soap",
    "dxn-spirulina",
    "dxn-spirulina-cereal",
    "dxn-tailam",
    "dxn-tooth-paste",
    "dxn-virgin-oil"
]

# for folder in folderList:
#     renameMediaFiles(folder)