#-------------------------------------------------------------------------------
# Copyright 2016-2017 All Rights Reserved by Surya Tej :p
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
# Import statements
#-------------------------------------------------------------------------------
import re  # Re Package for finding regular expressions in the File
import sys
from Tkinter import *   # Tkinter for GUI
import tkFileDialog as filedialog
import tkMessageBox
import webbrowser   # For Web Applications

#-------------------------------------------------------------------------------
# INITIALIZATION
#-------------------------------------------------------------------------------
# Starting Root TKINTER
root = Tk()
pypath = ''

# Functions to Print messages when pressed in Menu Bar
def warning_func():
    tkMessageBox.showerror(title = 'Warning!', message = "Warning! -> Means something that deviates from the Template \nCannot be Ignored")
    
def caution_func():
    tkMessageBox.showwarning(title = 'Caution!', message = "Caution! -> Double Check if its correct or not \nCan be Ignored")

# Message Box functions
def tool_docs_func():
    tkMessageBox.showinfo(title = "Tool Docs", message = "This Tool Basically compares your test script with Standard Template and throws the deviations")

def about_func():
    tkMessageBox.showinfo(title = "About Tool", message = "I Work only with Python 2.7, as of now")

def author_func():
    tkMessageBox.showinfo(title = "Author", message = "Surya Tej, smeda@rockwellcollins.com \nContact: 7708542808 \nAlways Welcome for Feedback")

# Info Menu Fucntions
def Read_Me_func():
    tkMessageBox.showinfo(title = "Read_Me", message = "Hey! Brilliant User, I dont Print any Findings if every thing is K.O! \nI mean OK")

def Apology_func():
    tkMessageBox.showinfo(title = "Sumimasen Deshita!", message = "I am Really Sorry If i give any Extra Finding \nAnd Extremely Sorry If I forget any Finding")

def what_i_check_func():
    checks = "The Following are the things that I check in your script: \n1. Copyright \n2. Line Seperators \n3. Few Unused Imports \n4. Delay Realted \n5. Usage of HardCode Values \n6. Label Min/Max stuff \n7. Section Headers and their Ordering \n8. Table Row Numbering \n9. Toggling of Outputs \n10. Minor Template Related Stuff"
    tkMessageBox.showinfo(title = "Things I Do!", message = checks)

def copyright_func():
    checks = "1. If file updation has a range - Ex: it was last updated in 2016, \n \
    the copyright must be like 2016-2017 \n \
    2. if not previous year , 2017.  Ex: 2014, 2017  or  2013-2015, 2017"
    tkMessageBox.showinfo(title = "How Copyright should be!", message = checks)
    
# Function for Hyper Link, Call Back
def callback(event):
    webbrowser.open_new(event.widget.cget("text"))

def Finding_File(event):
    webbrowser.open_new(event.widget.cget("text"))
    

# Creating a Menu
menubar = Menu(root)

# Info Menu
infomenu = Menu(menubar, tearoff = 0)
infomenu.add_command(label = "Read_Me", command = Read_Me_func)
infomenu.add_command(label = "Apology", command = Apology_func)
infomenu.add_command(label = "What I Check", command = what_i_check_func)

menubar.add_cascade(label = "Info", menu=infomenu)
root.config(menu = menubar)

# Finding Menu
# tear off prevents the removal of sub menu from Menu list
fidmenu = Menu(menubar, tearoff = 0)
fidmenu.add_command(label = "Warning!", command = warning_func)
fidmenu.add_command(label = "Caution!", command = caution_func)

menubar.add_cascade(label = "Findings", menu=fidmenu)
root.config(menu = menubar)

# Help Menu
# tear off prevents the removal of sub menu from Menu list
helpmenu = Menu(menubar, tearoff = 0)
helpmenu.add_command(label = "Tool Docs", command = tool_docs_func)
helpmenu.add_command(label = "About Auto_Review", command = about_func)
helpmenu.add_command(label = "Author", command = author_func)
helpmenu.add_command(label = "Copyright", command = copyright_func)

menubar.add_cascade(label = "Help!", menu=helpmenu)
root.config(menu = menubar)

root.geometry('750x600+500+300')
label_1 = Label(root, text="Step_1: Select the Test script, by clicking the Browse_Py Button")
label_2 = Label(root, text="Step_2: Script Type: Synoptics or Special Processing select Radio Button")
label_1.grid(row=3, sticky=W)
#label_1.pack()
label_2.grid(row=5, sticky=W)
#label_2.pack()

