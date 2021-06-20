import GetTense
import FindWord
import readBook

def GetLsisLevel(list) :

   l = []
   finalList0 = []
   finalList=[]
   for i in list:
      if i == '':
         list.remove(i)
   for i in list:
      a = FindWord.findWord(i)
      l.append(a)
   for i in l:
         if i != 'null':
            finalList0.append(i)

   x = GetTense.get(list)
   finalList0 += x
   A=finalList0.count('A1')
   B=finalList0.count('A2')
   C=finalList0.count('B1')
   D=finalList0.count('B2')
   E=finalList0.count('C')
   L= [A,B,C,D,E]
   finalList.append(finalList0)
   finalList.append(L)
   return finalList


'''
if __name__ == "__main__":
   y = readBook.readBookFile(readBook.convertBook('2.PNG'))
   print (y)
   a=GetLsisLevel(y)
   print(a)
   #print(listToGraph(GetLsisLevel(['A1','A2','B1','A1'])))
'''