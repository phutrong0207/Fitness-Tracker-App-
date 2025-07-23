import tkinter as tk   # Importing the tkinter module for GUI and renaming it as tk     
from tkinter import *   # Importing the tkinter module for GUI
from tkinter import messagebox,ttk,Frame,Label  # Importing the messagebox,ttk,Frame,Label from tkinter module
import customtkinter as ctk #Importing the customtkinter module for custom widgets that are not available in tkinter and renaiming it as ctk
from PIL import Image, ImageTk # Importing the Image and ImageTk from PIL module for image processing and image resizing
import csv # Importing the csv module for reading and writing csv files


#Creating files for different functions of the application and every file has a header row that will not be written again if the file already exists from line 10 to 64
with open('account info','a',newline='') as booking:
    header=csv.writer(booking)
    with open('account info','r') as booking:
        fl=csv.reader(booking)
        firstLine=next(fl,None)
        if firstLine!=['Username', 'Password']:
            header.writerow(['Username', 'Password'])

with open('activities log','a',newline='') as booking:
    header=csv.writer(booking)
    with open('activities log','r') as booking:
        fl=csv.reader(booking)
        firstLine=next(fl,None)
        if firstLine!=['Username', 'Activity', 'Duration', 'Intensity Level','Energy Needed','Distance']:
            header.writerow(['Username', 'Activity', 'Duration', 'Intensity Level','Energy Needed','Distance'])

with open('info','a',newline='') as booking:
    header=csv.writer(booking)
    with open('info','r') as booking:
        fl=csv.reader(booking)
        firstLine=next(fl,None)
        if firstLine!=['Username','Age', 'Height', 'Weight', 'Gender']:
            header.writerow(['Username', 'Age', 'Height', 'Weight', 'Gender'])

with open('calorie and food','a',newline='') as booking:
    header=csv.writer(booking)
    with open('calorie and food','r') as booking:
        fl=csv.reader(booking)
        firstLine=next(fl,None)
        if firstLine!=['Username','Food','Calories','Macronutrients']:
            header.writerow(['Username','Food','Calories','Macronutrients'])

with open('calorie need and acti level','a',newline='') as booking:
    header=csv.writer(booking)
    with open('calorie need and acti level','r') as booking:
        fl=csv.reader(booking)
        firstLine=next(fl,None)
        if firstLine!=['Username','Daily Calorie Needs','Activity Level']:
            header.writerow(['Username','Daily Calorie Needs','Activity Level'])

with open('total calorie and total macronutrient','a',newline='') as booking:
    header=csv.writer(booking)
    with open('total calorie and total macronutrient','r') as booking:
        fl=csv.reader(booking)
        firstLine=next(fl,None)
        if firstLine!=['Username','Total Calorie','Total Protein','Total Carbohydrates','Total Fat']:
            header.writerow(['Username','Total Calorie','Total Protein','Total Carbohydrates','Total Fat'])

with open('goal','a',newline='') as booking:
    header=csv.writer(booking)
    with open('goal','r') as booking:
        fl=csv.reader(booking)
        firstLine=next(fl,None)
        if firstLine!=['Username','Activity Type','Target Distance']:
            header.writerow(['Username','Activity Type','Target Distance'])


def log_out():  #Function to log out of the application by destroying the main page and calling the sign_in_page function
    main_page.destroy()
    sign_in_page()

