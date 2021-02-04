# 
# Example file for parsing and processing HTML
#
from html.parser import HTMLParser

import
  
def main():
  # instantiate the parser and feed it some HTML
  parser = MyHTMLParser()
  f = open("samplehtml.html")
  if f.mode =='r':
    contents = f.read()
    parser.feed(contents)
  print("Meta tags found: " + str(metacount))

if __name__ == "__main__":
  main();
  
