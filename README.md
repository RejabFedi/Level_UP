# Level_UP
Books scan application
An application can get the content of a book and return many statistic about it 

#The manager file of the application to create or modify the DB is "main.py"
#The main file to get the output of the application is "Affiche.py" 

#Create.Db.py
Content methods of creating the database of words linked to their levels 
#CreateBook.py 
Content methods of creating a book in the database
#CreateListOfWords.py
Extract the content of the  Oxford 3000™ and 5000 by CEFR level (All.pdf) to a list content the level name followed by the words who belong to
#CreateTenseNodes.py
Content methods of creating a tnese nodes in the DB 
#FindWord.py
Search a word in the database and retund the name of the level who linked to
#ForAffiche.py 
Content methods who collect the data and analyse them and Prepare them to the Afiichage.py
#GetNode.py
Search a node in the database an deturn the name of the node 
#GetTense.py 
Brose the list of words and every time if we found a verb, GetTense will analyse the syntax of the sentense and conclude in whitch time that the verb is conjugated , in other side GetTense conclude the infinitive of the conjugated verb and return the level of the verbe
#listOfLevelsOP.py
Brose the list (content of the book ) and use GetTense.py and FindWord.py to return a list of using levels ( [A1,A2,C...... ]) as return , to use hereafter in Affiche.py
#readBook.py
Get a picure of a page as input and scan it using pytesseract to trosform it to a text then a list as output 