def home_page():    #Function to destroy the sign in page and display a screen with a welcome message and functions of the application
    root.destroy()
    #Call global variables to access it in other functions
    global main_page
    global main_frame
    #Creating the main page and title of the page from line 77 to 86
    main_page=tk.Tk()
    main_page.geometry('1500x800+100+80')
    main_page.title('Fitness Tracker')
    main_page.resizable(False,False)

    main_frame=tk.Frame(main_page,width=1500,height=800,bg='#f0f0f0')
    main_frame.place(x=0,y=0)
    main_page.configure(bg='#f0f0f0')
    title=Label(main_frame,text='Welcome to Fitness Tracker',fg='#5c547e',bg='#f0f0f0',font=('Helvetica',35,'bold'))
    title.place(x=430,y=50)
    user_info_exist=False #Variable to check if the user information already exists in the file
    with open('info','r') as activity:  #Checking if the personal information already exists in the file by iterating through the file to find the username
        allActivities=csv.reader(activity)
        infolist=list(allActivities)
        line_num=len(infolist)
        for i in range(line_num-1,0,-1):
            if len(infolist[i])>=5:
                if name in infolist[i]:
                    user_info_exist=True
    if user_info_exist==False: #If the user information does not exist, the user will be asked to enter the personal information (from line 96 to 261)
        info_page=tk.Frame(main_page,width=1500,height=800,bg='#f0f0f0')
        info_page.place(x=0,y=0)
        info_page.configure(bg='#f0f0f0')
        title2=Label(info_page,text='Welcome to Fitness Tracker',fg='#5c547e',bg='#f0f0f0',font=('Helvetica',35,'bold'))
        title2.place(x=430,y=50)
        year_Label=ctk.CTkLabel(
            info_page,
            text='Age:',
            font=('Helvetica',15),
            text_color='#5c547e',
        )
        year_Label.place(x=640,y=200)

        age_in_year=ctk.CTkLabel(
            info_page,
            text='Years',
            font=('Helvetica',15),
            text_color='black',
        )
        age_in_year.place(x=830,y=200)

        year=ctk.CTkEntry(
            info_page,
            fg_color=('black','white'),
            text_color='black',
            width=140,
            height=30,
            corner_radius=10,
            font=('Helvetica',15),
            placeholder_text='Enter your age'
        )
        year.place(x=680,y=200) 

        height_Label=ctk.CTkLabel(
            info_page,
            text='Height:',
            font=('Helvetica',15),
            text_color='#5c547e',
        )
        height_Label.place(x=620,y=250)

        height=ctk.CTkEntry(
            info_page,
            fg_color=('black','white'),
            text_color='black',
            width=140,
            height=30,
            corner_radius=10,
            font=('Helvetica',15),
            placeholder_text='Enter your height',
        )
        height.place(x=680,y=250)

        height_in_cm=ctk.CTkLabel(
            info_page,
            text='cm',
            font=('Helvetica',15),
            text_color='black',
        )
        height_in_cm.place(x=830,y=250)

        weight_Label=ctk.CTkLabel(
            info_page,
            text='Weight:',
            font=('Helvetica',15),
            text_color='#5c547e',
        )
        weight_Label.place(x=620,y=300)

        weight_in_cm=ctk.CTkLabel(
            info_page,
            text='kg',
            font=('Helvetica',15),
            text_color='black',
        )
        weight_in_cm.place(x=830,y=300)
        global weight
        weight=ctk.CTkEntry(
            info_page,
            fg_color=('black','white'),
            text_color='black',
            width=140,
            height=30,
            corner_radius=10,
            font=('Helvetica',15),
            placeholder_text='Enter your weight',
        )
        weight.place(x=680,y=300)
        gender_var=ctk.StringVar(value='Female')  


        gender_Label=ctk.CTkLabel(
            info_page,
            text='Gender:',
            font=('Helvetica',15),
            text_color='#5c547e',
        )
        gender_Label.place(x=620,y=350)

        def continue_func():#Function to check if the user has entered the personal information and if the information is valid to access the home page from line 196 to 242
            age=year.get()
            hei=height.get()
            wei=weight.get()
            
            if age=='' and hei!='' and wei!='':
                messagebox.showerror('Invalid','Age is required')
            elif hei=='' and age!='' and wei!='':
                messagebox.showerror('Invalid','Height is required')
            elif wei=='' and age!='' and hei!='':
                messagebox.showerror('Invalid','Weight is required')
            elif age=='' and hei=='' and wei!='':
                messagebox.showerror('Invalid','Age and Height are required')
            elif age=='' and wei=='' and hei!='':
                messagebox.showerror('Invalid','Age and Weight are required')
            elif hei=='' and wei=='' and age!='':
                messagebox.showerror('Invalid','Height and Weight are required')
            elif age=='' and hei=='' and wei=='':
                messagebox.showerror('Invalid','Age, Height and Weight are required')
            else:
                if age.isdigit()==False or int(age)<=0:
                    messagebox.showerror('Invalid','Age, Height, Weight must all be a numbers and greater than 0')
                    year.insert(0,'')
                elif hei.isdigit()==False or int(hei)<=0:
                    messagebox.showerror('Invalid','Age, Height, Weight must all be a numbers and greater than 0')
                    height.insert(0,'')
                elif wei.isdigit()==False or int(wei)<=0:
                    messagebox.showerror('Invalid','Age, Height, Weight must all be a numbers and greater than 0')
                    weight.insert(0,'')
                elif age.isdigit()==True and hei.isdigit()==True and wei.isdigit()==True and int(age)> 0 and int(hei)>0 and int(wei)>0:
                    age=int(year.get())
                    hei=int(height.get())
                    wei=int(weight.get())
                    global bmr
                    bmr=0
                    bmr=bmr+10*wei+6.25*hei-5*age+5
                    #if the personal information is valid, the information will be written to the file and the user will be directed to the home page
                    with open('info','a',newline='') as activity:
                        writecalo=csv.writer(activity)
                        with open('info','r') as activity:
                            allActivities=csv.reader(activity)
                            infolist=list(allActivities)
                            if [name,str(age),str(hei),str(wei),gender_var.get()] not in infolist:
                                writecalo.writerow([name,age,hei,wei,gender_var.get()])
                            elif [name,str(age),str(hei),str(wei),gender_var.get()] in infolist and [name,str(age),str(hei),str(wei),gender_var.get()] != infolist[-1]:
                                writecalo.writerow([name,age,hei,wei,gender_var.get()])
                    info_page.place_forget() #Forget the personal information page after the information has been written to the file
        
        continue_button=ctk.CTkButton(
            info_page,
            text='Continue',
            width=100,
            height=40,
            corner_radius=10,
            fg_color=('white','#5c547e'),
            hover_color=('white','#37334A'),
            font=('Helvetica',15),
            hover=True,
            command=continue_func,
        )
        continue_button.place(x=690,y=400)

        female=ctk.CTkRadioButton(info_page,text="Female",fg_color='black',bg_color='#f0f0f0',text_color='black',value='Female',variable=gender_var)
        female.place(x=680,y=350)
        male=ctk.CTkRadioButton(info_page,text="Male",fg_color='black',bg_color='#f0f0f0',text_color='black',value='Male',variable=gender_var)
        male.place(x=780,y=350)

    def log(): #function allowing user to add activities to the activities log
        def go_back1(): #function once triggered will forget the current page and display the home page
            page_1.pack_forget()
        global page_1 #create page 1 as a global variable
        page_1=tk.Frame(main_frame,width=1500,height=800,bg='#f0f0f0') #create a frame for page 1 and add the title of the page
        title_page_1=Label(page_1,text='Physical Activities Log',fg='#5c547e',bg='#f0f0f0',font=('Helvetica',35,'bold'))
        title_page_1.place(x=470,y=70)
        page_1.pack(fill=tk.BOTH,expand=True)

        back_button=ctk.CTkButton(#add a back button which can trigger tthe fucntion go_back1
            page_1,
            text='<-- Back',
            width=100,
            height=40,
            corner_radius=10,
            fg_color=('white','#5c547e'),
            hover_color=('white','#37334A'),
            font=('Helvetica',15),
            hover=True,
            command=go_back1,
        )
        back_button.place(x=30,y=20)
        def create_log(): #function to create the activities log and display the activities that the user has added by reading the activities log file (from 286 to316)
            global phy_log
            phy_log=ttk.Treeview(page_1,height=26)#create a table treeview to display the activities log and add the columns and headings of the table 288-302
            phy_log['columns']=('Activity','Duration','Intensity Level','Energy Needed','Distance')

            phy_log.column('#0',width=0,stretch=tk.NO)
            phy_log.column('Activity',anchor=tk.CENTER,width=150)
            phy_log.column('Duration',anchor=tk.CENTER,width=200)
            phy_log.column('Intensity Level',anchor=tk.CENTER,width=130)
            phy_log.column('Energy Needed',anchor=tk.CENTER,width=130)
            phy_log.column('Distance',anchor=tk.CENTER,width=100)

            phy_log.heading('#0',text='',anchor=tk.W)
            phy_log.heading('Activity',text='Activity',anchor=tk.CENTER)
            phy_log.heading('Duration',text='Duration',anchor=tk.CENTER)
            phy_log.heading('Intensity Level',text='Intensity Level',anchor=tk.CENTER)
            phy_log.heading('Energy Needed',text='Energy Needed',anchor=tk.CENTER)
            phy_log.heading('Distance',text='Distance',anchor=tk.CENTER)
            #read the activities csv file and display the activities that the user has added to the activities log
            with open('activities log','r') as activity:
                allActivities=csv.reader(activity)
                next(allActivities)
                for line in allActivities:
                    if len(line)==4:#if the length of the line is 4, the activity is walking, running, cycling or swimming
                        if line[0]==name:
                            phy_log.insert(parent='',index='end',text='',values=(line[1],'','',line[2],line[3]+'km'))
                    elif len(line)==5:#if the length of the line is 5, the activity is gym activities, training and sport activities, outdoor activities or home & daily activities
                        if line[0]==name:
                            phy_log.insert(parent='',index='end',text='',values=(line[1],line[2],line[3],line[4]))
                    
            phy_log.place(x=370,y=150)
        create_log() #call the create_log function to display the activities log when the user uses the log function
        def deleteAll_act(): #function to delete all the activities in the activities log and clear the activities log file (from 318 to 324)
            with open('activities log', 'r') as booking:
                allActivities = csv.reader(booking)
                activities_list = list(allActivities)
                # Write back only the activities that do not belong to the current user
            with open('activities log', 'w', newline='') as booking:
                header = csv.writer(booking)
                header.writerow(['Username', 'Activity', 'Duration', 'Intensity Level', 'Energy Needed', 'Distance'])
                for line in activities_list[1:]:  # Skip the header row
                    if len(line) >= 4 and line[0] != name:  # Keep activities of other users
                        header.writerow(line)
            create_log()
        def add_acti(): #function to add activities to the activities log and display the add activity page (from 326 to 486)
            #creating a window for the user to input the information of activities
            add_page=tk.Toplevel()
            add_page.title('Add Activity')
            add_page.geometry('350x200+530+280')
            acti_type_Label=ctk.CTkLabel(
                add_page,
                text='Activity Type:',
                font=('Helvetica',15),
                text_color='black',
            )
            acti_type_Label.place(x=55,y=50)
            #list of activities that the user can choose from to add to the activities log and a combobox to display the list
            activity_list=['Walking', 'Running', 'Cycling', 'Swimming','Gym Activities','Training and Sport Activities','Outdoor Activities','Home & Daily Activities']
            acti_type=ttk.Combobox(add_page,values=activity_list)
            acti_type.place(x=150,y=50)
            def further_add(): #function to create another window for the user to input the information of the activity based on the activity type selected
                def save_add1(): #function to calculate the calories based on the distance if the activity chosen is walking, running, cycling or swimming and write the information to the activities log file
                    acti=acti_type.get()
                    dis=distance.get()

                    if acti=='' or dis=='':
                        messagebox.showerror('Invalid','All fields are required')
                        add_page.attributes('-topmost', True)
                        add_page.attributes('-topmost', False)
                    else:
                        with open('info','r') as activity:
                            allActivities=csv.reader(activity)
                            infolist=list(allActivities)
                            line_num=len(infolist)
                            for i in range(line_num-1,0,-1):
                                if len(infolist[i])>=5:
                                    if  infolist[i][0]==name:
                                        kg=int(infolist[i][3])
                                        break
                        if acti=='Walking':
                            calorie_burned=int(dis)*1*kg
                        if acti=='Running':
                            calorie_burned=int(dis)*1.5*kg
                        if acti=='Cycling':
                            calorie_burned=int(dis)*1.2*kg
                        if acti=='Swimming':
                            calorie_burned=int(dis)*1.7*kg

                        with open('activities log','a',newline='') as activity:
                            newac=csv.writer(activity)
                            newac.writerow([name,acti,round(int(calorie_burned),2),dis])
                            phy_log.insert(parent='',index='end',text='',values=(acti,'','',round(int(calorie_burned),2),dis+'km'))
                            messagebox.showinfo('Successfull','Activities created successfully')
                        f_add_page.destroy()
                        add_page.destroy()
                def save_add2():#function to calculate the calories based on the duration, intensity and activity type if the activity chosen is gym activities, training and sport activities, outdoor activities or home & daily activities and write the information to the activities log file
                    acti=acti_type.get()
                    dur_hours=duration_hour.get()
                    dur_minutes=duration_minute.get()
                    dur=str(dur_hours+dur_minutes)
                    inten=intensity.get()

                    if acti=='' or dur=='' or inten=='':
                        messagebox.showerror('Invalid','All fields are required')
                        add_page.attributes('-topmost', True)
                        add_page.attributes('-topmost', False)
                    else:
                        with open('info','r') as activity:
                            allActivities=csv.reader(activity)
                            infolist=list(allActivities)
                            line_num=len(infolist)
                            for i in range(line_num-1,0,-1):
                                if len(infolist[i])>=5:
                                    if  infolist[i][0]==name:
                                        kg=int(infolist[i][3])
                                        break
                        if dur_minutes=='':
                            dur_minutes=0
                        if dur_hours=='':
                            dur_hours=0
                        dur = str(dur_hours)+' Hours'+' '+str(dur_minutes)+' Minutes'
                        if acti=='Gym Activities':
                            met=8
                            if inten == 'Light':
                                calorie_burned=(met*3.5*(int(dur_hours)*60+int(dur_minutes))*kg)/200
                            elif inten == 'Moderate':
                                calorie_burned=(met*1.2*3.5*(int(dur_hours)*60+int(dur_minutes))*kg)/200
                            elif inten=='Vigorous':
                                calorie_burned=(met*1.5*3.5*(int(dur_hours)*60+int(dur_minutes))*kg)/200
                        elif acti=='Training and Sport Activities':
                            met=7
                            if inten == 'Light':
                                calorie_burned=(met*3.5*(int(dur_hours)*60+int(dur_minutes))*kg)/200
                            elif inten == 'Moderate':
                                calorie_burned=(met*1.2*3.5*(int(dur_hours)*60+int(dur_minutes))*kg)/200
                            elif inten=='Vigorous':
                                calorie_burned=(met*1.5*3.5*(int(dur_hours)*60+int(dur_minutes))*kg)/200
                        elif acti=='Outdoor Activities':
                            met=4
                            if inten == 'Light':
                                calorie_burned=(met*3.5*(int(dur_hours)*60+int(dur_minutes))*kg)/200
                            elif inten == 'Moderate':
                                calorie_burned=(met*1.2*3.5*(int(dur_hours)*60+int(dur_minutes))*kg)/200
                            elif inten=='Vigorous':
                                calorie_burned=(met*1.5*3.5*(int(dur_hours)*60+int(dur_minutes))*kg)/200
                        elif acti=='Home & Daily Activities':
                            met=2
                            if inten == 'Light':
                                calorie_burned=(met*3.5*(int(dur_hours)*60+int(dur_minutes))*kg)/200
                            elif inten == 'Moderate':
                                calorie_burned=(met*1.2*3.5*(int(dur_hours)*60+int(dur_minutes))*kg)/200
                            elif inten=='Vigorous':
                                calorie_burned=(met*1.5*3.5*(int(dur_hours)*60+int(dur_minutes))*kg)/200

                        with open('activities log','a',newline='') as activity:
                            newac=csv.writer(activity)
                            newac.writerow([name,acti,dur,inten,round(int(calorie_burned),2)])
                            phy_log.insert(parent='',index='end',text='',values=(acti,dur,inten,round(int(calorie_burned),2)))
                            messagebox.showinfo('Successfull','Activities created successfully')
                        f_add_page.destroy()
                        add_page.destroy()
                if acti_type.get()=='Walking' or acti_type.get()=='Running' or acti_type.get()=='Cycling' or acti_type.get()=='Swimming':
                    #if the activity type is walking, running, cycling or swimming, the user will be asked to enter the distance of the activity
                    f_add_page=tk.Toplevel()
                    f_add_page.title('Add Activity')
                    f_add_page.geometry('350x250+530+280')

                    distance_Label=ctk.CTkLabel(
                        f_add_page,
                        text='Distance:',
                        font=('Helvetica',15),
                        text_color='black',
                    )
                    distance_Label.place(x=70,y=100)

                    distance=ctk.CTkEntry(
                        f_add_page,
                        fg_color=('black','white'),
                        text_color='black',
                        width=140,
                        height=30,
                        corner_radius=10,
                        font=('Helvetica',15),
                        placeholder_text='Enter distance',
                    )
                    distance.place(x=150,y=100)

                    distance_in_km=ctk.CTkLabel(
                        f_add_page,
                        text='km',
                        font=('Helvetica',15),
                        text_color='black',
                    )
                    distance_in_km.place(x=305,y=100)
                    adda=ctk.CTkButton(
                        f_add_page,
                        text='Add',
                        width=80,
                        height=40,
                        corner_radius=10,
                        fg_color=('white','#5c547e'),
                        hover_color=('white','#37334A'),
                        font=('Helvetica',15),
                        hover=True,
                        command=save_add1,
                    )
                    adda.place(x=130,y=160)

                elif acti_type.get()=='':
                    #if the activity type is not selected, the user will be asked to select the activity type
                    messagebox.showerror('Invalid','Activity type is required')
                    add_page.attributes('-topmost', True)
                    add_page.attributes('-topmost', False)
                else:
                    #if the activity type is gym activities, training and sport activities, outdoor activities or home & daily activities, the user will be asked to enter the duration and intensity of the activity
                    f_add_page=tk.Toplevel()
                    f_add_page.title('Add Activity')
                    f_add_page.geometry('350x400+530+280')
                    duration_Label=ctk.CTkLabel(
                        f_add_page,
                        text='Duration:',
                        font=('Helvetica',15),
                        text_color='black',
                    )
                    duration_Label.place(x=70,y=100)

                    minute_list = [5,10,15,20,25,30,35,40,45,50,55,60]
                    hour_list=[1,2,3,4,5,6,7,8,9,10]

                    duration_hour=ttk.Combobox(f_add_page,values=hour_list,width=10)
                    duration_hour.place(x=150,y=100) 

                    dur_hour=ctk.CTkLabel(
                        f_add_page,
                        text='Hour(s)',
                        font=('Helvetica',15),
                        text_color='black',
                    )
                    dur_hour.place(x=245,y=100)

                    duration_minute=ttk.Combobox(f_add_page,values=minute_list,width=10)
                    duration_minute.place(x=150,y=130) 

                    dur_min=ctk.CTkLabel(
                        f_add_page,
                        text='Minute(s)',
                        font=('Helvetica',15),
                        text_color='black',
                    )
                    dur_min.place(x=245,y=130)

                    intensity_list = ['Light','Moderate','Vigorous']

                    intensity_Label=ctk.CTkLabel(
                        f_add_page,
                        text='Intensity Level:',
                        font=('Helvetica',15),
                        text_color='black',
                    )
                    intensity_Label.place(x=50,y=180)

                    intensity=ttk.Combobox(f_add_page,values=intensity_list)
                    intensity.place(x=150,y=180)
                    adda=ctk.CTkButton(
                        f_add_page,
                        text='Add',
                        width=80,
                        height=40,
                        corner_radius=10,
                        fg_color=('white','#5c547e'),
                        hover_color=('white','#37334A'),
                        font=('Helvetica',15),
                        hover=True,
                        command=save_add2,
                    )
                    adda.place(x=130,y=290)
                    
            add=ctk.CTkButton(
                add_page,
                text='Confirm',
                width=80,
                height=40,
                corner_radius=10,
                fg_color=('white','#5c547e'),
                hover_color=('white','#37334A'),
                font=('Helvetica',15),
                hover=True,
                command=further_add,
            )
            add.place(x=130,y=120)
        #a button to trigger the function add_acti to add activities to the activities log
        add_button=ctk.CTkButton(
            page_1,
            text='Add Activity',
            width=80,
            height=40,
            corner_radius=10,
            fg_color=('white','#5c547e'),
            hover_color=('white','#37334A'),
            font=('Helvetica',15),
            hover=True,
            command=add_acti,
        )
        add_button.place(x=1150,y=150)
        #a button to trigger the function deleteAll_act to delete all the activities in the activities log
        delete_act_button=ctk.CTkButton(
            page_1,
            text='Delete All Activities',
            width=80,
            height=40,
            corner_radius=10,
            fg_color=('white','#5c547e'),
            hover_color=('white','#37334A'),
            font=('Helvetica',15),
            hover=True,
            command=deleteAll_act,
        )
        delete_act_button.place(x=1150,y=200)
        #A label to tell the user that they has logged in as 'name' variable
        logged_in=Label(main_frame,text='Logged in as: '+name,fg='#5c547e',bg='#f0f0f0',font=('Helvetica',15))
        logged_in.place(x=640,y=730)

    def intake(): #function to display the nutrition and calories intake page and allow the user to calculate the daily calorie needs and activity level 
        def go_back2():#function once triggered will forget the current page and display the home page
            page_2.pack_forget()
        global page_2
        global tdee
        tdee=0 #a variable to store daily calorie needs
        #create a frame for page 2 and add the titles of the page
        page_2=tk.Frame(main_frame,width=1500,height=800,bg='#f0f0f0')
        title_page_2=Label(page_2,text='Nutritions And Calories Intake',fg='#5c547e',bg='#f0f0f0',font=('Helvetica',35,'bold'))
        title_page_2.place(x=415,y=70)
        h2_page_2=Label(page_2,text='Daily Calories and Nutrition Intake:',fg='#5c547e',bg='#f0f0f0',font=('Helvetica',20,))
        h2_page_2.place(x=530,y=130)
        h2_page_2_2=Label(page_2,text='Daily Calorie Needs:',fg='#5c547e',bg='#f0f0f0',font=('Helvetica',20,))
        h2_page_2_2.place(x=610,y=450)
        h3_page_2=Label(page_2,text='Activity Level:',fg='black',bg='#f0f0f0',font=('Helvetica',15,))
        h3_page_2.place(x=330,y=500)
        page_2.pack(fill=tk.BOTH,expand=True)
        #radio button for the user to select the activity level
        activity_var=ctk.StringVar(value='Inactive')
        inactive=ctk.CTkRadioButton(page_2,text="Inactive",fg_color='black',bg_color='#f0f0f0',text_color='black',value='Inactive',variable=activity_var)
        inactive.place(x=240,y=550)
        somewhat_active=ctk.CTkRadioButton(page_2,text="Somewhat Active",fg_color='black',bg_color='#f0f0f0',text_color='black',value='Somewhat Active',variable=activity_var)
        somewhat_active.place(x=400,y=550)
        active=ctk.CTkRadioButton(page_2,text="Active",fg_color='black',bg_color='#f0f0f0',text_color='black',value='Active',variable=activity_var)
        active.place(x=240,y=600)
        very_active=ctk.CTkRadioButton(page_2,text="Very Active",fg_color='black',bg_color='#f0f0f0',text_color='black',value='Very Active',variable=activity_var)
        very_active.place(x=400,y=600)
        #function to calculate the daily calorie needs based on the user's personal information and activity level
        def calculate():
            with open('info','r') as activity: #read the personal information file to get the user's gender to calculate daily calorie needs
                allActivities=csv.reader(activity)
                infolist=list(allActivities)
                line_num=len(infolist)
                for i in range(line_num-1,0,-1):
                    if len(infolist[i])>=5:
                        if name in infolist[i]:
                            if infolist[i][4]=='Male':
                                bmr=10*int(infolist[i][3])+6.25*int(infolist[i][2])-5*int(infolist[i][1])+5
                                break
                            elif infolist[i][4]=='Female':
                                bmr=10*int(infolist[i][3])+6.25*int(infolist[i][2])-5*int(infolist[i][1])-161
                                break
                #calculate the daily calorie needs based on the user's activity level and display the daily calorie needs
                if activity_var.get()=='Inactive':
                    tdee=bmr*1.2
                elif activity_var.get()=='Somewhat Active':
                    tdee=bmr*1.375
                elif activity_var.get()=='Active':
                    tdee=bmr*1.55
                elif activity_var.get()=='Very Active':
                    tdee=bmr*1.725
                tdee_label=ctk.CTkLabel(
                    page_2,
                    text=str(round(tdee,2))+' Calories',
                    font=('Helvetica',20),
                    text_color='black',
                )
                tdee_label.place(x=870,y=563)
                explain_label=ctk.CTkLabel(
                    page_2,
                    text='(This is calculated based on your age, height, weight and activity level)',
                    font=('Helvetica',15),
                    text_color='black',
                )
                explain_label.place(x=870,y=603)
                with open('calorie need and acti level','a',newline='') as activity:
                    writecalo=csv.writer(activity)
                    writecalo.writerow([name,round(tdee,2),activity_var.get()])
        def fill_act_calo(): #function to read the file and the tick the radio button based on the last activity level selected by the user
            global tdee
            with open('calorie need and acti level','r') as activity:
                allActivities=csv.reader(activity)
                calolist=list(allActivities)
                line_num=len(calolist)
                for i in range(line_num-1,0,-1):
                    if len(calolist[i])>=3:
                        if calolist[i][0]==name:
                            tdee=float(calolist[i][1])
                            activity_var.set(calolist[i][2])
                            break
            inactive=ctk.CTkRadioButton(page_2,text="Inactive",fg_color='black',bg_color='#f0f0f0',text_color='black',value='Inactive',variable=activity_var)
            inactive.place(x=240,y=550)
            somewhat_active=ctk.CTkRadioButton(page_2,text="Somewhat Active",fg_color='black',bg_color='#f0f0f0',text_color='black',value='Somewhat Active',variable=activity_var)
            somewhat_active.place(x=400,y=550)
            active=ctk.CTkRadioButton(page_2,text="Active",fg_color='black',bg_color='#f0f0f0',text_color='black',value='Active',variable=activity_var)
            active.place(x=240,y=600)
            very_active=ctk.CTkRadioButton(page_2,text="Very Active",fg_color='black',bg_color='#f0f0f0',text_color='black',value='Very Active',variable=activity_var)
            very_active.place(x=400,y=600)
            tdee_label=ctk.CTkLabel(
                    page_2,
                    text=str(round(tdee,2))+' Calories',
                    font=('Helvetica',20),
                    text_color='black',
                )
            tdee_label.place(x=870,y=563)
            explain_label=ctk.CTkLabel(
                page_2,
                text='(This is calculated based on your age, height, weight and activity level)',
                font=('Helvetica',15),
                text_color='black',
            )
            explain_label.place(x=870,y=603)

        fill_act_calo() #call the fill_act_calo function to display the daily calorie needs and tick the radio button based on the last activity level selected by the user
        calculate() #call the calculate function to calculate the daily calorie needs based on the user's personal information and activity level
        calculate_button=ctk.CTkButton(
            page_2,
            text='Calculate',
            width=100,
            height=40,
            corner_radius=10,
            fg_color=('white','#5c547e'),
            hover_color=('white','#37334A'),
            font=('Helvetica',15),
            hover=True,
            command=calculate,
        )
        calculate_button.place(x=700,y=560)
        
        back_button=ctk.CTkButton(
            page_2,
            text='<-- Back',
            width=100,
            height=40,
            corner_radius=10,
            fg_color=('white','#5c547e'),
            hover_color=('white','#37334A'),
            font=('Helvetica',15),
            hover=True,
            command=go_back2,
        )
        back_button.place(x=30,y=20)
        #a list of food that the user can choose from to add to the food log
        food_list=[
            'Beef 1 Portion (170g)',
            'Boiled Rice (120g)',
            'Fried Rice (150g)',
            'Sandwich',
            'Scrambled Eggs (100g)',
            'Boiled Eggs',
            'Chicken 1/2 (460g)',
            'Lamb 1 Portion (110g)',
            'Pork 1 Portion (200g)',
            'Fish 1 Palm (100g)',
            'Fish and Chips 1 Portion',
            'Hamburger 1 Portion',
            'Pizza 1 Slice',
            'English Breakfast'
        ]
        calorie_list=[265,156,188,250,148,77,764,128,557,116,1000,295,285,900] #a list of calories for each food in the food list
        macronutrient_list=[['Protein:',26,'g','Carbohydrates:',0,'g','Fat:', 17,'g'], #a list of macronutrients for each food in the food list
                            ['Protein:',3,'g','Carbohydrates:',35,'g','Fat:', 0,'g'],
                            ['Protein:',4,'g','Carbohydrates:',35,'g','Fat:', 0,'g'],
                            ['Protein:',12,'g','Carbohydrates:',35,'g','Fat:', 0,'g'],
                            ['Protein:',13,'g','Carbohydrates:',1,'g','Fat:', 11,'g'],
                            ['Protein:',6,'g','Carbohydrates:',1,'g','Fat:', 5,'g'],
                            ['Protein:',92,'g','Carbohydrates:',0,'g','Fat:', 6,'g'],
                            ['Protein:',22,'g','Carbohydrates:',0,'g','Fat:', 11,'g'],
                            ['Protein:',38,'g','Carbohydrates:',0,'g','Fat:', 22,'g'],
                            ['Protein:',20,'g','Carbohydrates:',0,'g','Fat:', 5,'g'],
                            ['Protein:',10,'g','Carbohydrates:',35,'g','Fat:', 0,'g'],
                            ['Protein:',13,'g','Carbohydrates:',35,'g','Fat:', 0,'g'],
                            ['Protein:',12,'g','Carbohydrates:',35,'g','Fat:', 0,'g'],
                            ['Protein:',13,'g','Carbohydrates:',35,'g','Fat:', 0,'g']]
        food=Listbox(page_2,selectmode='single',width=30,height=10) #a listbox to display the food list
        food.place(x=150,y=185)
        for i in food_list:#add the food list to the listbox
            food.insert(END,i)
        def treeView():#function to create the food log and display the food that the user has added by reading the food log file
            global total
            total=ttk.Treeview(page_2,height=1)
            total['columns']=('No','Total','Total Calorie','Total Macronutrients')

            total.column('#0',width=0,stretch=tk.NO)
            total.column('No',anchor=tk.CENTER,width=100)
            total.column('Total',anchor=tk.CENTER,width=200)
            total.column('Total Calorie',anchor=tk.CENTER,width=100)
            total.column('Total Macronutrients',anchor=tk.CENTER,width=300)

            total.heading('#0',text='',anchor=tk.W)
            total.heading('No',text='',anchor=tk.CENTER)
            total.heading('Total',text='',anchor=tk.CENTER)
            total.heading('Total Calorie',text='',anchor=tk.CENTER)
            total.heading('Total Macronutrients',text='',anchor=tk.CENTER)
            total.place(x=510,y=387)
            global food_log
            food_log=ttk.Treeview(page_2,height=10)
            food_log['columns']=('No','Food','Calorie','Macronutrients')
            food_log.column('#0',width=0,stretch=tk.NO)
            food_log.column('No',anchor=tk.CENTER,width=100)
            food_log.column('Food',anchor=tk.CENTER,width=200)
            food_log.column('Calorie',anchor=tk.CENTER,width=100)
            food_log.column('Macronutrients',anchor=tk.CENTER,width=300)

            food_log.heading('#0',text='',anchor=tk.W)
            food_log.heading('No',text='No',anchor=tk.CENTER)
            food_log.heading('Food',text='Food',anchor=tk.CENTER)
            food_log.heading('Calorie',text='Calorie',anchor=tk.CENTER)
            food_log.heading('Macronutrients',text='Macronutrients',anchor=tk.CENTER)

            global total_calo
            global total_protein
            global total_carbohydrates
            global total_fat
            total_calo=0    
            total_protein=0
            total_carbohydrates=0
            total_fat=0
            i=1
            #read the food log file and calculate the total calories and macronutrients of the food that the user has added to the food log
            with open('calorie and food','r') as activity:
                allActivities=csv.reader(activity)
                flist=list(allActivities)
                for line in flist[1:]:
                    if len(line)>=4 and line[0]==name:      
                        macro=eval(line[3])
                        food_log.insert(parent='',index='end',text='',values=(i,line[1],line[2],macro[0]+' '+str(macro[1])+macro[2]+'; '+macro[3]+' '+str(macro[4])+macro[5]+'; '+macro[6]+' '+str(macro[7])+macro[8]))
                        total_calo+=int(line[2])
                        total_protein+=macro[1]
                        total_carbohydrates+=macro[4]
                        total_fat+=macro[7]
                        i+=1
                        total.insert(parent='',index='0',text='',values=('Total','',str(total_calo),'Protein: '+str(total_protein)+'g; Carbohydrates: '+str(total_carbohydrates)+'g; Fat: '+str(total_fat)+'g'))
                total_calo=total_calo
                total_protein=total_protein
                total_carbohydrates=total_carbohydrates
                total_fat=total_fat
                #write the total calories and macronutrients of the food that the user has added to the food log to the total calorie and macronutrient file
                with open('total calorie and total macronutrient','a',newline='') as activity:
                    writecalo=csv.writer(activity)
                    writecalo.writerow([name,total_calo,total_protein,total_carbohydrates,total_fat])
            food_log.place(x=510,y=185)
        treeView()#call the treeView function to display the food log when the user uses the food log function
        #function to add the selected food to the food log and calculate the total calories and macronutrients of the food that the user has added
        def select(total_calo=total_calo,total_protein=total_protein,total_carbohydrates=total_carbohydrates,total_fat=total_fat):
            with open('calorie and food','a',newline='') as activity:
                newac=csv.writer(activity)
                if food.get(ANCHOR)=='':
                    messagebox.showerror('Invalid','Please select a food')
                elif food.get(ANCHOR)in food_list:
                    index=food_list.index(food.get(ANCHOR))
                    total_calo+=calorie_list[index]
                    total_protein+=macronutrient_list[index][1]
                    total_carbohydrates+=macronutrient_list[index][4]
                    total_fat+=macronutrient_list[index][7]
                    newac.writerow([name,food_list[index],calorie_list[index],macronutrient_list[index]])
                    with open('total calorie and total macronutrient','a',newline='') as activity:
                        writecalo=csv.writer(activity)
                        writecalo.writerow([name,total_calo,total_protein,total_carbohydrates,total_fat])
            treeView() #call the treeView function to update the list

        def deleteAll(): #function to delete all the food in the food log and clear the food log file
            with open('calorie and food', 'r') as booking:
                allActivities = csv.reader(booking)
                activities_list = list(allActivities)
                # Write back only the foods that do not belong to the current user
            with open('calorie and food', 'w', newline='') as booking:
                header = csv.writer(booking)
                header.writerow(['Username','Food','Calories','Macronutrients'])
                for line in activities_list[1:]:  # Skip the header row
                    if len(line) >= 4 and line[0] != name:  # Keep foods of other users
                        header.writerow(line)
            treeView() #call the treeView function to update the list
        def deleteSelect(): #function to delete the selected food in the food log and clear the overwrite every line except for the one the user wants to delete
            delete_item=food_log.focus()
            food_dict=food_log.item(delete_item)
            selected_line=food_dict['values'][0]
            
            with open('calorie and food','r') as booking:
                fl=csv.reader(booking)
                food_info=list(fl)
                i=0
                for line in food_info[1:]:
                    if len(line)>=4 and line[0]==name:
                        i+=1
                    if i==int(selected_line): 
                        line_to_delete=line
                        break
                print(line_to_delete)
            with open('calorie and food', 'w', newline='') as booking:
                header=csv.writer(booking)
                header.writerow(['Username','Food','Calories','Macronutrients'])
                j=0
                for line in food_info[1:]:  # Skip the header row
                    if len(line) >= 4:
                        if line[0]==name:
                            j+=1 
                        if j==selected_line and line==line_to_delete:
                            pass
                        else:
                            header.writerow(line)
            treeView() #call the treeView function to update the list
        #buttons to trigger the select, deleteAll and deleteSelect functions
        select_button=ctk.CTkButton(
            page_2,
            text='Select',
            width=100,
            height=40,
            corner_radius=10,
            fg_color=('white','#5c547e'),
            hover_color=('white','#37334A'),
            font=('Helvetica',15),
            hover=True,
            command=select,
        )
        select_button.place(x=365,y=185)

        delete_all_button=ctk.CTkButton(
            page_2,
            text='Delete All Food',
            width=100,
            height=40,
            corner_radius=10,
            fg_color=('white','#5c547e'),
            hover_color=('white','#37334A'),
            font=('Helvetica',15),
            hover=True,
            command=deleteAll,
        )
        delete_all_button.place(x=1260,y=185)

        delete_one_button=ctk.CTkButton(
            page_2,
            text='Delete Selected Food',
            width=100,
            height=40,
            corner_radius=10,
            fg_color=('white','#5c547e'),
            hover_color=('white','#37334A'),
            font=('Helvetica',15),
            hover=True,
            command=deleteSelect,
        )
        delete_one_button.place(x=1260,y=245)

        logged_in=Label(main_frame,text='Logged in as: '+name,fg='#5c547e',bg='#f0f0f0',font=('Helvetica',15))
        logged_in.place(x=640,y=730)

    def change_personal_info(): #function to display the change personal information page and allow the user to change their personal information
        def fill_info(): #function to read the personal information file and fill the entry boxes with the user's personal information
            age=year.get()
            hei=height.get()
            wei=weight.get()
            if age=='' and hei=='' and wei=='': #if the entry boxes are empty (which is also the case when the user access the page) the function will read the personal information file and fill the entry boxes with the user's personal information
                with open('info','r') as activity:
                    allActivities=csv.reader(activity)
                    calolist=list(allActivities)
                    line_num=len(calolist)
                    for i in range(line_num-1,0,-1):
                        if len(calolist[i])>=5: #set condition len >=5 first to avoid index out of range error
                            if calolist[i][0]==name: #this condition will make the info added to the entry boxes to be the last info added by the user
                                year.insert(0,calolist[i][1])
                                height.insert(0,calolist[i][2])
                                weight.insert(0,calolist[i][3])
                                global gender_var2
                                gender_var2=ctk.StringVar(value=calolist[i][4])
                                female=ctk.CTkRadioButton(page_4,text="Female",fg_color='black',bg_color='#f0f0f0',text_color='black',value='Female',variable=gender_var2)
                                female.place(x=680,y=350)
                                male=ctk.CTkRadioButton(page_4,text="Male",fg_color='black',bg_color='#f0f0f0',text_color='black',value='Male',variable=gender_var2)
                                male.place(x=780,y=350)                                
                                break
        def go_back4(): #function once triggered will forget the current page and display the home page
            page_4.pack_forget()
        '''create a frame for page 4 and add the titles of the page
        create entry boxes for the user to enter their age, height and weight
        create radio buttons for the user to select their 950-1062'''
        page_4=tk.Frame(main_frame,width=1500,height=800,bg='#f0f0f0')
        page_4.pack(fill=tk.BOTH,expand=True)
        back_button=ctk.CTkButton(
            page_4,
            text='<-- Back',
            width=100,
            height=40,
            corner_radius=10,
            fg_color=('white','#5c547e'),
            hover_color=('white','#37334A'),
            font=('Helvetica',15),
            hover=True,
            command=go_back4,
        )
        back_button.place(x=30,y=20)

        year_Label=ctk.CTkLabel(
            page_4,
            text='Age:',
            font=('Helvetica',15),
            text_color='#5c547e',
        )
        year_Label.place(x=640,y=200)

        age_in_year=ctk.CTkLabel(
            page_4,
            text='Years',
            font=('Helvetica',15),
            text_color='black',
        )
        age_in_year.place(x=830,y=200)

        year=ctk.CTkEntry(
            page_4,
            fg_color=('black','white'),
            text_color='black',
            width=140,
            height=30,
            corner_radius=10,
            font=('Helvetica',15),
            placeholder_text='Enter your age'
        )
        year.place(x=680,y=200) 

        height_Label=ctk.CTkLabel(
            page_4,
            text='Height:',
            font=('Helvetica',15),
            text_color='#5c547e',
        )
        height_Label.place(x=620,y=250)

        height=ctk.CTkEntry(
            page_4,
            fg_color=('black','white'),
            text_color='black',
            width=140,
            height=30,
            corner_radius=10,
            font=('Helvetica',15),
            placeholder_text='Enter your height',
        )
        height.place(x=680,y=250)

        height_in_cm=ctk.CTkLabel(
            page_4,
            text='cm',
            font=('Helvetica',15),
            text_color='black',
        )
        height_in_cm.place(x=830,y=250)

        weight_Label=ctk.CTkLabel(
            page_4,
            text='Weight:',
            font=('Helvetica',15),
            text_color='#5c547e',
        )
        weight_Label.place(x=620,y=300)

        weight_in_cm=ctk.CTkLabel(
            page_4,
            text='kg',
            font=('Helvetica',15),
            text_color='black',
        )
        weight_in_cm.place(x=830,y=300)

        weight=ctk.CTkEntry(
            page_4,
            fg_color=('black','white'),
            text_color='black',
            width=140,
            height=30,
            corner_radius=10,
            font=('Helvetica',15),
            placeholder_text='Enter your weight',
        )
        weight.place(x=680,y=300)
        
        gender_var=ctk.StringVar(value='Female')  
        gender_Label=ctk.CTkLabel(
            page_4,
            text='Gender:',
            font=('Helvetica',15),
            text_color='#5c547e',
        )
        gender_Label.place(x=620,y=350)

        female=ctk.CTkRadioButton(page_4,text="Female",fg_color='black',bg_color='#f0f0f0',text_color='black',value='Female',variable=gender_var)
        female.place(x=680,y=350)
        male=ctk.CTkRadioButton(page_4,text="Male",fg_color='black',bg_color='#f0f0f0',text_color='black',value='Male',variable=gender_var)
        male.place(x=780,y=350)

        fill_info() #call the function fill_info to fill the entry boxes with the user's personal information once all entry boxes has been created       

        def change(): #function to change the user's personal information
            age=year.get()
            hei=height.get()
            wei=weight.get()
            #if the user does not enter their age, height and weight, the user will be asked to enter their age, height and weight
            if age=='' and hei!='' and wei!='':
                messagebox.showerror('Invalid','Age is required')
            elif hei=='' and age!='' and wei!='':
                messagebox.showerror('Invalid','Height is required')
            elif wei=='' and age!='' and hei!='':
                messagebox.showerror('Invalid','Weight is required')
            elif age=='' and hei=='' and wei!='':
                messagebox.showerror('Invalid','Age and Height are required')
            elif age=='' and wei=='' and hei!='':
                messagebox.showerror('Invalid','Age and Weight are required')
            elif hei=='' and wei=='' and age!='':
                messagebox.showerror('Invalid','Height and Weight are required')
            elif age=='' and hei=='' and wei=='':
                messagebox.showerror('Invalid','Age, Height and Weight are required')
            else:#if the user enters their age, height and weight, the user's personal information will be checked again to see if inputs are valid
                if age.isdigit()==False or int(age)<=0:
                    messagebox.showerror('Invalid','Age, Height, Weight must all be a numbers and greater than 0')
                    year.insert(0,'')
                elif hei.isdigit()==False or int(hei)<=0:
                    messagebox.showerror('Invalid','Age, Height, Weight must all be a numbers and greater than 0')
                    height.insert(0,'')
                elif wei.isdigit()==False or int(wei)<=0:
                    messagebox.showerror('Invalid','Age, Height, Weight must all be a numbers and greater than 0')
                    weight.insert(0,'')
                elif age.isdigit()==True and hei.isdigit()==True and wei.isdigit()==True and int(age)> 0 and int(hei)>0 and int(wei)>0:
                    age=int(year.get())
                    hei=int(height.get())
                    wei=int(weight.get())
                    #once the user's personal information is valid, the user's personal information will be changed and the user will be informed that the information has been changed successfully
                    with open('info','a',newline='') as activity:
                        writecalo=csv.writer(activity)
                        with open('info','r') as activity:
                            allActivities=csv.reader(activity)
                            infolist=list(allActivities)
                            if [name,str(age),str(hei),str(wei),gender_var2.get()] not in infolist:
                                writecalo.writerow([name,age,hei,wei,gender_var2.get()])
                            elif [name,str(age),str(hei),str(wei),gender_var.get()] in infolist and [name,str(age),str(hei),str(wei),gender_var.get()] != infolist[-1]:
                                writecalo.writerow([name,age,hei,wei,gender_var2.get()])
                    messagebox.showinfo('Successfull','Information changed successfully')
        #a button to trigger the function change to change the user's personal information
        change_button=ctk.CTkButton(
            page_4,
            text='Change',
            width=100,
            height=40,
            corner_radius=10,
            fg_color=('white','#5c547e'),
            hover_color=('white','#37334A'),
            font=('Helvetica',15),
            hover=True,
            command=change,
        )
        change_button.place(x=690,y=400)
        #a label to tell the user that they has logged in as 'name' variable
        title_page_4=Label(page_4,text='Personal Information',fg='#5c547e',bg='#f0f0f0',font=('Helvetica',35,'bold'))
        title_page_4.place(x=510,y=70)
        logged_in=Label(main_frame,text='Logged in as: '+name,fg='#5c547e',bg='#f0f0f0',font=('Helvetica',15))
        logged_in.place(x=640,y=730)

    def progress(): #function to display the fitness goals progress page and allow the user to see their fitness goals progress
        def go_back3(): #function once triggered will forget the current page and display the home page
            page_3.pack_forget()
        global page_3
        #create a frame for page 3 and add the titles of the page
        page_3=tk.Frame(main_frame,width=1500,height=800,bg='#f0f0f0')
        title_page_3=Label(page_3,text='Fitness Goals Progress',fg='#5c547e',bg='#f0f0f0',font=('Helvetica',35,'bold'))
        title_page_3.place(x=480,y=70)
        page_3.pack(fill=tk.BOTH,expand=True)
        #a back button to trigger the function go_back3 to forget the current page and display the home page
        back_button=ctk.CTkButton(
            page_3,
            text='<-- Back',
            width=100,
            height=40,
            corner_radius=10,
            fg_color=('white','#5c547e'),
            hover_color=('white','#37334A'),
            font=('Helvetica',15),
            hover=True,
            command=go_back3,
        )
        back_button.place(x=30,y=20)
        #a tabview to display the user's fitness goals progress
        goal_list=ctk.CTkTabview(page_3,fg_color='white',width=800,height=450)
        goal_list.place(x=350,y=175)
        def fill_goal(): #function to read the fitness goals file and fill the tabview with the user's fitness goals progress
            cur_run=0
            cur_walk=0
            cur_cycle=0
            cur_swim=0
            #read the activities log to find the current progress of the user's fitness goals
            with open('activities log','r') as activity:
                allActivities=csv.reader(activity)
                calolist=list(allActivities)
                line_num=len(calolist)
                for i in range(line_num-1,0,-1):
                    if len(calolist[i])==4:
                        if calolist[i][0]==name:
                            if calolist[i][1]=='Walking':
                                cur_walk+=float(calolist[i][3])
                            elif calolist[i][1]=='Running':
                                cur_run+=float(calolist[i][3])
                            elif calolist[i][1]=='Cycling':
                                cur_cycle+=float(calolist[i][3])
                            elif calolist[i][1]=='Swimming':
                                cur_swim+=float(calolist[i][3])
            #read the fitness goals file to find the user's fitness goals
            with open('goal','r') as activity:
                allActivities=csv.reader(activity)
                calolist=list(allActivities)
                line_num=len(calolist)
                for i in range(0,line_num):
                    if len(calolist[i])>=3:
                        if calolist[i][0]==name:
                            #if the user has a fitness goal, the tabview will be filled with the user's fitness goals progress
                            #the progress bar will show the user's progress towards their fitness goals
                            #if the user has achieved their fitness goals, the progress bar will show 100% and the current progress label will show 'Goal Achieved'
                            #there are four different tabs for the user's fitness goals progress: Walking Goal, Running Goal, Cycling Goal and Swimming Goal
                            if calolist[i][1]=='Walking':
                                goal_walk=float(calolist[i][2])
                                run_tab=goal_list.add('Walking Goal')
                                progress_bar=ctk.CTkProgressBar(run_tab,orientation=HORIZONTAL,width=500,height=50,fg_color='#f0f0f0',progress_color='#5c547e')
                                current_distance_label=ctk.CTkLabel(
                                    run_tab,
                                    text='Current Distance: '+str(cur_walk)+' km',
                                    font=('Helvetica',20),
                                    text_color='black',
                                )
                                current_distance_label.place(x=200,y=50)
                                distance_Label=ctk.CTkLabel(
                                    run_tab,
                                    text='Goal Distance: '+str(goal_walk)+' km',
                                    font=('Helvetica',20),
                                    text_color='black',
                                )
                                distance_Label.place(x=200,y=100)
                                current_progress=ctk.CTkLabel(
                                    run_tab,
                                    text='Current Progress: '+str(round(cur_walk/goal_walk*100,2))+'%',
                                    font=('Helvetica',20),
                                    text_color='black',
                                )
                                current_progress.place(x=200,y=150)
                                progress_bar.set(cur_walk/goal_walk)
                                progress_bar.place(x=140,y=240)
                                if cur_walk>=goal_walk:
                                    progress_bar.set(1)
                                    current_progress.configure(text='Goal Achieved')
                            elif calolist[i][1]=='Running':
                                goal_run=float(calolist[i][2])
                                run_tab=goal_list.add('Running Goal')
                                progress_bar=ctk.CTkProgressBar(run_tab,orientation=HORIZONTAL,width=500,height=50,fg_color='#f0f0f0',progress_color='#5c547e')
                                current_distance_label=ctk.CTkLabel(
                                    run_tab,
                                    text='Current Distance: '+str(cur_run)+' km',
                                    font=('Helvetica',20),
                                    text_color='black',
                                )
                                current_distance_label.place(x=200,y=50)
                                distance_Label=ctk.CTkLabel(
                                    run_tab,
                                    text='Goal Distance: '+str(goal_run)+' km',
                                    font=('Helvetica',20),
                                    text_color='black',
                                )
                                distance_Label.place(x=200,y=100)
                                current_progress=ctk.CTkLabel(
                                    run_tab,
                                    text='Current Progress: '+str(round(cur_run/goal_run*100,2))+'%',
                                    font=('Helvetica',20),
                                    text_color='black',
                                )
                                current_progress.place(x=200,y=150)
                                progress_bar.set(cur_run/goal_run)
                                progress_bar.place(x=140,y=240)
                                if cur_run>=goal_run:
                                    progress_bar.set(1)
                                    current_progress.configure(text='Goal Achieved')
                            elif calolist[i][1]=='Cycling':
                                goal_cycle=float(calolist[i][2])
                                run_tab=goal_list.add('Cycling Goal')
                                progress_bar=ctk.CTkProgressBar(run_tab,orientation=HORIZONTAL,width=500,height=50,fg_color='#f0f0f0',progress_color='#5c547e')
                                current_distance_label=ctk.CTkLabel(
                                    run_tab,
                                    text='Current Distance: '+str(cur_cycle)+' km',
                                    font=('Helvetica',20),
                                    text_color='black',
                                )
                                current_distance_label.place(x=200,y=50)
                                distance_Label=ctk.CTkLabel(
                                    run_tab,
                                    text='Goal Distance: '+str(goal_cycle)+' km',
                                    font=('Helvetica',20),
                                    text_color='black',
                                )
                                distance_Label.place(x=200,y=100)
                                current_progress=ctk.CTkLabel(
                                    run_tab,
                                    text='Current Progress: '+str(round(cur_cycle/goal_cycle*100,2))+'%',
                                    font=('Helvetica',20),
                                    text_color='black',
                                )
                                current_progress.place(x=200,y=150)
                                progress_bar.set(cur_cycle/goal_cycle)
                                progress_bar.place(x=140,y=240)
                                if cur_cycle>=goal_cycle:
                                    progress_bar.set(1)
                                    current_progress.configure(text='Goal Achieved')
                            elif calolist[i][1]=='Swimming':
                                goal_swim=float(calolist[i][2])
                                run_tab=goal_list.add('Swimming Goal')
                                progress_bar=ctk.CTkProgressBar(run_tab,orientation=HORIZONTAL,width=500,height=50,fg_color='#f0f0f0',progress_color='#5c547e')
                                current_distance_label=ctk.CTkLabel(
                                    run_tab,
                                    text='Current Distance: '+str(cur_swim)+' km',
                                    font=('Helvetica',20),
                                    text_color='black',
                                )
                                current_distance_label.place(x=200,y=50)
                                distance_Label=ctk.CTkLabel(
                                    run_tab,
                                    text='Goal Distance: '+str(goal_swim)+' km',
                                    font=('Helvetica',20),
                                    text_color='black',
                                )
                                distance_Label.place(x=200,y=100)
                                current_progress=ctk.CTkLabel(
                                    run_tab,
                                    text='Current Progress: '+str(round(cur_swim/goal_swim*100,2))+'%',
                                    font=('Helvetica',20),
                                    text_color='black',
                                )
                                current_progress.place(x=200,y=150)
                                progress_bar.set(cur_swim/goal_swim)
                                progress_bar.place(x=140,y=240)
                                if cur_swim>=goal_swim:
                                    progress_bar.set(1)
                                    current_progress.configure(text='Goal Achieved')
        fill_goal() #call the function fill_goal to fill the tabview with the user's fitness goals progress once all tabs have been created
        def delete_goal():#function to delete the user's fitness goals
            #read the 'goal file and overwrite every single line except for the one that the user wants to delete
            with open('goal','r') as activity:
                allActivities=csv.reader(activity)
                calolist=list(allActivities)
                line_num=len(calolist)
                with open('goal','w',newline='') as activity:
                    allActivities=csv.writer(activity)
                    allActivities.writerow(['Username','Activity Type','Target Distance'])
                    for i in range(0,line_num):
                        if len(calolist[i])>=3:
                            if calolist[i][0]==name:
                                if calolist[i][1] not in goal_list.get():
                                    allActivities.writerow(calolist[i])
            goal_list.delete(goal_list.get())
        
        def add_goal(): #function to add the user's fitness goals
            def goal_add(): #function for the user to fill in the information for the goal they want to add
                goal_type=goal.get()
                add_page.destroy()
                if goal_type=='Running-Walking-Cycling-Swimming Distance':
                    def save_goal():#function to save the user's fitness goals and write the user's fitness goals to the goal file and display the user's fitness goals progress
                        activity_type=acti_type.get()
                        distance_=distance.get()
                        #iterate through the goal file to check if the user already has a goal for the activity type they want to add
                        with open('goal','r') as activity:
                            allActivities=csv.reader(activity)
                            calolist=list(allActivities)
                            line_num=len(calolist)
                            for i in range(line_num-1,0,-1):
                                if len(calolist[i])>=3:
                                    if calolist[i][0]==name:
                                        if calolist[i][1]==activity_type:
                                            messagebox.showerror('Invalid','You already have a goal for this activity type')
                                            return
                        if distance_=='': #show an error message if the user does not enter the distance
                            messagebox.showerror('Invalid','Please enter distance')
                        elif distance_.isdigit()==False: #show an error message if the user enters a non-numeric value for the distance
                            messagebox.showerror('Invalid','Distance must be a number')
                            distance.insert(0,'')
                        elif distance_.isdigit()==True: #write the user's fitness goals to the goal file and display the user's fitness goals progress
                            with open('goal','a',newline='') as activity:
                                writecalo=csv.writer(activity)
                                writecalo.writerow([name,activity_type,distance_])
                            messagebox.showinfo('Successfull','Goal added successfully')
                            current_distance=0
                            goal_page.destroy()
                            #iterate through the activities log file to find the user's current progress for the activity type they want to add
                            with open('activities log','r') as activity:
                                allActivities=csv.reader(activity)
                                calolist=list(allActivities)
                                line_num=len(calolist)
                                for i in range(line_num-1,0,-1):
                                    if len(calolist[i])==4:
                                        if calolist[i][0]==name:
                                            if calolist[i][1]==activity_type:
                                                current_distance+=float(calolist[i][3])
                            #iterate through the goal file to find the user's fitness goals
                            with open('goal','r') as activity:
                                allActivities=csv.reader(activity)
                                calolist=list(allActivities)
                                line_num=len(calolist)
                                for i in range(line_num-1,0,-1):
                                    if len(calolist[i])>=3:
                                        if calolist[i][0]==name:
                                            if calolist[i][1]==activity_type:
                                                distance_=calolist[i][2]
                                                goal_tab=goal_list.add(activity_type+ 'Goal')
                                                progress_bar=ctk.CTkProgressBar(goal_tab,orientation=HORIZONTAL,width=500,height=50,fg_color='#f0f0f0',progress_color='#5c547e')
                                                current_distance_label=ctk.CTkLabel(
                                                    goal_tab,
                                                    text='Current Distance: '+str(current_distance)+' km',
                                                    font=('Helvetica',20),
                                                    text_color='black',
                                                )
                                                current_distance_label.place(x=200,y=50)
                                                distance_Label=ctk.CTkLabel(
                                                    goal_tab,
                                                    text='Goal Distance: '+distance_+' km',
                                                    font=('Helvetica',20),
                                                    text_color='black',
                                                )
                                                distance_Label.place(x=200,y=100)
                                                current_progress=ctk.CTkLabel(
                                                    goal_tab,
                                                    text='Current Progress: '+str(round(current_distance/float(distance_)*100,2))+'%',
                                                    font=('Helvetica',20),
                                                    text_color='black',
                                                )
                                                current_progress.place(x=200,y=150)
                                                progress_bar.set(current_distance/float(distance_))
                                                progress_bar.place(x=140,y=240)
                                                if current_distance>=float(distance_):
                                                    progress_bar.set(1)
                                                    current_progress.configure(text='Goal Achieved')
                    #create a page for the user to fill in the information for the goal they want to add
                    goal_page=tk.Toplevel()
                    goal_page.title('Add A Goal')
                    goal_page.configure(bg='#f0f0f0')
                    goal_page.resizable(False,False)
                    goal_page.geometry('350x250+530+280')
                    acti_type_Label=ctk.CTkLabel(
                        goal_page,
                        text='Activity Type:',
                        font=('Helvetica',15),
                        text_color='black',
                    )
                    acti_type_Label.place(x=55,y=50)
                    #a combobox for the user to select the activity type for the goal they want to add
                    activity_list=['Walking', 'Running', 'Cycling', 'Swimming']
                    acti_type=ttk.Combobox(goal_page,values=activity_list)
                    acti_type.place(x=150,y=50)

                    distance_Label=ctk.CTkLabel(
                        goal_page,
                        text='Distance:',
                        font=('Helvetica',15),
                        text_color='black',
                    )
                    distance_Label.place(x=70,y=100)

                    distance=ctk.CTkEntry(
                        goal_page,
                        fg_color=('black','white'),
                        text_color='black',
                        width=140,
                        height=30,
                        corner_radius=10,
                        font=('Helvetica',15),
                        placeholder_text='Enter distance',
                    )
                    distance.place(x=150,y=100)

                    distance_in_km=ctk.CTkLabel(
                        goal_page,
                        text='km',
                        font=('Helvetica',15),
                        text_color='black',
                    )
                    distance_in_km.place(x=305,y=100)
                    #a button to trigger the function save_goal to save the user's fitness goals
                    adda=ctk.CTkButton(
                        goal_page,
                        text='Add',
                        width=80,
                        height=40,
                        corner_radius=10,
                        fg_color=('white','#5c547e'),
                        hover_color=('white','#37334A'),
                        font=('Helvetica',15),
                        hover=True,
                        command=save_goal,
                    )
                    adda.place(x=130,y=150)
            #create a page for the user to select the goal type they want to add
            add_page=tk.Toplevel()
            add_page.title('Add Goal')
            add_page.geometry('350x200+530+280')
            goal_type=['Running-Walking-Cycling-Swimming Distance']
            goal_type_label=ctk.CTkLabel(
                add_page,
                text='Goal Type:',
                font=('Helvetica',15),
                text_color='black',
            )
            goal_type_label.place(x=55,y=50)
            goal=ttk.Combobox(add_page,values=goal_type)
            goal.place(x=150,y=50)
            add_button=ctk.CTkButton(
                add_page,
                text='Add',
                width=80,
                height=40,
                corner_radius=10,
                fg_color=('white','#5c547e'),
                hover_color=('white','#37334A'),
                font=('Helvetica',15),
                hover=True,
                command=goal_add,
            )
            add_button.place(x=130,y=120)
        #a button to trigger the function add_goal to add the user's fitness goals
        add_button=ctk.CTkButton(
            page_3,
            text='Add A Goal',
            width=80,
            height=40,
            corner_radius=10,
            fg_color=('white','#5c547e'),
            hover_color=('white','#37334A'),
            font=('Helvetica',15),
            hover=True,
            command=add_goal,
        )
        add_button.place(x=1200,y=190)
        delete_button=ctk.CTkButton(#a button to trigger the function delete_goal to delete the user's fitness goals
            page_3,
            text='Delete Goal',
            width=100,
            height=40,
            corner_radius=10,
            fg_color=('white','#5c547e'),
            hover_color=('white','#37334A'),
            font=('Helvetica',15),
            hover=True,
            command=delete_goal,
        )
        delete_button.place(x=1200,y=250)
        
        logged_in=Label(main_frame,text='Logged in as: '+name,fg='#5c547e',bg='#f0f0f0',font=('Helvetica',15))
        logged_in.place(x=640,y=730)
    #from 1522-1550: create four image buttons for the user to access the physical activities log, calorie intake log, fitness goals progress and change personal information pages
    log_out_image=Image.open('log_out_button.png')
    resized_log_out=log_out_image.resize((280,280))
    new_log_out_image=ImageTk.PhotoImage(resized_log_out)
    log_out_button=tk.Button(main_frame,image=new_log_out_image,borderwidth=0,command=log_out)
    log_out_button.place(x=880,y=450)

    physical_activities_image=Image.open('physical_log.png')
    resized_log=physical_activities_image.resize((280,280))
    new_log=ImageTk.PhotoImage(resized_log)
    log_button=tk.Button(main_frame,image=new_log,borderwidth=0,command=log)
    log_button.place(x=310,y=130)

    calorie_image=Image.open('calorie_remake.png')
    resized_calorie=calorie_image.resize((280,280))
    new_calorie=ImageTk.PhotoImage(resized_calorie)
    calorie_button=tk.Button(main_frame,image=new_calorie,borderwidth=0,command=intake)
    calorie_button.place(x=880,y=130)

    progress_image=Image.open('progress (1).png')
    resized_progress=progress_image.resize((280,280))
    new_progress=ImageTk.PhotoImage(resized_progress)
    progress_button=tk.Button(main_frame,image=new_progress,borderwidth=0,command=progress)
    progress_button.place(x=310,y=450)

    info_image=Image.open('perinfo.png')
    resized_info=info_image.resize((280,280))
    new_info=ImageTk.PhotoImage(resized_info)
    info_button=tk.Button(main_frame,image=new_info,borderwidth=0,command=change_personal_info)
    info_button.place(x=595,y=290)
    #a label to tell the user that they has logged in as 'name' variable
    logged_in=Label(main_frame,text='Logged in as: '+name,fg='#5c547e',bg='#f0f0f0',font=('Helvetica',15))
    logged_in.place(x=640,y=730)

    main_page.mainloop()

