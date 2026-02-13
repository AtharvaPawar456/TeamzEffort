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
            # newFileName = f"temp_{fileCounter}{extension}"
            newPath = os.path.join(folderPath, newFileName)

            os.rename(oldPath, newPath)
            fileCounter += 1

        print(f"Renamed {fileCounter - 1} files in '{folderPath}' successfully.")

    except Exception as error:
        print(f"Error: {error}")


folderList = [

    # "NewYearCelebration_Jan_2026",
    # "DXNAnnualRecognitionNite8Jan2026/v2",
    # "DXN_AchiverTraining9Jan2026",
    # "Diwali_Celebration_2025",
    # "DXN_PalgharDivesh_2025",
    # "DXN_StarAgentEvent_2025",
    # "DXN_GetTogether_2025",
    # "DXN_WomenWellness_Palghar_Divesh_2025",
    # "Payment_Proof",
    # "DXN_Palghar_Chinchghar_28_6_2024",
    # "DXN_Salwad_Boisar_30_7_2024",
    
    
]
# for folder in folderList:
#     renameAllFiles(folder)


# files = os.listdir("DXN_AchiverTraining9Jan2026")
# files = os.listdir("DXNAnnualRecognitionNite8Jan2026/v2")
files = os.listdir("DXN_Palghar_Chinchghar_28_6_2024")
# files = os.listdir("DXN_Salwad_Boisar_30_7_2024")
# # # tempPath = "https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/galleryimgs/NewYearCelebration_Jan_2026/"
# # # tempPath = "https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/galleryimgs/DXNAnnualRecognitionNite8Jan2026/"
# tempPath = "https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/galleryimgs/DXNAnnualRecognitionNite8Jan2026/v2/"
tempPath = "https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/galleryimgs/Payment_Proof/"



for fileName in files:
    print(f"{tempPath}{fileName};")





"""






"""