label_Template = Label(root, text = "If U want, Click on Hyper Link to open Standard Template in Browser")
label_Template.grid(row=7, sticky=W)
label_link = Label(root, text=r"http://alm.rockwellcollins.com/wiki/pages/viewpage.action?pageId=133403450", fg="blue", cursor="hand2")
label_link.grid(row =8, columnspan = 3)
label_link.bind("<Button-1>", callback)
label_radio_button = Label(root, text = "Step_3: Press the Indentify_Fid Button to generate Findings")
label_radio_button.grid(row = 9, sticky = W)

label_finding_file = Label(root, text = "Finally Click on the below Link to Open the Finding File When appeared")
label_finding_file.grid(row = 10, sticky = W)


# StringVar variable
var = StringVar()

Radio_1 = Radiobutton(root, text = "SYNOPTICS", value = 'S', variable = var)
Radio_2 = Radiobutton(root, text = "SPECIAL PROCESSING", value = 'C', variable = var)
Radio_1.grid(row = 6, columnspan = 1, sticky = W)
Radio_2.grid(row = 6, columnspan = 1, sticky = E)

#-------------------------------------------------------------------------------
# Global Function
#-------------------------------------------------------------------------------
    
def browsepy():
    root.fileName = filedialog.askopenfilename(filetypes=(("All Files", "*.*"), ("Py Files", "*.py")))
    

