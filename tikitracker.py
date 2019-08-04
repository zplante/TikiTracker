import urllib.request
import re



temp = open("ids.txt","r")
curids = temp.read().split('\n')
fp = urllib.request.urlopen("http://www.geekitikis.com/products")
mybytes = fp.read()

mystr = mybytes.decode("utf8")
fp.close()
result = re.findall(r'<li ([\s\S]*?)<\/li>', mystr)
file = open("ids.txt","w")
for element in result:
  dataid = re.findall(r'data-id="([^"]*)"',element)
  id = dataid[0]
  file.write("\n")
  imageurl= re.findall(r'<img src="([\s\S^"]*?)">',element)
  img = imageurl[0].split(".jpg", 1)[0]+".jpg"
  if id not in curids:
    print("new shit at geekitiki")
    f = open('newtiki.jpg','wb')
    f.write(urllib.request.urlopen(img).read())
    f.close()
  file.write(id)


