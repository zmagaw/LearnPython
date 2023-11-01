import sys
import os 

print('Original sys.path:', sys.path)

current_working_directory = os.getcwd()

print("cwd: " + current_working_directory)



sys.path.append('../')

print('New sys.path:', sys.path)


##import TutorialModule
##import mock
##import builtins


#test to see if you name is returned? (not sure great test)
##def test_answer():
##        with mock.patch.object(builtins, 'input', lambda _: 'Bobalicious'):
##                assert TutorialModule.greet() == "Bobalicious"

#test to see if dictionary returned is correct length - wondering if we have to see if the correct format
##def test_fileDictionary():
##    d = TutorialModule.readFile()
##    dictCount = len(d)
##    with open('../temp/usernames.txt','r') as temp_file:
##        lineCount = len(temp_file.readlines())
##    assert lineCount == dictCount
##    temp_file.close()
##    return d