class Tag(object):
    
    def __init__(sself, name, contents):
        self.start_tag = '<{}>'.format(name)
        self.end_tag='</{}>'.format(name)
        self.contents== contents
        
    def __str__(self):
        return"{0.start_tag}{0.contents}{0.end_tag}".format(self)
    
    def display(self):  
        print(self)
        
class DocType(Tag):
    
    def __init__(self):
        super.__init__('') #add link 
        self.end_tag= '' #doctype doesnt have an end tag 
        
class head(Tag):
    def __init__(self):
        super().__init__('head','')
        
class body(Tag):
    
    def __init__(self):
        super().__init__('body','')
        self._body_contents=[]
        
    def add_tag(self, name ,contents):
        mew_tag=Tag(name,contents)
        self._body_contents.append(new_tag)
        
    def display(self): #ovwerides the method from supper class
        for tag in self._body_contents:
            self.contents += str(tag)
            
            super().display()
            
class HtmlDoc(object):
    
    def __init__(self):
        self._doc_type=Doctype()
        self.__head = Head()
        self._body = Body()
        
    def add_tag(self, name, contents):
        self._body.add_tag(name,contents)
        
        
        