class Mystring :
    def __init__(self,stringContent):
        self.stringContent = stringContent
        self.stringLen=len(self.stringContent)
    def __str__(self):
        return f"{self.stringContent}"
    def getlen(self):
        return self.stringLen   
    def deletedigit(self):
        temp=""
        for ch in self.stringContent:
            if not ch.isdigit():
                temp+=ch
        self.stringContent=temp
        self.stringLen=len(self.stringContent)
    def deleteSpaces(self):
        self.stringContent=self.stringContent.replace(" ","")
        self.stringLen=len(self.stringContent)        
    def startend(self,start,end):
        self.stringContent=start+self.stringContent+end
        self.stringLen=len(self.stringContent)       
    def start(self,start):
        self.stringContent=start+self.stringContent
        self.stringLen=len(self.stringContent)       
    def end(self,end):
        self.stringContent=self.stringContent+end
        self.stringLen=len(self.stringContent)       
    def sumdigits(self):
        digit=0
        for ch in self.stringContent:
            if ch.isdigit():
                digit+=int(ch)
        return digit
    def DeleteComaa(self):
        self.stringContent=self.stringContent.replace(',','')
        self.stringLen=len(self.stringContent)