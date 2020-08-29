import os, sys
import csv

def getListFromDir(filePath):
    ''' Reads a parent directory and returns a list of string entries '''
    listofBooks = list()
    standalone_cnt = 0
    for rootPath, subDirs, subFiles in os.walk(filePath):
        if os.path.basename(rootPath) == 'Standalone':
            for aFile in subFiles:
                listofBooks.append(aFile.split('.')[0] + ' - Standalone')
                standalone_cnt += 1
        elif not ('-' in os.path.basename(rootPath)):
            continue
        else:
            listofBooks.append(os.path.basename(rootPath))

    #print("Total books: ", len(listofBooks), "Standalone books: ", standalone_cnt)
    return listofBooks

def makeDictEntry(inputStr):
    ''' Takes a string entry and formats it into a dictionary form '''
    if inputStr:
        listofStrs = [x.strip() for x in inputStr.split('-')]
        if 'Standalone' in listofStrs:
            return {'Author' : listofStrs[0], 'Book_name' : listofStrs[1], 'Type' : listofStrs[2]}
        else:
            return {'Author' : listofStrs[0], 'Book_name' : listofStrs[1], 'Type' : 'Series'}

def makeDictEntries(inputList):
    ''' Takes a list of string entries and returns a list of dictionary entries '''
    if inputList:
        return [makeDictEntry(x) for x in inputList]

def readDir_makeCsv(dir_file_path, csv_file_path):
    ''' Reads directory path input & adds to CSV file path specified in input '''
    with open(csv_file_path, 'a+', newline='') as csv_fp:
        g_listofBooks = getListFromDir(dir_file_path)
        g_entries = makeDictEntries(g_listofBooks)
        if g_entries:
            for anEntry in g_entries:
                print(anEntry)
                csv.DictWriter(csv_fp, fieldnames=['Author', 'Book_name', 'Type']).\
                    writerow({'Author' : anEntry['Author'], 'Book_name' : anEntry['Book_name'], 'Type': anEntry['Type']})
        else:
            print('Encountered an error - Directory file path invalid!')
    
def readStr_makeCsv(input_info_string, csv_file_path):
    with open(csv_file_path, 'a+', newline='') as csv_fp:
        g_entries = makeDictEntries([input_info_string])
        if g_entries:
            for anEntry in g_entries:
                print(anEntry)
                csv.DictWriter(csv_fp, fieldnames=['Author', 'Book_name', 'Type']).\
                    writerow({'Author' : anEntry['Author'], 'Book_name' : anEntry['Book_name'], 'Type': anEntry['Type']})
        else:
            print('Encountered an error - Directory file path invalid!')

def debug_readDir(filePath):
    r_listofBooks = getListFromDir(filePath)
    r_entries = makeDictEntries(r_listofBooks)
    if r_entries:
        for anEntry in r_entries:
            print(anEntry)
        print('Total entries:', len(r_entries))
    else:
        print('Error - cannot decode information!')

def debug_readStr(input_info_string):
    g_entries = makeDictEntries([input_info_string])
    if g_entries:
        for anEntry in g_entries:
            print(anEntry)
    else:
        print('Encountered an error - Directory file path invalid!')

if __name__ == "__main__":
    while True:
        print("WELCOME TO BookKeeperPY. Please follow the commands listed ahead to create/modify a CSV file,", end='')
        print("then head over to the csv_to_html.py to generate an HTML file which can be viewed in a browser!")
        print("Please press the keys enclosed in brackets() in the following prompts to answer...")

        debug_char = input("Please choose whether you want to work in Debug mode(Y) or in actual mode(N):\t").lower()
        prompt_message = "Choose your options:\nDirectory to CSV(1)  String to CSV(2)  Any other char to exit(E):\t"
        opt_char = input(prompt_message).lower()

        if opt_char == "1":
            inputDir = input("Type the full input directory path:\t")
            csvPath = input("Type the full CSV file path:\t")
            if debug_char == "y":
                debug_readDir(inputDir)
            else:
                readDir_makeCsv(inputDir, csvPath)
        elif opt_char == "2":
            inputStr = input("Type the entry string in the format <Author_name> - <Book_name> - <if Standalone>:\t")
            csvPath = input("Type the full CSV file path:\t")
            if debug_char == "y":
                debug_readStr(inputStr)
            else:
                readStr_makeCsv(inputStr, csvPath)
        else:
            break
