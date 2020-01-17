# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 10:51:15 2020

@author: Lalitha
@Desc: Data Layer
"""

from bs4 import BeautifulSoup as bs
import os
import json
import urllib.request
import urllib.parse
import urllib.error
from urllib.request import urlretrieve

class ScrapperImage:
    
   ## Create  Image URl
   def createImageUrl(searchterm):
       searchterm = searchterm.split()
       searchterm = "+".join(searchterm)
       web_url = "https://www.google.co.in/search?q=" + searchterm + "&source=lnms&tbm=isch"
       
       return web_url
   
   def delete_downloaded_images(self,list_of_images):
       for self.image in list_of_images:
           try:
               os.remove("./static/"+self.image)
           except Exception as e:
               print('error in deleting:  ',e)
               
       return 0
   
    # get Raw HTML
   def scrap_html_data(url,header):
        request = urllib.request.Request(url,headers=header)
        response = urllib.request.urlopen(request)
        responseData = response.read()
        html = bs(responseData, 'html.parser')
        
        return html
    
    # contains the link for Large original images, type of  image
   def getimageUrlList(rawHtml):
        imageUrlList = []
        # from UI debugger tool -> inspect html code 
        # rg_meta - contains data in the form of json
        for a in rawHtml.find_all("div", {"class": "rg_meta"}):
            # ou contains the link / url 
            # ity contains image extension 
            link, imageExtension = json.loads(a.text)["ou"], json.loads(a.text)["ity"]
            imageUrlList.append((link, imageExtension))
            
            print("there are total", len(imageUrlList), "images")
        return imageUrlList
    
    
    # Downloads images from imageUrlList array
   def downloadImagesFromURL(imageUrlList,image_name, header):
        masterListOfImages = []
        count=0
        ###print images
        imageFiles = []
        imageTypes = []
        image_counter=0
        
        for i, (img, Type) in enumerate(imageUrlList):
            try:
                if (count > 5):
                    break
                else:
                    count = count + 1
                    
                req = urllib.request.Request(img, headers=header) # it returns request
                try:
                    # It downloads images inside static folder
                    urllib.request.urlretrieve(img,"./static/"+image_name+str(image_counter)+".jpg")
                    image_counter = image_counter+1
                    print("Image write Success:",e)
                    
                except Exception as e:
                    # If any problem while retrieving images comes into this block
                    print("Image write failed:  ",e)
                    image_counter = image_counter + 1
                    
                # reading request and gets response data 
                respData = urllib.request.urlopen(req)
                
                # reads the response data, which means image
                raw_img = respData.read()
                
                imageFiles.append(raw_img)
                imageTypes.append(Type)
                
            except Exception as e:
                print("could not load : " + img)
                print(e)
                count = count + 1
        
        # Final images list      
        masterListOfImages.append(imageFiles)
        masterListOfImages.append(imageTypes)
        
        return masterListOfImages
                
      
           
    
   
    
    
    
     