def sign_in_page():
    def sign_up():
        def make_new_account():
            #get the user's input for the new account
            new_user_name=new_username.get()
            new_pass_word=new_password.get()
            confirm_password=password_confirm.get()
            #if the user does not enter their username, password and confirm password, the user will be asked to enter their username, password and confirm password
            if new_user_name=='' and new_pass_word!='' and confirm_password==new_pass_word:
                messagebox.showerror('Invalid','Username is required')
                sign_up_window.attributes('-topmost', True)
                sign_up_window.attributes('-topmost', False)
                new_username.delete(0,tk.END)
                new_password.delete(0,tk.END)
                password_confirm.delete(0,tk.END)
            elif new_pass_word=='' and new_user_name!='' and confirm_password!='':
                messagebox.showerror('Invalid','Password is required')
                sign_up_window.attributes('-topmost', True)
                sign_up_window.attributes('-topmost', False)
                new_username.delete(0,tk.END)
                new_password.delete(0,tk.END)
                password_confirm.delete(0,tk.END)
            elif new_pass_word=='' and new_user_name!='' and confirm_password=='':
                messagebox.showerror('Invalid','Password is required')
                sign_up_window.attributes('-topmost', True)
                sign_up_window.attributes('-topmost', False)
                new_username.delete(0,tk.END)
                new_password.delete(0,tk.END)
                password_confirm.delete(0,tk.END)
            elif new_user_name=='' and new_pass_word=='' and confirm_password!='':
                messagebox.showerror('Invalid','Username and Password are required')
                sign_up_window.attributes('-topmost', True)
                sign_up_window.attributes('-topmost', False)
                new_username.delete(0,tk.END)
                new_password.delete(0,tk.END)
                password_confirm.delete(0,tk.END)
            elif new_user_name=='' and new_pass_word=='' and confirm_password=='':
                messagebox.showerror('Invalid','Username and Password are required')
                sign_up_window.attributes('-topmost', True)
                sign_up_window.attributes('-topmost', False)
                new_username.delete(0,tk.END)
                new_password.delete(0,tk.END)
                password_confirm.delete(0,tk.END)
            elif new_user_name!='' and new_pass_word!='' and confirm_password!=new_pass_word:
                messagebox.showerror('Invalid','Passwords do not match')
                sign_up_window.attributes('-topmost', True)
                sign_up_window.attributes('-topmost', False)
                new_username.delete(0,tk.END)
                new_password.delete(0,tk.END)
                password_confirm.delete(0,tk.END)
            #if the user enters their username, password and confirm password, the user's account will be checked to see if the account already exists
            elif new_user_name!='' and new_pass_word!='' and confirm_password==new_pass_word:
                account_exists=False
                with open('account info','r') as booking:
                    allAccounts=csv.reader(booking)
                    next(allAccounts)
                    allaccounts=list(allAccounts)
                    for line in allaccounts:
                        if len(line)>=2:
                            if new_user_name == line[0]:
                                account_exists=True
                    if account_exists==True:
                        #if the account already exists, the user will be informed that the account already exists and the user will be asked to enter a new username and password
                        messagebox.showerror('Invalid','Account already exists')
                        sign_up_window.attributes('-topmost', True)
                        sign_up_window.attributes('-topmost', False)
                        new_username.delete(0,tk.END)
                        new_password.delete(0,tk.END)
                        password_confirm.delete(0,tk.END)
                    else:
                        #if the account does not exist, the user's account will be created and the user will be informed that the account has been created successfully
                        with open('account info','a',newline='') as booking:
                            newBooking=csv.writer(booking)
                            newBooking.writerow([new_user_name,new_pass_word])
                            messagebox.showinfo('Success','Account created successfully')
                            sign_up_window.destroy()
        #create a window for the user to sign up
        sign_up_window=tk.Toplevel()
        sign_up_window.title('Login')
        sign_up_window.geometry('450x350+530+280')
        sign_up_window.configure(bg='#f0f0f0')
        #line 1634-1749: create the labels, entry boxes and buttons for the user to sign up
        heading=Label(sign_up_window,text='Sign up', fg='#5c547e',bg='#f0f0f0',font=('Helvetica',30,'bold' ))
        heading.place(x=143,y=15)

        new_username_Label=ctk.CTkLabel(
            sign_up_window,
            text='Username:',
            font=('Helvetica',15),
            text_color='black',
        )
        new_username_Label.place(x=70,y=100)

        new_username=ctk.CTkEntry(
            sign_up_window,
            fg_color=('black','white'),
            text_color='black',
            width=200,
            height=30,
            corner_radius=10,
            font=('Helvetica',15),
            placeholder_text='Enter your username'
        )
        new_username.place(x=150,y=100) 

        new_password_Label=ctk.CTkLabel(
            sign_up_window,
            text='Password:',
            font=('Helvetica',15),
            text_color='black',
        )
        new_password_Label.place(x=70,y=160)

        new_password=ctk.CTkEntry(
            sign_up_window,
            fg_color=('black','white'),
            text_color='black',
            width=200,
            height=30,
            corner_radius=10,
            font=('Helvetica',15),
            placeholder_text='Enter your password',
            show='*',
        )
        new_password.place(x=150,y=160)

        def show_password():#function to show the user's password
            if new_password.cget('show')=='*':
                new_password.configure(show='')
            else:
                new_password.configure(show='*')
        check_button=tk.Checkbutton(
            sign_up_window,
            text='Show',
            border=0,
            fg='#5c547e',
            bg='#f0f0f0',
            font=('Helvetica',11),
            cursor='hand2',
            activebackground='#f0f0f0',
            activeforeground='#37334A',
            command=show_password,
        )
        check_button.place(x=360,y=162)
        
        password_confirm_Label=ctk.CTkLabel(
            sign_up_window,
            text='Confirm Password:',
            font=('Helvetica',15),
            text_color='black',
        )
        password_confirm_Label.place(x=17,y=220)

        password_confirm=ctk.CTkEntry(
            sign_up_window,
            fg_color=('black','white'),
            text_color='black',
            width=200,
            height=30,
            corner_radius=10,
            font=('Helvetica',15),
            placeholder_text='Confirm your password',
            show='*',
        )
        password_confirm.place(x=150,y=220) 

        def show_password2():#function to show the user's password
            if password_confirm.cget('show')=='*':
                password_confirm.configure(show='')
            else:
                password_confirm.configure(show='*')
        check_button2=tk.Checkbutton(
            sign_up_window,
            text='Show',
            border=0,
            fg='#5c547e',
            bg='#f0f0f0',
            font=('Helvetica',11),
            cursor='hand2',
            activebackground='#f0f0f0',
            activeforeground='#37334A',
            command=show_password2,
        )
        check_button2.place(x=360,y=222)

        sign_up=ctk.CTkButton(
            sign_up_window,
            text='Create account',
            width=280,
            height=40,
            corner_radius=10,
            fg_color=('white','#5c547e'),
            hover_color=('white','#37334A'),
            font=('Helvetica',15),
            hover=True,
            command=make_new_account,
        )
        sign_up.place(x=70,y=280)
        root.mainloop()
    def sign_in():
        #get the user's input for the username and password
        user_name=username.get()
        pass_word=password.get()
        if user_name=='' and pass_word!='':#if the user does not enter their username, the user will be asked to enter their username
            messagebox.showerror('Invalid','Username is required')
        elif pass_word=='' and user_name!='':
            messagebox.showerror('Invalid','Password is required')
        elif user_name=='' and pass_word=='':
            messagebox.showerror('Invalid','Username and Password are required')
        elif user_name!='' and pass_word!='':
            #if the user enters their username and password, the user's account will be checked to see if the account exists
            with open('account info','r') as booking:
                allBooking=csv.reader(booking)
                next(allBooking)
                global allaccounts
                allaccounts=list(allBooking)
                account_exists=False
                correct_password=False
                for line in allaccounts:#iterate through the account info file to check if the user's account exists
                    if len(line)>=2:
                        if user_name == line[0] and pass_word == line[1]:
                            account_exists=True
                            correct_password=True
                        elif user_name == line[0] and pass_word != line[1]:
                            account_exists=True
                            correct_password=False
                if account_exists==True and correct_password==True:
                        #if the account exists and the password is correct, the user will be informed that they have logged in successfully and the home page will be displayed
                        messagebox.showinfo('Success','Logged in successfully')
                        global name
                        name=user_name
                        home_page()#call the function home_page to display the home page
                elif account_exists == True and correct_password ==False:
                    #if the account exists and the password is incorrect, the user will be informed that the password is incorrect
                    messagebox.showerror('Invalid','Incorrect password')
                elif account_exists==False:
                    messagebox.showinfo('Invalid','Account does not exist')
    #create a window for the user to sign in                
    global root
    root=tk.Tk()
    root.title('Login')
    root.geometry('925x500+300+200')
    root.configure(bg='#f0f0f0')
    root.resizable(False,False)
    #1801-1909: create the labels, entry boxes and buttons for the user to sign in and add pictures to the sign in page
    frame=Frame(root,width=350,height=350,bg='#f0f0f0')
    frame.place(x=520,y=70)

    my_pic=Image.open('9544904.png')
    resized=my_pic.resize((300,300))
    new_pic=ImageTk.PhotoImage(resized)
    Label(root,image=new_pic,bg='#f0f0f0').place(x=100,y=50)

    pic_label=Label(root,text='FITNESS TRACKER',fg='#5c547e',bg='#f0f0f0',font=('Helvetica',25,'bold'))
    pic_label.place(x=100,y=370)

    heading=Label(frame,text='Sign in', fg='#5c547e',bg='#f0f0f0',font=('Helvetica',30,'bold' ))
    heading.place(x=73,y=15)

    username_Label=ctk.CTkLabel(frame,
        text='Username:',
        font=('Helvetica',15),
        text_color='black',
    )
    username_Label.place(x=0,y=100)

    username=ctk.CTkEntry(
        frame,
        fg_color=('black','white'),
        text_color='black',
        width=200,
        height=30,
        corner_radius=10,
        font=('Helvetica',15),
        placeholder_text='Enter your username'
    )
    username.place(x=80,y=100) 

    password_Label=ctk.CTkLabel(frame,
        text='Password:',
        font=('Helvetica',15),
        text_color='black',
    )
    password_Label.place(x=0,y=160)

    password=ctk.CTkEntry(
        frame,
        fg_color=('black','white'),
        text_color='black',
        width=200,
        height=30,
        corner_radius=10,
        font=('Helvetica',15),
        placeholder_text='Enter your password',
        show='*',
    )
    password.place(x=80,y=160)


    def show_password():
        if password.cget('show')=='*':
            password.configure(show='')
        else:
            password.configure(show='*')
    check_button=tk.Checkbutton(
        frame,
        text='Show',
        border=0,
        fg='#5c547e',
        bg='#f0f0f0',
        font=('Helvetica',11),
        cursor='hand2',
        activebackground='#f0f0f0',
        activeforeground='#37334A',
        command=show_password,
    )
    check_button.place(x=283,y=163)

    sign_in_button=ctk.CTkButton(
        frame,
        text='Sign in',
        width=280,
        height=40,
        corner_radius=10,
        fg_color=('white','#5c547e'),
        hover_color=('white','#37334A'),
        font=('Helvetica',15),
        hover=True,
        command=sign_in
    )
    sign_in_button.place(x=0,y=220)

    create_account=ctk.CTkLabel(
        frame,
        text="You don't have an account?",
        font=('Helvetica',15),
        text_color='black',
    )
    create_account.place(x=7,y=260)

    sign_up_button=tk.Button(
        frame,
        text='Sign up here',
        border=0,
        fg='#5c547e',
        bg='#f0f0f0',
        font=('Helvetica',11),
        cursor='hand2',
        activebackground='#f0f0f0',
        activeforeground='#37334A',
        command=sign_up,
    )
    sign_up_button.place(x=185,y=260)
    root.mainloop()

sign_in_page() #call the function sign_in_page to display the sign in page when the program is run
