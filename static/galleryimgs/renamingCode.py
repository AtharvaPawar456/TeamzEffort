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
    # "DirectSellingConferance_15_5_2025",
    # "BusinessOpportunityMeeting_Kandivali_2023",
    # "BusinessOpportunityMeeting_Dadar_2023",
    # "DXN_New_Product_Launching_2_7_2025",
    # "DXN_New_Product_Launching_17_08_2025",
    # "DXN_NDTatDadarOffice_19_7_2025",
    # "DXN_Shradhanjali_6_6_2025",
    # "DXN_CouncellingDMI_Dadar_25_5_2025",
    # "DXN_ShilajitOpening_14_Feb_2026",
    "DXN_Vasai_WomensDayCelebrationMarch2026",
    
    
]
# for folder in folderList:
#     renameAllFiles(folder)





# files = os.listdir("DXN_AchiverTraining9Jan2026")
# files = os.listdir("DXNAnnualRecognitionNite8Jan2026/v2")
# files = os.listdir("DXN_Palghar_Chinchghar_28_6_2024")
# files = os.listdir("DXN_CouncellingDMI_Dadar_25_5_2025")
files = os.listdir("DXN_Vasai_WomensDayCelebrationMarch2026")
# # # tempPath = "https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/galleryimgs/NewYearCelebration_Jan_2026/"
# # # tempPath = "https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/galleryimgs/DXNAnnualRecognitionNite8Jan2026/"
# tempPath = "https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/galleryimgs/DXNAnnualRecognitionNite8Jan2026/v2/"
# tempPath = "https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/galleryimgs/DXN_CouncellingDMI_Dadar_25_5_2025/"
tempPath = "https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/galleryimgs/DXN_ShilajitOpening_14_Feb_2026/"
tempPath = "https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/galleryimgs/DXN_Vasai_WomensDayCelebrationMarch2026/file_3.jpeg"



for fileName in files:
    print(f"{tempPath}{fileName};")





"""






"""