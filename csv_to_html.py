import os, sys
import csv

def create_html_page(filePath):
    print(os.path.join(os.getcwd(), 'booksviewer.html'))
    with open(os.path.join(os.getcwd(), 'booksviewer.html'), 'w+') as html_fp:
        webpage_string = "<!DOCTYPE html>\n<html>\n<head>"\
        + get_HeadString() + \
        "</head>\n<body>\n"\
        + get_BodyString(filePath) + \
        "</body>\n</html>"

        html_fp.write(webpage_string)

def get_HeadString():
    return (get_TopicString() + get_StyleString())

def get_TopicString():
    return "\n<h1>List Of Books</h1>\n"

def get_StyleString():
    return "\n<style>\n\
    table, th, td {\n\
    border: 0.5px solid black;\n\
    border-collapse: collapse;\n\
    }\n\
    table.center {\n\
    margin-left: auto;\n\
    margin-right: auto;\n\
    }\n\
    </style>\n"

def get_BodyString(filePath):
    with open(filePath, 'r') as csv_fp:
        csvReader = csv.DictReader(csv_fp)
        
        table_head = "<table>\n\t<tr>"
        for colName in csvReader.fieldnames:
            table_head += ("<th>" + colName + "</th>")
        table_head += "</tr>\n"

        table_content = ""
        for rowEntry in csvReader:
            table_content += "\t<tr> "
            for colName in csvReader.fieldnames:
                table_content += ("<td>" + rowEntry[colName] + "</td> ")
            table_content += "</tr>\n"
        table_content += "</table>\n"

        return (table_head + table_content)

if __name__ == "__main__":
    inputFilePath = input("Enter the complete file path of the CSV file:\t")
    create_html_page(inputFilePath)
