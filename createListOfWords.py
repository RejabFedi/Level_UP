import PyPDF2

class PdfWord :

    def extractAndSortFileToText(FileName):
         listOfWords=[]

         filename: str = FileName
         FILE_PATH = filename

         with open(FILE_PATH, mode='rb') as file:
              reader = PyPDF2.PdfFileReader(file)
              for pageNum in range(reader.getNumPages()) :
                  page = reader.getPage(pageNum)


                  textList = page.extractText().replace('\n',' ').replace('. ','\n').replace('© Oxford University Press','\n').replace(' ˜e Oxford 3000Ž by CEFR level','').replace('A1','').replace('n.','n.\n').replace('v.','n.\n').replace(' The Oxford 3000 is the list of the 3000 most important words to learn in English , from  to B2 level','').replace('article about','article \nabout').replace('prep\n, adv','prep,adv.').replace('det\n, pron','det,pron.').replace('n.\n, auxiliary v','n,auxiliary v.').replace('adv\n, prep','adv,prep.').replace('adj\n, n','adj,n.').replace('n.\n, n.','n,v.').replace('n.\n, adj','n,adj.').replace('adj\n, adv','adj,adv.').replace('pron.\n, adv','pron,adv.').replace('n.\n, adv','n,adv.').replace('n,adj.\n, adv','n,adj,adv.').replace('det./adj\n, pron','det,adj,pron.').replace(' ˛','\n˛').replace('n.\n, det./pron','n,det,pron.').replace('pron\n, det','pron,det.').replace('adj\n, det./pron','adj,det,pron.').replace('adj,adv.\n, n.','adj,adv,n.').replace('pron,det.\n, adv','pron,det,adv.').replace('det./pron\n, adv','det,pron,adv.').replace('prep\n, adj,adv.','prep,adj,adv.').replace('exclam\n, det','exclam,det.').replace('exclam\n, adj./adv','exclam,adj,adv').replace('n.\n, prep,adv.','n,prep,adv').replace('adn.\n/prep','adn,prep').replace('adv\n, conj','adv,conj.').replace('adj\n, exclam','adj,exclam.').replace('prep\n, in˜nitive marker today  adv\n, n.','prep, in˜nitive marker today,adv,n.').replace('n..','n.').replace('adj\n, pron\n, adv','adj,pron,adv.').replace('adj,n.\n, prep,adv.','adj,n,prep,adv.').replace('adj,n.\n, prep','adj,n,prep.').replace('exclam\n, n.','exclam,n.').replace('det,pron.\n, conj','det,pron,conj.').replace('adv\n, n.','adv,n.').replace('exclam\n, n,adj.','exclam,n,adj.').replace('adv\n, adj,exclam.','adv,adj,exclam.').replace('pron.\n/det','pron,det.').replace('adv\n, pron\n, conj','adv,pron,conj.').replace('adv\n, n.','adv,n.').replace('conj\n, adv','conj,adv.').replace('adj./adv\n, exclam','adj,adv,exclam.').replace('adv\n, pron','adv,pron.').replace('n.\n, exclam','n,exclam.').replace('adv\n, n.','adv,n.').replace('adj\n, det,pron,v.','adj,det,pron,v.').replace('prep\n, n,adj.','prep,n,adj.').replace('prep\n, conj','prep,conj.').replace('adv\n, adj','adv,adj.').replace('adj,n.\n, n.','adj,n,v.').replace('n,v.\n, adj','n,v,adj.').replace('adj,n.\n, conj','adj,n,coj.').replace('prep,adv.\n, n,adj.','prep,adv,n,adj.').replace('#####\n ','#####\n\n').replace('  1 / 12','').replace('  2 / 12','').replace('  3 / 12','').replace('  4 / 12','').replace('  5 / 12','').replace('  6 / 12','').replace('  7 / 12','').replace('  8 / 12','').replace('  9 / 12','').replace('  10 / 12','').replace('  11 / 12','').replace('  12 / 12','').replace('B1absolutely  adv','\nabsolutely adv').replace('A2ability  n.','ability n.').replace('B2abandon  n.','abandon n.').replace('C1abolish','C  abolish').replace('B2absorb','B2 absorb')
                  lignes = textList.split("\n")
                  listOfWords.extend(lignes)
                  while '' in listOfWords :
                       listOfWords.remove('')

         for i in range(len(listOfWords)):
            if listOfWords[i].find(" ")!= -1 :
                Space = listOfWords[i].index(" ")
                listOfWords[i]=listOfWords[i][:Space]
         for i in listOfWords :
             if i == '' or i ==',' :
                 listOfWords.remove(i)
         listOfWords.remove(listOfWords[listOfWords.index('As')])
         listOfWords.remove(listOfWords[listOfWords.index('abstract')-1])
         listOfWords.remove(listOfWords[0])
         listOfWords.insert(listOfWords.index('abstract'), 'absorb')
         listOfWords.insert(0,'an')
         listOfWords.insert(0,'a')
         listOfWords.insert(0, 'A1')
         listOfWords.insert((listOfWords.index('C')+1),'abolish')
         listOfWords.insert(listOfWords.index('yourself')+1, 'A2')
         listOfWords.insert(listOfWords.index('zero')+1, 'B1')
         listOfWords.insert(listOfWords.index('youth')+1, 'B2')

         return listOfWords

l = PdfWord.extractAndSortFileToText('all.pdf')








