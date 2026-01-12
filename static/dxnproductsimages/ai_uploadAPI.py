import requests


def uploadPromoImgData(piProdId, piHighlightTitle="*", piMainImgBaseTxt="*"):
    """
    Upload promo image data to remote API.
    Input: product ID, highlight title, base image text
    Working: Sends POST request with JSON payload
    Output: API response JSON or error details
    """

    apiUrl = "https://digitalassets.pythonanywhere.com/api/promoimg/upload/"

    payload = {
        "pi_prodid": piProdId,
        "pi_highlighttitle": piHighlightTitle,
        "pi_mainimgbasetxt": piMainImgBaseTxt
    }

    headers = {
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(
            apiUrl,
            json=payload,
            headers=headers,
            timeout=30
        )

        response.raise_for_status()

        return {
            "status": True,
            "response": response.json()
        }

    except requests.exceptions.Timeout:
        return {
            "status": False,
            "error": "Request timeout"
        }

    except requests.exceptions.ConnectionError:
        return {
            "status": False,
            "error": "Connection failed"
        }

    except requests.exceptions.HTTPError as error:
        return {
            "status": False,
            "error": f"HTTP error: {error}",
            "response": response.text
        }

    except Exception as error:
        return {
            "status": False,
            "error": str(error)
        }









imageUrls = [

    "https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/dxnproductsimages/dxn-kombucha/file_199.mp4"

    
    https://raw.githubusercontent.com/AtharvaPawar456/TeamzEffort/refs/heads/main/static/dxnproductsimages/dxn-kombucha/file_199.mp4
    
    
    
    
    
    
    
    
    
]



# result = uploadPromoImgData(piProdId=4,piHighlightTitle="*",piMainImgBaseTxt=imgpath)
# result = uploadPromoImgData(piProdId=7,piHighlightTitle="*",piMainImgBaseTxt=imgpath)

# imageUrlsLen = len(imageUrls)
# for index, imgpath in enumerate(imageUrls):
#     result = uploadPromoImgData(piProdId=4 ,piHighlightTitle="*",piMainImgBaseTxt=imgpath)
#     print(f"{index}/{imageUrlsLen} : {result}")





# result = uploadPromoImgData(piProdId=6,piHighlightTitle="*",piMainImgBaseTxt="...")
# print(result)
