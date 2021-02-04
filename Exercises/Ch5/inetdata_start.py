# 
# Example file for retrieving data from the internet
#
import urllib.request

def main():
  webUrl=urllib.request.urlopen("http://www.google.com")
  print("result code:" +str(webUrl.getcode()))
  #read some data and print it out
  data=webUrl.read()#reading the entier of this url into a variable named data
  print(data)
  
if __name__ == "__main__":
  main()
