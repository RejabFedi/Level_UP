import GetNode
import createListOfWords
import createDb
import CreateTenseNodes
import readBook
import test
import listOfLevelsOP
import FindWord
import GetTense
import nltk
import CreateBook
import ForAffiche
if __name__ == "__main__":
   #Create data base
   #createDb.Create.creation(createListOfWords.PdfWord.extractAndSortFileToText('all.pdf'))

   #Add Times nodes to the data base
   '''
   
   A1 = GetNode.Match_nodes('Level', 'A1')
   A2 = GetNode.Match_nodes('Level', 'A2')
   B1 = GetNode.Match_nodes('Level', 'B1')
   B2 = GetNode.Match_nodes('Level', 'B2')
   C = GetNode.Match_nodes('Level', 'C')
   
   SimplePresent=CreateTenseNodes.CreateTenseNodes.create_Tense('Simple Present')
   createDb.Create.create_relationship(A1, GetNode.Match_nodes('Tense', 'Simple Present'))
   Presentperfectprogressive = CreateTenseNodes.CreateTenseNodes.create_Tense('Present perfect progressive')
   createDb.Create.create_relationship(B1, GetNode.Match_nodes('Tense', 'Present perfect progressive'))
   PresentPerfect = CreateTenseNodes.CreateTenseNodes.create_Tense('Present Perfect')
   createDb.Create.create_relationship(A2, GetNode.Match_nodes('Tense', 'Present Perfect'))
   PresentProgressive = CreateTenseNodes.CreateTenseNodes.create_Tense('Present Progressive')
   createDb.Create.create_relationship(A2, GetNode.Match_nodes('Tense', 'Present Progressive'))

   SimplePast=CreateTenseNodes.CreateTenseNodes.create_Tense('Simple Past')
   createDb.Create.create_relationship(a, SimplePast)
   pastProgressive = CreateTenseNodes.CreateTenseNodes.create_Tense('past Progressive')
   createDb.Create.create_relationship(B1, GetNode.Match_nodes('Tense', 'past Progressive'))
   Pastperfectprogressive = CreateTenseNodes.CreateTenseNodes.create_Tense('Past perfect progressive')
   createDb.Create.create_relationship(B2, GetNode.Match_nodes('Tense', 'Past perfect progressive'))
   PastPerfect = CreateTenseNodes.CreateTenseNodes.create_Tense('Past perfect')
   createDb.Create.create_relationship(B1, GetNode.Match_nodes('Tense', 'Past perfect'))

   goingtofuture=CreateTenseNodes.CreateTenseNodes.create_Tense('going to future')
   createDb.Create.create_relationship(A2, GetNode.Match_nodes('Tense', 'going to future'))
   willfuture = CreateTenseNodes.CreateTenseNodes.create_Tense('will future')
   createDb.Create.create_relationship(A2, GetNode.Match_nodes('Tense', 'will future'))
   futureprogressive = CreateTenseNodes.CreateTenseNodes.create_Tense('future progressive')
   createDb.Create.create_relationship(B1, GetNode.Match_nodes('Tense', 'future progressive'))
   futureperfect = CreateTenseNodes.CreateTenseNodes.create_Tense('future perfect')
   createDb.Create.create_relationship(B2, GetNode.Match_nodes('Tense', 'future perfect'))
   futureperfectprogressive = CreateTenseNodes.CreateTenseNodes.create_Tense('future perfect progressive')
   createDb.Create.create_relationship(B2, GetNode.Match_nodes('Tense', 'future perfect progressive'))

   conditionalsimple=CreateTenseNodes.CreateTenseNodes.create_Tense('conditional simple')
   createDb.Create.create_relationship(C, GetNode.Match_nodes('Tense', 'conditional simple'))
   conditionalprogressiv = CreateTenseNodes.CreateTenseNodes.create_Tense('conditional progressive')
   createDb.Create.create_relationship(C, GetNode.Match_nodes('Tense', 'conditional progressive'))
   conditionalperfect = CreateTenseNodes.CreateTenseNodes.create_Tense('conditional perfect')
   createDb.Create.create_relationship(C, GetNode.Match_nodes('Tense', 'conditional perfect'))
   conditionalperfectprogressive = CreateTenseNodes.CreateTenseNodes.create_Tense('conditional perfect progressive')
   createDb.Create.create_relationship(C, GetNode.Match_nodes('Tense', 'conditional perfect progressive'))
    
'''
