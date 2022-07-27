data =[
    "https://s3.ap-south-1.amazonaws.com/byjus-media-delivery/videos/mpkgr-production-d64dd5e1/rar60s/Search_QnA/220420/Batch_4/Portrait/Set1/21QNAEXEMP06BIO05P01_The_Living_Organisms_and_their_Surroundings/Batch_2/21QNAEXEMP06BIO05Q21_2/thumbs/c33c7ad0/360x480.jpg",
    "https://s3.ap-south-1.amazonaws.com/byjus-media-delivery/videos/mpkgr-production-f5b49ffb/rar60r/Search_QnA/220420/Batch_4/Portrait/Set1/21QNAEXEMP06BIO05P01_The_Living_Organisms_and_their_Surroundings/Batch_2/21QNAEXEMP06BIO05Q21_1/thumbs/9e0417e2/360x480.jpg",
    "https://qnavideos.byjusweb.com/thumbnails/byjus-media-delivery/videos/25022022/21QNAEXEMP06BIO05P01 The Living Organisms and their Surroundings/21QNAEXEMP06BIO05Q21_1/thumbs/480x360.jpg",
    "https://qnavideos.byjusweb.com/thumbnails/byjus-media-delivery/videos/25022022/21QNAEXEMP06BIO05P01 The Living Organisms and their Surroundings/21QNAEXEMP06BIO05Q21_2/thumbs/480x360.jpg"
] 

# +
from PIL import Image
import requests

for i in data:
    im = Image.open(requests.get(i, stream=True).raw)
    print(im.size)
    display(im)
    
# -




