# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 15:24:49 2020

@author: krish.naik
"""

from scrapperImage.ScrapperImage import ScrapperImage

class BusinessLayer:
    
    keyword=""
    fileLoc=""
    image_name=""
    header=""
    
    
    def downloadImages( keyWord, header):
        imgScrapper = ScrapperImage
        url = imgScrapper.createImageUrl(keyWord)
        rawHtml = imgScrapper.scrap_html_data(url, header) # rawHtml holds all images
        imageURLList = imgScrapper.getimageUrlList(rawHtml) # it extracts images from raw html
        masterListOfImages = imgScrapper.downloadImagesFromURL(imageURLList,keyWord, header) # it download the images(imageURLList)
        
        return masterListOfImages
    
    
    
    