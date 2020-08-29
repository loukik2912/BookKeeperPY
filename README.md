# BookKeeperPY
A simple Python project for maintaining a record of your local e-book files

Hi, welcome to BookKeeperPY! This project came into being from my love of reading books - I'm an avid reader, and I prefer the old-school technique of downloading the e-books to my local machine for reading. Recently, I decided to organize my collection which was stored in a directory, and maintain a record - but I'm lazy, so I decided to automate the procedure.

Luckily, I do maintain a semblance of order while adding books to the collection. Firstly, I add them in directories named year-wise, and secondly I name the series' directory in format of <Author_name> - <Series_name/Book_name>. For Standalone books, I create a separate directory alongside year-wise named 'Standalone' and rename books inside it in the same format as earlier. To illustrate with a section of the directory tree:

```
Books
+---2016
|   +---J.K.Rowling - The Harry Potter Series
|   |   +---1-Harry Potter and the Sorcerer_s Stone.epub
|   |   +---2-Harry Potter and the Chamber of Secrets.epub
+---Standalone
|   +---Dan Millman - Way of the Peaceful Warrior.epub
|   +---Neil Gaiman - Norse Mythology.epub
|   +---Yuval Harari - Sapiens.epub
|   +---Sir Arthur Conan Doyle - The Complete Sherlock Holmes.mobi
```

What this does is that it converts the directory listings into book-entry objects containing 3 fields - Author name, Series/Book name & whether it is a Standalone/Series.
It then generates a CSV file containing all this data. Then an HTML file is generated for viewing the data in table a browser for a more aesthetic look.  
![Booksviewer_HTML_table](/booksviewer.png?raw=true)  
To use this, run create_csv.py & follow the instructions...

For now, this is just a fun side-project :) But in the future, I'd like to integrate more features as I learn about them (to add a UI & other fields & make filtering possible)...
