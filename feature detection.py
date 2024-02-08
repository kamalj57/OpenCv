#                      Feature dection and matching
'''
-> is the process of checking the important feature of the images such as edges,corners,ridges and blobs in the imgs
-> ORB(Oriented FASRT and Rotated Brief)
     * very effective of detecting the feature of the img
     * it is programmed to find fewer features of the img
-> Brute Force
      * Brute_force.match()
'''
import cv2 as cv
def detector(img1,img2):
    detect=cv.ORB_create()
    key1,des1=detect.detectAndCompute(img1,None)
    key2,des2=detect.detectAndCompute(img2,None)
    return (key1,des1,key2,des2)
def BF_FeatureMatcher(des1,des2):
    brute=cv.BFMatcher(cv.NORM_HAMMING,crossCheck=True)
    noofmatches=brute.match(des1,des2)
    noofmatches=sorted(noofmatches,key=lambda x:x.distance)
    return noofmatches
def output(pic1,kpt1,pic2,kpt2,best_match):
    oimg=cv.drawMatches(pic1,kpt1,pic2,kpt2,best_match[:55],None,flags=2)
    cv.imshow('output',oimg)
if __name__=='__main__':
    img1='goku.jpg'
    img2='goku.jpg'
    gray1=cv.imread(img1,0)
    gray2=cv.imread(img2,0)
    key1,des1,key2,des2=detector(gray1,gray2)
    noofmatch=BF_FeatureMatcher(des1,des2)
    total=len(noofmatch)
    print('no f features found',total)
    output(gray1,key1,gray2,key2,noofmatch)
 
'''----------------------------------------------------------------------------
Application of image registration:
* Stitching various scenes together to form a continuous  panaroma shots
* Algorithm camera imgs of documents to a standard alignment to create realistic scnned documents
*'''
