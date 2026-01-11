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
    # "dxn-2in1-v2",
    # "img",
    
    # "dxn-ashwagandha",
    # "dxn-gano-oil",
    # "dxn-gano-tea",
    # "dxn-gokshura",
    # "dxn-kombucha",
    # "dxn-neeli-oil",
    # "dxn-super-green",
    # "dxn-tea-tree-cream",
    
    # "dxn",
    
]

# for folder in folderList:
#     renameAllFiles(folder)


# files = os.listdir("dxn-2in1")
# files = os.listdir("dxn-cocozhi")
# files = os.listdir("dxn-tooth-paste")
# files = os.listdir("dxn-2in1-v2")
# tempPath = "https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/dxnproductsimages/Dxn%20Spirulina.png"
# tempPath = "https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/dxnproductsimages/dxn-2in1/"
# tempPath = "https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/dxnproductsimages/dxn-cocozhi/"
# tempPath = "https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/dxnproductsimages/dxn-tooth-paste/"
# tempPath = "https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/dxnproductsimages/dxn-2in1/"


# files = os.listdir("dxn-ashwagandha")
# tempPath = "https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/dxnproductsimages/dxn-ashwagandha/"
# files = os.listdir("dxn-gano-oil")
# tempPath = "https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/dxnproductsimages/dxn-gano-oil/"
# files = os.listdir("dxn-gano-tea")
# tempPath = "https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/dxnproductsimages/dxn-gano-tea/"
# files = os.listdir("dxn-gokshura")
# tempPath = "https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/dxnproductsimages/dxn-gokshura/"
# files = os.listdir("dxn-neeli-oil")
# tempPath = "https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/dxnproductsimages/dxn-neeli-oil/"
# files = os.listdir("dxn-tea-tree-cream")
# tempPath = "https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/dxnproductsimages/dxn-tea-tree-cream/"
# files = os.listdir("dxn-super-green")
# tempPath = "https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/dxnproductsimages/dxn-super-green/"
# files = os.listdir("dxn-kombucha")
# tempPath = "https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/dxnproductsimages/dxn-kombucha/"
files = os.listdir("dxn-soap")
tempPath = "https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/dxnproductsimages/dxn-soap/"
files = os.listdir("dxn-soap/banners")
tempPath = "https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/dxnproductsimages/dxn-soap/banners/"
files = os.listdir("dxn-soap/shorts")
tempPath = "https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/dxnproductsimages/dxn-soap/shorts/"



for fileName in files:
    print(f"'{tempPath}{fileName}',")


# https://github.com/AtharvaPawar456/TeamzEffort/blob/main/static/dxnproductsimages/dxn-tooth-paste/file_63.mp4
# https://github.com/AtharvaPawar456/TeamzEffort/blob/main/static/dxnproductsimages/dxn-tooth-paste/file_64.mp4


# https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/dxnproductsimages/dxn-tooth-paste/file_63.mp4
# https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/dxnproductsimages/dxn-tooth-paste/file_64.mp4





"""
New images:

dxn-ashwagandha
dxn-gano-oil
dxn-gano-tea
dxn-gokshura
dxn-kombucha
dxn-neeli-oil
dxn-super-green
dxn-tea-tree-cream






Old imgs:









get details for this product in below format


productname : 
highlighttitle : (10 words )
info : (200 words )
product detailed content  : (350 words, in plain html format )
product images  : (get 5 to 6 product images)
benefits : (give me 5 points in plain html format )
usage : (give me 5 points in plain html format )
Tags: (eg: personalcare, organic, oralcare, skin care, haircare, beverages, organic)



# context:
'''

DXN Tea Tree Cream



Indulge in the soothing and healing properties of DXN Tea Tree Cream, a versatile skincare solution. Enriched with the natural goodness of tea tree oil, this cream helps alleviate skin irritations, blemishes, and discomfort. Its gentle formulation nourishes and moisturizes the skin, promoting a healthier and clearer complexion. DXN Tea Tree Cream is your go-to remedy for addressing various skin concerns and maintaining a radiant, blemish-free appearance.


DXN Tea Tree Cream is a soothing and refreshing herbal cream that contains pure Tea Tree Oil. Known for its natural antibacterial and antifungal properties, it helps in promoting healthy skin by protecting it from infections and irritation. Suitable for all skin types, this cream is ideal for skin conditions like acne, rashes, and insect bites.

Key Features
Enriched with pure Tea Tree Oil.
Antibacterial and antifungal properties.
Soothes irritated and inflamed skin.
Helps in treating acne, rashes, and insect bites.
Non-greasy, easily absorbed formula.
Suitable for all skin types.
Key Ingredients
Tea Tree Oil
Aloe Vera Extract
Vitamin E
Shea Butter
Glycerin
How to Use
Apply a small amount of DXN Tea Tree Cream to the affected area. Gently massage into the skin until fully absorbed. Use 2-3 times daily for best results.

Net Qty : 30gram


'''




"""