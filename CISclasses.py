import re
        

class CISclasses() :
    def __init__ (self):
        self._quartersDict = {}
        self._classDict = {}
        
        #self._totalClasses = totalClasses
        #self._quarters = quarters
        #self._classNames = classNames  
        
        self._quartersDict["fall"] = set()
        self._quartersDict["winter"] = set()
        self._quartersDict["spring"] = set()
        self._quartersDict["summer"] = set()
        
        DEFAULT_FILE = "cis_classesAnna.txt"
        with open (DEFAULT_FILE) as infile :
            line = infile.readline()
            
            
            while line != "":
                line = line.rstrip()
                # print(line)             
                if (re.search("detailNum=[\w\d-]*</a>\"&gt;</span><span>([\d\w\s\+\+\/#:-]*)<", line)) :
                    m2 = re.search("detailNum=[\w\d-]*</a>\"&gt;</span><span>([\d\w\s\+\+\/#:-]*)<", line).group(1)
                    print(re.search("detailNum=[\w\d-]*</a>\"&gt;</span><span>([\d\w\s\+\+\/#:-]*)<", line).group(1))   
                    
                
                    line = infile.readline()
                    if re.search("(x)", line) :
                
                        self._quartersDict["fall"].add(m2)
                        aList1 = []
                        self._classDict[m2] = aList1
                        self._classDict[m2].append("fall")
                
                    #
                
                    line = infile.readline()
                
                    if re.search("(x)", line) :
                
                        aList2 = []
                
                
                        self._quartersDict["winter"].add(m2)
                
                        self._classDict[m2] = aList2
                        self._classDict[m2].append("winter")
                
                    # 
                    line = infile.readline()
                    if re.search("(x)", line) :
                
                        aList3 = []
                
                
                        self._quartersDict["spring"].add(m2)
                
                        self._classDict[m2] = aList3
                        self._classDict[m2].append("spring")
                        
                    #    
                
                    line = infile.readline()
                    if re.search("(x)", line) :
                
                        aList4 = []
                
                
                        self._quartersDict["summer"].add(m2)
                
                        self._classDict[m2] = aList4
                        self._classDict[m2].append("summer")
                    #
                    
                elif (re.search("catalogID=\d+</a>\"&gt;</span><span>([\w\s\+\+\.\/\d*:#-]*)<", line)) :
                    m = re.search("catalogID=\d+</a>\"&gt;</span><span>([\w\s\+\+\.\/\d*:#-]*)<", line).group(1)
                    print(re.search("catalogID=\d+</a>\"&gt;</span><span>([\w\s\+\+\.\/\d*:#-]*)<", line).group(1))
                    
                    
                    line = infile.readline()
                    if re.search("(x)", line) :
                        
                        self._quartersDict["fall"].add(m)
                        aList1 = []
                        self._classDict[m] = aList1
                        self._classDict[m].append("fall")
                    
                   #
                    
                    line = infile.readline()
                    
                    if re.search("(x)", line) :
                        
                        aList2 = []
                    
                        
                        self._quartersDict["winter"].add(m)
                        
                        self._classDict[m] = aList2
                        self._classDict[m].append("winter")
                    
                   # 
                    line = infile.readline()
                    if re.search("(x)", line) :
                                         
                        aList3 = []
                    
                        
                        self._quartersDict["spring"].add(m)
                        
                        self._classDict[m] = aList3
                        self._classDict[m].append("spring")
                    
                    #    
                   
                    line = infile.readline()
                    if re.search("(x)", line) :
                   
                        aList4 = []
                    

                        self._quartersDict["summer"].add(m)
                        
                        self._classDict[m] = aList4
                        self._classDict[m].append("summer")
                    #
                    
                line = infile.readline()
                
                

    def getCount(self, totalClasses):
        pass
    
    def getQuarters(self, name):
        #if name in self._classDict:
            #print("True")
        classList = []
        for key in self._classDict:
            if name in key :
                classList.append(key)
        for j in classList :
            print(j)
        inName = input("\nEnter a class name: ")
        #print(self._classDict[inName])
        
        for e in self._classDict:
            print(self._classDict[inName])
        
    def getClasses(self, quarters):
        for i in self._quartersDict[quarters] :
            print(i)
       
        
        