def buttonpress():
    pypath = str(root.fileName)
    fidpath = pypath[:-2] + "txt"
    w = open(fidpath, 'w')
    file_under_review = open(pypath)
    flist = list(file_under_review)
    fsize = len(flist)
    
    # ATP Type selection
    #atp_selector = raw_input( "<ENTER> S: for Synoptics, C: for any special processing: ")
    # Value Obatained From Radio Button Selection
    atp_selector = var.get()
    
    w.write( "\n")
    w.write( "#--------------------FINDINGS--------------------------------------\n")
    w.write( "\n")
    # Checking for Copyright Year
    if 'Copyright' not in flist[1]:  
        w.write( "-> Warning: Please Update Copyright as per Template\n")
    
    for i in range(0, 5):
        if 'Copyright' in flist[i]:
            if '2014' not in flist[i]:
                w.write( "-> Caution: Mention 2014 year if the File isnt a Newly Generated one in 2016\n")
    
    for i in range(0, 5):
        if 'Copyright' in flist[i]:
            if '2015' in flist[i]:
                w.write( "-> Caution: 2015 has to be changed to 2016 in the copyright section, if its getting modified\n")
            if '2017' not in flist[i]:
                w.write("-> Caution: 2017 has to be added to copyright.")
    for i in range(0, 5):
        if 'Copyright' in flist[i]:
            if 'Rockwell Collins. All Rights Reserved.' in flist[i]:
                pass
            else:
                w.write( "-> Warning: Incorrect Copyright, update as per template\n")
    
    # Checking Proprietary Information
    for i in range(0, 6):
        if 'Proprietary' in flist[i]:
            w.write( "-> Warning: Please Update the Copy Right as per Template\n")
    w.write( "\n")            
    
    # The Following Lines of code cross the 81 Character length
    def vertical_edge(x,i):
        a = x.strip()
        if len(a) > 80:
            w.write( "-> Warning: Line Seperator above 81 at " + str(i+1) + "\n")
        elif len(a) < 80:
            w.write( "-> Warning: Line Seperator below 81 at " + str(i+1) + "\n")
    w.write( "\n")
    # Import statements comment check
    for i in range(0, fsize):
        if re.search(r'#.*utilities', flist[i].lower()):
            if '#--' in flist[i-1]:
                w.write( "-> Warning: Replace uitlities with Import statements in Line " + str(i+1) + "\n")
    w.write( "\n")
    # Checking Presence of AUTOMATIC:
    for i in range(0, fsize):
        if 'AUTOMATIC' in flist[i] and 'verify' in (flist[i] or flist[i-1]):
            w.write('\n-> Warning: AUTOMATIC is no longer Applicable in Verify steps\n')
            w.write('If its in Verify Step replace it with auto_verify \n')
            w.write('If its in _a661 step, remove it\n\n')
            break
    # Removal of Comment after Initialization Section
    w.write( "\n")
    for i in range(0, fsize):
        if re.search(r'#\s*INITIALIZATION', flist[i]):
            if re.search(r'\wnitiali\w*', flist[i+2]):
                w.write("-> Warning: Any additional comment should be removed. after the 'Initialization' Seperator. \n" )
    # Line Seperator Check
    w.write( "\n")
    for i in range(0, fsize):
        if re.search("#-",flist[i]):
            vertical_edge(flist[i],i)
    
    # Avoiding import * in Test scripts
    w.write( "\n")
    for i in range(0,fsize):
        if 'import *' in flist[i]:
            if '#' not in flist[i]:
                w.write( "-> Warning: Import Required Parameters instead of '*' in Line " + str(i+1) + "\n")

    # Checking for unwanted imports
    w.write( "\n")
    import_list = ['DISCRETE_NORMAL', 'DISCRETE_FAIL', 'DISCRETE_NCD', 'DISCRETE_TEST', 'BNR_NORMAL', 'BNR_FAIL', 'BNR_NCD', 'BNR_TEST', 'BCD_NORMAL', 'BCD_FAIL', 'BCD_NCD', 'BCD_TEST','_DELAY_0', '_DELAY_1']
    for i in range(0, len(import_list)):
        import_count = 0
        for j in range(0, fsize):
            if import_list[i] in flist[j]:
                import_count = import_count + 1
        if import_count == 1:
             w.write( '-> Warning: There is an un used '+ import_list[i] + ' import\n')    
    
    
    # Checking for Vista.wait in the Test script
    w.write( "\n")
    for i in range(0, fsize):
        if 'vista.wait' in flist[i]:
            w.write( "-> Warning: Use EICAS_Wait instead of Vista.wait in Line " + str(i+1) + "\n")
    
    # Checking for Hard Code Value instead of imported parameter in EICAS_Wait
    # Checking for delay
    w.write( "\n")
    temp = 0
    w.write("Info: If label.delay is used as wait, the below delay related cautions [if arised] can be ignored \n")
    for i in range(0, fsize):
        if "EICAS_Wait" in flist[i]:
            if "EICAS_Wait(OUTPUTS" in flist[i]:
                pass
            elif "EICAS_Wait(delay" in flist[i]:
                w.write( "-> Warning: It must be OUTPUTS_DELAY_X and not delay at Line " + str(i+1) + "\n")
            else:
                if temp > 0:
                    w.write( "-> Caution: Use Imported Constant Like OUTPUTS_DELAY_X instead of Hard Code Value in Line " + str(i+1) + "\n")
                temp = temp + 1
    w.write( "\n")
    # Dude - When parameter.delay is used, the function has to be udpated!!!
    for i in range(0, fsize):
        if re.search(r'\welay\s*=\s*\d+', flist[i]):
            w.write( '-> Warning: Use EICAS_Wait function and remove the delay parameter ' + flist[i][:-1]  + " from the line "+ str(i+1) + "\n")
    
    # Checking for Presence of Graphical Description
    w.write( "\n")
    for i in range(0, fsize):
        if "Graphical Description" in flist[i]:
            w.write( "-> Warning: As per CR FUSN00530860, Graphical Description Section has to be removed from the Script at Line " + str(i+1) + "\n")
            break
    
    # Caution Messages for Max and Min Cases:
    w.write( "\n")
    for i in range(0,fsize):
        if re.search('#\s*\wax\s*\walue', flist[i]):
            if "N/A" in flist[i+2]:
                pass
            else:
                w.write( "-> Caution: Test For Label Max in Third Test Case, and mention comment in Robutsness seciton\n")
            break
    for i in range(0,fsize):
        if re.search('#\s*\win\s*\walue', flist[i]):
            if "N/A" in flist[i+2]:
                pass
            else:
                w.write( "-> Caution: Test For Label Min in Third Test Case, and mention comment in Robutsness seciton\n")
            break
    
    # Ordering of Section separators to be same as DOORs requirement section ordering.
    Synoptics_Sections = ["# input", "# filtering", "# resolution", "# hysteresis", "# max value", "# min value", "# functional processing", "# state", "# flashing", "# special", "test robustness"]
    
    Special_Processing_Sections = ["# input", "# global data", "# global functions", "# state", "# functional processing", "# special", "# output", "test robustness"]
    
    syn_len_exp = 66
    syn_len_act = 0
    
    w.write( "\n")
    if atp_selector.lower() == 's':
        for i in range(0, len(Synoptics_Sections)):
            l = 0
            for j in range(0, fsize):
                if Synoptics_Sections[i] in flist[j].lower():
                    #w.write( Synoptics_Sections[i]
                    l = 1
                    syn_len_act = syn_len_act + Synoptics_Sections.index(Synoptics_Sections[i])
                    break
        #w.write( syn_len_act
            if l == 0:
                w.write( "-> Warning: " + Synoptics_Sections[i] + " section header is missing from test script OR Some Deviation from the Template\n")
    
    spec_len_exp = 28
    spec_len_act = 0
    
    w.write( "\n")
    if atp_selector.lower() == 'c':
        for i in range(0, len(Special_Processing_Sections)):
            l = 0
            for j in range(0, fsize):
                if Special_Processing_Sections[i] in flist[j].lower():
                    #w.write( Synoptics_Sections[i]
                    l = 1
                    spec_len_act = spec_len_act + Special_Processing_Sections.index(Special_Processing_Sections[i])
                    break
            if l == 0:
                w.write( "-> Warning: " + Special_Processing_Sections[i] + " section header is missing from test script\n")
    
    # Test Case Numbering Check
    Test_Case_Count = 1
    w.write( "\n")
    # w.write( "Note: Test Case Numbering Check is for regular test scripts might not be suitable for class file")
    for i in range(0, fsize):
        string = 'Test Case ' + str(Test_Case_Count)
        m = re.search(r'\west \wase.+\d+', flist[i])
        if m:
            if string == m.group():
                pass
            else:
                if '#' not in flist[i]:
                    print 'Surya'
                    w.write( "-> Warning: Either Extra Spaces between 'Case and Number' or Incorrect Test case number at  Line " + str(i+1) + "\n")
            Test_Case_Count = Test_Case_Count + 1
    for i in range(0, fsize):
        if re.search(r'\west\s*\wase\s*\w*\s*\wow\s*\d*', flist[i]):
            w.write('\n-> Warning: Interchage Table Row and Test Case at Line ' + str(i+1) + "\n")
    
    # Checking for Table Row
    w.write( "\n")
    for i in range(0, fsize):
        if re.search('\s+Row\s+', flist[i]):
            if 'Table' not in flist[i]:
                if "#" not in flist[i]:
                    w.write( "-> Warning: As per template it must be Table Row at  Line " + str(i+1) + "\n")
        elif re.search('\s+row\s+', flist[i]):
            if 'Table' not in flist[i]:
                if "#" not in flist[i]:
                    w.write( "-> Warning: As per template it must be Table Row at  Line " + str(i+1) + "\n")

    
    # Checking for Row X/Y
    w.write( "\n")
    for i in range(0, fsize):
        if re.search('\s+Row\s+', flist[i]):
            if '/' not in flist[i]:
                w.write( "-> Warning: As per template row number must be of X/Y format at  Line " + str(i+1) + "\n")
        elif re.search('\s+row\s+', flist[i]):
            if '/' not in flist[i]:
                w.write( "-> Warning: As per template row number must be of X/Y format at  Line " + str(i+1) + "\n")
    
    # Replacing # outputs to # Expected
    w.write( "\n")
    for i in range(0, fsize):
        if re.search(r'#\s*\wutput',flist[i]):
            if not '#--' in flist[i-1]:
                if not (re.search(r'\s+#\s*\wutput',flist[i])):
                    w.write( "-> Warning: It has to be # Expected not # Outputs in Line " + str(i+1) + "\n")

    # Replacing #input to # Inputs
    w.write( "\n")
    for i in range(0, fsize):
        if re.search(r'#\wnput',flist[i]):
            if not '#--' in flist[i-1]:
                w.write( "-> Warning: It has to be # Inputs not #input in Line " + str(i+1) + "\n")

    # checking for logger.setTestcase
    w.write( "\n")
    for i in range(0, fsize):
        if 'logger.setTestCase' in flist[i]:
            w.write( "-> Warning: Remove the 'logger.setTestCase' from the script at Line " + str(i+1) + "\n")
            
    # Ordering of section headers: check
    w.write( "\n")
    if atp_selector.lower() == 's':
        syn_section_header_list = []
        temp_list = []
        for j in range(0, len(Synoptics_Sections)):
            for i in range(0, fsize):
                if Synoptics_Sections[j] in flist[i].lower():
                    if '#--' in flist[i-1] and '#--' in flist[i+1]:
                        syn_section_header_list.append(i+1)
                        temp_list.append(i+1)
                        break
        temp_list.sort()
        for l in range(0, len(temp_list)):
            if temp_list[l] == syn_section_header_list[l]:
                pass
            else:
                w.write( "-> Warning: Section Headers are not arranged properly for " + flist[temp_list[l]-1] + " Refer Template for info\n")
    
    if atp_selector.lower() == 'c':
        spec_section_header_list = []
        temp_list = []
        for j in range(0, len(Special_Processing_Sections)):
            for i in range(0, fsize):
                if Special_Processing_Sections[j] in flist[i].lower():
                    if '#--' in flist[i-1] and '#--' in flist[i+1]:
                        spec_section_header_list.append(i+1)
                        temp_list.append(i+1)
                        break
        #w.write( spec_section_header_list            
        temp_list.sort()
        for l in range(0, len(temp_list)):
            if temp_list[l] == spec_section_header_list[l]:
                pass
            else:
                w.write( "-> Warning: Section Headers are not arranged properly for " + flist[temp_list[l]-1] + " Refer Template for info\n")
    
    # hard code values check
    w.write( "\n")
    for i in range(0, fsize):
        if '(0)' in flist[i]:
            w.write( "-> Warning: Use FALSE or Corresponding import and not hard code value at line " + str(i+1) + ' Ignore if its ENUM\n')
        elif '(1)' in flist[i]:
            w.write( "-> Warning: Use TRUE or Corresponding import and not hard code value at line " + str(i+1) + ' Ignore if its ENUM\n')
        elif '(2)' in flist[i]:
            w.write( "-> Warning: Use imported constant and not hard code value at line " + str(i+1) + ' Ignore if its ENUM\n')
        elif '(3)' in flist[i]:
            w.write( "-> Warning: Use imported constant and not hard code value at line " + str(i+1) + ' Ignore if its ENUM\n')
    
    # Checking for Verify Statements
    w.write( "\n")
    verify_list = []
    verify_list_num = []
    for i in range(0, fsize):
        if 'verify(' in flist[i]:
            if ')' in flist[i]:
                verify_list.append(flist[i])
                verify_list_num.append(i+1)
    
    Flag = 0
    for i in range(0 , len(verify_list) - 1):
        if verify_list[i] == verify_list[i+1] :
            Flag = 1
            w.write( "-> Warning: Have Toggling of output in Verify Statement at Line " + str(verify_list_num[i+1]) + "\n")
    if (Flag > 0):
        w.write('\n The Warning realted to Toggling of ouput can be Ignored if its in Hysteresis/Max/Min Test cases or any other Exception\n')
    
    # cautions to User:
    if atp_selector.lower() == 's':
        caution_text = "Have 2 TCs for Resolution, \nHave 4 TCs for Hysteresis, \nMention comment under section header when clubbed with other TCs, \nRemove unwanted space, empty lines, tab spaces "
        tkMessageBox.showinfo(title = "Reminder", message = caution_text)

    if atp_selector.lower() == 'c':
        caution_text = "Mention comment under section header when clubbed with other TCs, \nRemove unwanted space, empty lines, tab spaces "
        tkMessageBox.showinfo(title = "Reminder", message = caution_text)

    for i in range(0 , fsize):
        if '.close()' in flist[i]:
            if '#' not in flist[i-1]:
                w.write('\n-> Caution: Make sure u mention a comment to Close the Log File\n')

    label_link_2 = Label(root, text=fidpath, fg="blue", cursor="hand2")
    label_link_2.grid(columnspan = 2)
    label_link_2.bind("<Button-1>", Finding_File)
    label_2 = Label(root, text = "!!!Script Auto Reviewed!!!")
    label_2.grid(columnspan = 2)

    file_under_review.close()
    w.close()


browse_button = Button(root, text=" __Browse_Py__ ", command=browsepy)
browse_button.grid(row = 3, column = 1, sticky = E)
#browse_button.pack()
Finding_button = Button(root, text=" __Identify_Findings__", command=buttonpress)
Finding_button.grid(row = 9, column = 1,sticky = E)
#Finding_button.pack()
#-------------------------------------------------------------------------------
#----------------------End of Test----------------------------------------------
#-------------------------------------------------------------------------------

root.title("!!-----------Auto Review Tool---------!!")
root.mainloop()
'''
# Code Documentation   -- # Only for Surya
Nov - 22
1. Still GUI has to be prepared to select the file - > refer the Test case gen tool that has info # - Done
2. Instead of printing the Findings Export them to a text File if possible with the Filename u ran in the same folder location # Done
# that would be coooool
3. Check for Unwanted imported parameters in the script # Sort of Done
4. If taken into Tool, i guess all for loops must go into a Function call i suppose
5. Instead of Multiple Copyright checks do this.. # Done
if copyright in line: check if Rockwell Collins. All Rights Reserved. exists or not>>

'''
