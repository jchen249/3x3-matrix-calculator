class Matrix:
  #class variables
  NUM_ROW=3
  NUM_COLUMN=3



  #constructors
  def __init__(self):
    self.__outerList=[]
    #self.__holderList=[]
    self.rowZero=[]
    self.rowOne=[]
    self.rowTwo=[]
##    self.__length=0
    self.__matrixRow=self.NUM_ROW
    self.__matrixColumn=self.NUM_COLUMN


  #accessor
  def getLength(self):
    return len(self.__outerList)
  def getMatrix(self):
    return self.__outerList
  def getRows(self):
    return self.__matrixRow
  def getColumns(self):
    return self.__matrixColumn
##
##  def setLength(self):
##    self.__length = self.getLength()
  def setRowZero(self, row):
    self.__rowZero = row

  def clearList(self, aList):
    aList[:]

  def setRowOne(self, row):
    self.__rowOne = row

  def setRowTwo(self, row):
    self.__rowTwo = row

  def setOuterList(self):
    self.__outerList.append(self.rowZero)
    self.__outerList.append(self.rowOne)
    self.__outerList.append(self.rowTwo)

  def getRow(self, positionOfRow):
    return self.__outerList[positionOfRow]

  #  simplifies row
  #  scalar is what gets entry to 1
  #  position is row number(row 1 is 0)
  def scaleRow(self, scalar, positionOfRow):
    row = self.getRow(positionOfRow)
    newRow = []
    for num in row:
      newRow.append(num * scalar)
    self.__outerList.pop(positionOfRow)
    self.__outerList.insert(positionOfRow, newRow)


  #  pos here is the row we want to change(row 1 is 0)
  def scaleTempRow(self, scalar, positionOfRow):
    row = self.getRow(positionOfRow)
    tempRow = []
    for num in row:
      tempRow.append(num * scalar)
    return tempRow

  #  tempRow is what we use to change the other
  #  positionOfRow is the row we want to change
  #  if thats the first row, position is 0
  def changeRowWithOther(self, tempRow, positionOfRow):
    idx = -1
    newSecondRow = []
    secondRow = self.getRow(positionOfRow)
    for number in secondRow:
      idx += 1
      number -= tempRow[idx]
      newSecondRow.append(number)
    self.__outerList.pop(positionOfRow)
    self.__outerList.insert(positionOfRow, newSecondRow)


  def getEntry(self, positionOfRow, columnNum):
    row = self.getRow(positionOfRow)
    for num in row:
      if row.index(num) == (columnNum - 1):
        return num


  #  puts desired row (given by its index in matrix) to bottom
  #  mutator
  def putRowtoBottom(self, positionOfRow):
    length = self.getLength()
    row = self.__outerList[positionOfRow]
    self.__outerList.pop(positionOfRow)
    self.__outerList.insert(length, row)

  #  returns True if row 0 first entry is zero
  def firstEntryIsZero(self, row):
    firstNum = row[0]
    return firstNum == 0

  def entryIsOne(self, num):
    return num == 1

  def checkRowIsZeros(self, row):
    count = 0
    for num in row:
      if num == 0:
        count += 1
    return count == len(row)

  def checkFirstColumnAllZero(self, columnNum):
    aMatrix = self.__outerList[:]
    entryHolderList = []
    zeroCount = 0
    x = -1
    for i in range(3):
      x += 1
      xRowFirstEntry = self.getEntry(x, columnNum)
      entryHolderList.append(xRowFirstEntry)
    for each in entryHolderList:
      if each == 0:
        zeroCount += 1
    return zeroCount == len(entryHolderList)

  def checkFirstColumnFirstEntryIsOnlyNonZero(self, columnNum):
    aMatrix = self.__outerList[:]
    entryHolderList = []
    check = [0, 0]
    x = -1
    idx = 0
    for i in range(3):
      x += 1
      xRowEntry = self.getEntry(x, columnNum)
      entryHolderList.append(xRowEntry)
    return check == entryHolderList[1:]

  def orderFirstColumn(self):
    length = self.getLength()
    holderList = []
    for line in self.__outerList:
      position = self.__outerList.index(line)
      if self.firstEntryIsZero(line) and position != (length - 1):
        holderList.append(position)
  #  print(holderList)
    for each in holderList:
      self.putRowtoBottom(each)
      if len(holderList) > 1:
        self.__outerList.reverse()
    for line in self.__outerList:
      idx = self.__outerList.index(line)
      if self.checkRowIsZeros(line):
        self.__outerList.pop(idx)
        self.__outerList.insert(length - 1, line)


  #  if all zeros in first column, skip step
  #  if all zeros but first one (we will know its the first \
  #  since we put all zero rows below non-zero, we just simplify
  #  the first row to get its first entry 1, our leading entry
  #  if all nonzero, reduce row 1 to get first entry to 1 and
  #  scale a temp row 1 to get its first entry be a negation of
  #  the second row's first entry. Then subtract row 2 by row,
  #  entry position by entry position. Pop the old row 2 out and
  #  insert the new one in. Row 1 doesnt change
  def reduceFirstColumn(self):
    if self.checkFirstColumnAllZero(1):
      pass
    elif self.checkFirstColumnFirstEntryIsOnlyNonZero(1):
      firstRowFirstEntry = self.getEntry(0, 1)
      if self.entryIsOne(firstRowFirstEntry):
        pass
      else:
        self.scaleRow(1 / firstRowFirstEntry, 0)
    else:
      firstRowFirstEntry = self.getEntry(0, 1)
      self.scaleRow(1 / firstRowFirstEntry, 0)
  #    print(sampleMatrix)
      secondRowFirstEntry = self.getEntry(1, 1)
      tempRowOne = self.scaleTempRow(secondRowFirstEntry, 0)
  #    print(tempRowOne)
      self.changeRowWithOther(tempRowOne, 1)
      thirdRowFirstEntry = self.getEntry(2, 1)
  #    print(thirdRowFirstEntry)
      tempRowTwo = self.scaleTempRow(thirdRowFirstEntry, 0)
      self.changeRowWithOther(tempRowTwo, 2)

  def reduceSecondColumn(self):
    firstRowSecondEntry = self.getEntry(0, 2)
    secondRowSecondEntry = self.getEntry(1, 2)
    thirdRowSecondEntry = self.getEntry(2, 2)


    if secondRowSecondEntry != None:
      self.scaleRow(1 / secondRowSecondEntry, 1)
      if thirdRowSecondEntry == None:
        if firstRowSecondEntry == None:
          pass
        else:
          tempSecondRow = self.scaleTempRow(firstRowSecondEntry, 1)
          self.changeRowWithOther(tempSecondRow, 0)
      else:
        tempSecondRow = self.scaleTempRow(thirdRowSecondEntry, 1)
        self.changeRowWithOther(tempSecondRow, 2)
        if firstRowSecondEntry == None:
          pass
        else:
          tempSecondRowTwo = self.scaleTempRow(firstRowSecondEntry, 1)
          self.changeRowWithOther(tempSecondRowTwo, 0)
    else:
      if thirdRowSecondEntry == None:
        if firstRowSecondEntry == None:
          pass
        else:
          tempSecondRow = self.scaleTempRow(firstRowSecondEntry, 1)
          self.changeRowWithOther(tempSecondRow, 0)
      else:
        self.scaleRow(1 / thirdRowSecondEntry, 2)
        if firstRowSecondEntry == None:
          self.putRowtoBottom(1)
        else:
          tempThirdRow = self.scaleTempRow(firstRowSecondEntry, 2)
          self.changeRowWithOther(tempThirdRow, 0)
          self.putRowtoBottom(1)

  def reduceThirdColumn(self):
    thirdRowThirdEntry = self.getEntry(2, 3)
    if thirdRowThirdEntry != None:
      for line in self.__outerList:
        if self.__outerList.index(line) != 2:
          line[-1] = 0.0
        else:
          line[-1] = 1.0
    else:
      pass

    for each in self.__outerList:
      for num in each:
        if num == -0.0:
          idx = each.index(num)
          each.pop(idx)
          each.insert(idx, 0.0)
    for line in self.__outerList:
      print(line)


