from tkinter import *
from matrix import *

#GUI class
class MatrixGUI():
  def __init__(self):
    self.__count=0
    self.__model=Matrix()
    self.__mainWindow=Tk()
    self.__entry=[]
    self.__entryOne=[]

    self.__titleFrame=Frame(self.__mainWindow)
    self.__titleLabel=Label(self.__mainWindow,\
                            text="Welcome",\
                            font=("gotham", 32)).grid(row=0)

    self.drawMatrix()
    self.__firstMatrixLabel=Label(self.__mainWindow, text='Enter a matrix:', font=('gotham', 18)).grid(row=2,column=0)
    #self.__separationLabel=Label(self.__mainWindow, text='second matrix').grid(row=2,column=4)
    self.__en.bind('<Return>', self.enFilled)
    self.__matrixRowReduction=Button(self.__mainWindow,\
                                     text='Reduced Row Reduction',state='normal',
                                     \
                                     command=self.rowReduced).grid(row=5, column=0)
    self.__newMatrixLable=Label(self.__mainWindow,text='Reduced matrix:', font=('gotham', 18)).grid(row=6)
    self.__matrixVar=StringVar()
    self.__matrixVarOne=StringVar()
    self.__matrixVarTwo=StringVar()
    
    
    self.__matrixVar.set('?')
    self.__matrixVarOne.set('?')
    self.__matrixVarTwo.set('?')
    self.__matrixVarLabel=Label(self.__mainWindow,textvariable=self.__matrixVar)\
                           .grid(row=6, column=1)
    self.__matrixVarLabelOne=Label(self.__mainWindow,textvariable=self.__matrixVarOne)\
                           .grid(row=7, column=1)
    self.__matrixVarLabelTwo=Label(self.__mainWindow,textvariable=self.__matrixVarTwo)\
                           .grid(row=8, column=1)
    



    mainloop()

##Event Handler-----------
  def drawMatrix(self):
    columns=0
    #entry=[]
    for rows in range(1,self.__model.getRows()+1):
      for columns in range(self.__model.getColumns()):
        

        self.__en=Entry(self.__mainWindow,width=5)
        #print (columns)
        self.__en.grid(row=rows+1, column=columns+1)
        self.__en.bind('<Return>', self.enFilled)
        self.__entry.append(self.__en)

##    for rows in range(1,self.__model.getRows()+1):
##      for columns in range(self.__model.getColumns()):
##        self.__enOne=Entry(self.__mainWindow,width=5).grid(row=rows+1, column=columns+5)
##        self.__entryOne.append(self.__enOne)
                                                           
        
        
  def enFilled(self,event):
    #outerlist = []
    #self.__model.clearList(self.__outerList)
    newlist=[]
    #print (self.__entry)
    for entry in self.__entry:
      if self.isDigit(entry.get()):
      #print (entry.get())
        newlist.append(int(entry.get()))
      #print (newlist)
      else:
        self.__count+=1
    if self.__count==0:
      
      self.__model.rowZero.extend(newlist[:3])
      self.__model.rowOne.extend(newlist[3:6])
      self.__model.rowTwo.extend(newlist[6:9])
      print(self.__model.rowZero)
      self.__model.setOuterList()
      self.__model.getMatrix()
    else:
      messagebox.showwarning('Input Error', 'There are {}'.format(self.__count)
                               +' invalid inputs \n Please input integers only')
      #del self.__outerList[:]
      self.__count=0


    
    print(self.__model.getMatrix())
    #print (self.__en)
    #print(self.__entry)
    #print(self.__en.get())
    #self.__en.config(state='disable')
      #self.__matrixRowReduction.configure(state='normal')
      
  def rowReduced(self):
    self.__model.orderFirstColumn()
    print(self.__model.getMatrix())
    self.__model.reduceFirstColumn()
    print(self.__model.getMatrix())
    self.__model.reduceSecondColumn()
    print(self.__model.getMatrix())
    self.__model.reduceThirdColumn()
    self.__matrixVar.set(self.__model.getRow(0))
    self.__matrixVarOne.set(self.__model.getRow(1))
    self.__matrixVarTwo.set(self.__model.getRow(2))
    #if self.__count=0
    #self.__matrixRowReduction.config(state='normal')

    


#help methods-------
  def isDigit(self,value):
    return value.isdigit()
      


    
        
        









MatrixGUI()
