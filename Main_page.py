import tkinter as tk
import tkinter.ttk as ttk
from pygubu.widgets.editabletreeview import EditableTreeview
import mysql.connector
from tkcalendar import Calendar
from tkinter.messagebox import * 



main_root=tk.Tk()
main_root.title("Admin Login")
main_root.geometry('750x500')
ans=list()
 #Database Connection


mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Password1.')

c=mydb.cursor()

c.execute("use Project_db;")

def added():
    showinfo("Information","Details Added Successfully.\t\n")
def deleted(name):
    answer= askquestion("Warning",f"Doy you want to delete the Details of {name}?\t\t\n")
    if answer == 'yes':
        return True
    else:
        return False
    

def updated():
    showinfo("Information","Details Updated Successfully.\t\n\n")




#Main class for ui
class Main:
    def __init__(self, master=None):
        
        # build ui
        self.main_frame = ttk.Notebook(master)
        self.date=str()
        self.values=str()
        self.upateid=int()
        self.idd = int()
        self.tobe= int()
        self.by= str()
        self.value=str()
        self.update_values = str()

        # Add Frame components...
        self.Add_frame = ttk.Frame(self.main_frame)
            
        self.name_entry = ttk.Entry(self.Add_frame)
        self.name_entry.configure(font='{timesnew} 12 {italic}')
        self.name_entry.place(anchor='nw', relheight='0.05',relwidth='0.25', relx='0.19', rely='0.1', x='0', y='0')

        self.name_label = ttk.Label(self.Add_frame)
        self.name_label.configure(anchor='n', compound='top', font='{timesnew} 12 {italic}', text='Name ')
        self.name_label.place(anchor='nw', relx='0.04', rely='0.1', x='0', y='0')
            
        self.age_label = ttk.Label(self.Add_frame)
        self.age_label.configure(font='{Timesnew} 12 {italic}', text='Age')
        self.age_label.place(anchor='nw', relx='0.04', rely='0.2', x='0', y='0')
            
        self.age_entry = ttk.Entry(self.Add_frame)
        self.age_entry.configure(font='{timesnew} 12 {italic}')
        self.age_entry.place(anchor='nw', relwidth='0.25',relheight='0.05', relx='0.19', rely='0.2', x='0', y='0')
        
        self.dob_label = ttk.Label(self.Add_frame)
        self.dob_label.configure(font='{timesnew} 12 {italic}', text='DOB')
        self.dob_label.place(anchor='nw', relx='0.04', rely='0.3', x='0', y='0')
        
        self.gender_label = ttk.Label(self.Add_frame)
        self.gender_label.configure(font='{timesnew} 12 {italic}', text='Gender')
        self.gender_label.place(anchor='nw', relx='0.04', rely='0.6', x='0', y='0')
        
        self.gender_combobox = ttk.Combobox(self.Add_frame)
        self.gender_combobox.configure(height='3', justify='left',font='{timesnew} 12 {italic}', values=('Male','Female'), width='23')
        self.gender_combobox.place(anchor='nw', relheight='0.05',relwidth='0.25', relx='0.19', rely='0.6', x='0', y='0')
        
        self.email_label = ttk.Label(self.Add_frame)
        self.email_label.configure(font='{timesnew} 12 {italic}', takefocus=False, text='Email ')
        self.email_label.place(anchor='nw', relx='0.55', rely='0.1', x='0', y='0')
        
        self.email_entry = ttk.Entry(self.Add_frame)
        self.email_entry.configure(font='{timenew} 12 {italic}')
        self.email_entry.place(anchor='nw', relheight='0.05', relwidth='0.25', relx='0.7', rely='0.1', x='0', y='0')
        
        self.contact_label = ttk.Label(self.Add_frame)
        self.contact_label.configure(font='{timesnew} 12 {italic}', text='Contact No')
        self.contact_label.place(anchor='nw', relx='0.55', rely='0.2', x='0', y='0')
        
        self.contact_entry = ttk.Entry(self.Add_frame)
        self.contact_entry.configure(font='{timesnew} 12 {italic}')
        self.contact_entry.place(anchor='nw', relheight='0.05', relwidth='0.25',relx='0.7', rely='0.2', x='0', y='0')
        
        self.blood_group_label = ttk.Label(self.Add_frame)
        self.blood_group_label.configure(font='{timesnew} 12 {italic}', text='Blood Group')
        self.blood_group_label.place(anchor='nw', relx='0.55', rely='0.3', x='0', y='0')
        
        self.blood_group_entry = ttk.Entry(self.Add_frame)
        self.blood_group_entry.configure(font='{timesnew} 12 {italic}')
        self.blood_group_entry.place(anchor='nw', relheight='0.05',relwidth='0.25' ,relx='0.7', rely='0.3', x='0', y='0')
        
        self.nationality_label = ttk.Label(self.Add_frame)
        self.nationality_label.configure(font='{timesnew} 12 {italic}', text='Country')
        self.nationality_label.place(anchor='nw', relx='0.55', rely='0.4', x='0', y='0')
        
        self.nationality_entry = ttk.Entry(self.Add_frame)
        self.nationality_entry.configure(font='{timesnew} 12 {italic}')
        self.nationality_entry.place(anchor='nw', relheight='0.05', relwidth='0.25',relx='0.7', rely='0.4', x='0', y='0')
        
        self.department_label = ttk.Label(self.Add_frame)
        self.department_label.configure(font='{timesnew} 12 {italic}', text='Derpartment')
        self.department_label.place(anchor='nw', relx='0.55', rely='0.5', x='0', y='0')
        
        self.department_entry = ttk.Entry(self.Add_frame)
        self.department_entry.configure(font='{timesnew} 12 {italic}')
        self.department_entry.place(anchor='nw', relheight='0.05', relwidth='0.25',relx='0.7', rely='0.5', x='0', y='0')
        
        self.address_label = ttk.Label(self.Add_frame)
        self.address_label.configure(font='{timesnew} 12 {italic}', text='City')
        self.address_label.place(anchor='nw', relx='0.04', rely='0.7', x='0', y='0')
        
        self.address_entry = ttk.Entry(self.Add_frame)
        self.address_entry.configure(font='{timesnew} 12 {italic}', justify='left')
        self.address_entry.place(anchor='nw', relheight='0.05', relwidth='0.25',relx='0.19', rely='0.7', x='0', y='0')
        
        self.add_button = tk.Button(self.Add_frame)
        self.add_button.configure(background='#b2edec', font='{timesnew} 12 {italic}', foreground='black', text='    Add    ')
        self.add_button.place(anchor='nw', relx='0.8', rely='0.75', x='0', y='0')
        self.add_button.configure(command=self.add_to_database)
        
        self.clear_default = tk.Button(self.Add_frame)
        self.clear_default.configure(background='#f78fe4', font='{timesnew} 12 {italic}', foreground='black', text=' Clear ')
        self.clear_default.configure(command=self.clear_all)
        self.clear_default.place(anchor='nw', relx='0.65', rely='0.75', x='0', y='0')
        
        self.id_label_add = ttk.Label(self.Add_frame)
        self.id_label_add.configure(font='{timesnew} 12 {italic}', text='ID')
        self.id_label_add.place(anchor='nw', relx='0.55', rely='0.6', x='0', y='0')
        
        self.id_entry_add = ttk.Entry(self.Add_frame)
        self.id_entry_add.configure(font='{timesnew} 12 {italic}')
        self.id_entry_add.place(anchor='nw', relheight='0.05',relwidth='0.25', relx='0.7', rely='0.6', x='0', y='0')
        
        self.dob_picker_add = Calendar(self.Add_frame,selectmode='day',year=2002,month=2,day=14,date_pattern='Y/MM/D')
        
        self.dob_picker_add.place(anchor='nw', relheight='0.25', relwidth='0.3', relx='0.19', rely='0.3', x='0', y='0')
        
        self.label1 = ttk.Label(self.Add_frame)
        self.label1.configure(text='Note: ')
        self.label1.place(anchor='nw', relx='0.02', rely='0.85', x='0', y='0')
        
        self.label2 = ttk.Label(self.Add_frame)
        self.label2.configure(text='All fields are mandatory.')
        self.label2.place(anchor='nw', relx='0.04', rely='0.89', x='0', y='0')
        
        self.Add_frame.configure(height='500', width='750')
        self.Add_frame.pack(side='top')
        
        self.main_frame.add(self.Add_frame, text='    Add     ')

#Update Frame Componets.....

        self.update_frame = ttk.Frame(self.main_frame)
        
        self.name_entry_update = ttk.Entry(self.update_frame)
        self.name_entry_update.configure(font='{timesnew} 12 {italic}')
        self.name_entry_update.place(anchor='nw', relheight='0.05', relwidth='0.25', relx='0.19', rely='0.2', x='0', y='0')
        
        self.name_label_update = ttk.Label(self.update_frame)
        self.name_label_update.configure(anchor='n', compound='top', font='{timesnew} 12 {italic}', text='Name ')
        self.name_label_update.place(anchor='nw', relx='0.04', rely='0.2', x='0', y='0')
        
        self.age_label_update = ttk.Label(self.update_frame)
        self.age_label_update.configure(font='{Timesnew} 12 {italic}', text='Age')
        self.age_label_update.place(anchor='nw', relx='0.04', rely='0.3', x='0', y='0')
        
        self.age_entry_update = ttk.Entry(self.update_frame)
        self.age_entry_update.configure(font='{timesnew} 12 {italic}')
        self.age_entry_update.place(anchor='nw', relheight='0.05', relwidth='0.25', relx='0.19', rely='0.3', x='0', y='0')
        
        self.dob_label_update = ttk.Label(self.update_frame)
        self.dob_label_update.configure(font='{timesnew} 12 {italic}', text='DOB')
        self.dob_label_update.place(anchor='nw', relx='0.04', rely='0.4', x='0', y='0')
        
        self.gender_label_update = ttk.Label(self.update_frame)
        self.gender_label_update.configure(font='{timesnew} 12 {italic}', text='Gender')
        self.gender_label_update.place(anchor='nw', relx='0.04', rely='0.7', x='0', y='0')
        
        self.gender_combobox_updte = ttk.Combobox(self.update_frame)
        self.gender_combobox_updte.configure(height='3', justify='left', values=('Male','Female'), width='23',font='{timesnew} 12 {italic}')
        self.gender_combobox_updte.place(anchor='nw', relheight='0.05', relwidth='0.25', relx='0.19', rely='0.7', x='0', y='0')
        
        self.email_label_update = ttk.Label(self.update_frame)
        self.email_label_update.configure(font='{timesnew} 12 {italic}', takefocus=False, text='Email ')
        self.email_label_update.place(anchor='nw', relx='0.55', rely='0.2', x='0', y='0')
        
        self.email_entry_update = ttk.Entry(self.update_frame)
        self.email_entry_update.configure(font='{timenew} 12 {italic}')
        self.email_entry_update.place(anchor='nw', relheight='0.05',relwidth='0.25', relx='0.7', rely='0.2', x='0', y='0')
        
        self.contact_label_update = ttk.Label(self.update_frame)
        self.contact_label_update.configure(font='{timesnew} 12 {italic}', text='Contact No')
        self.contact_label_update.place(anchor='nw', relx='0.55', rely='0.3', x='0', y='0')
        
        self.contact_entry_update = ttk.Entry(self.update_frame)
        self.contact_entry_update.configure(font='{timesnew} 12 {italic}')
        self.contact_entry_update.place(anchor='nw', relheight='0.05',relwidth='0.25', relx='0.7', rely='0.3', x='0', y='0')
        
        self.blood_label_update = ttk.Label(self.update_frame)
        self.blood_label_update.configure(font='{timesnew} 12 {italic}', text='Blood Group')
        self.blood_label_update.place(anchor='nw', relx='0.55', rely='0.4', x='0', y='0')
        
        self.blood_entry_update = ttk.Entry(self.update_frame)
        self.blood_entry_update.configure(font='{timesnew} 12 {italic}')
        self.blood_entry_update.place(anchor='nw', relheight='0.05',relwidth='0.25',relx='0.7', rely='0.4', x='0', y='0')
        
        self.nationality_label_update = ttk.Label(self.update_frame)
        self.nationality_label_update.configure(font='{timesnew} 12 {italic}', text='Country')
        self.nationality_label_update.place(anchor='nw', relx='0.55', rely='0.5', x='0', y='0')
        
        self.nationality_entry_update = ttk.Entry(self.update_frame)
        self.nationality_entry_update.configure(font='{timesnew} 12 {italic}')
        self.nationality_entry_update.place(anchor='nw', relheight='0.05', relwidth='0.25',relx='0.7', rely='0.5', x='0', y='0')
        
        self.department_label_update = ttk.Label(self.update_frame)
        self.department_label_update.configure(font='{timesnew} 12 {italic}', text='Department')
        self.department_label_update.place(anchor='nw', relx='0.55', rely='0.6', x='0', y='0')
        
        self.department_entry_update = ttk.Entry(self.update_frame)
        self.department_entry_update.configure(font='{timesnew} 12 {italic}')
        self.department_entry_update.place(anchor='nw', relheight='0.05',relwidth='0.25', relx='0.7', rely='0.6', x='0', y='0')
        
        self.address_label_update = ttk.Label(self.update_frame)
        self.address_label_update.configure(font='{timesnew} 12 {italic}', text='City')
        self.address_label_update.place(anchor='nw', relx='0.55', rely='0.7', x='0', y='0')
        
        self.address_entry_update = ttk.Entry(self.update_frame)
        self.address_entry_update.configure(font='{timesnew} 12 {italic}', justify='left')
        self.address_entry_update.place(anchor='nw', relheight='0.05',relwidth='0.25', relx='0.7', rely='0.7', x='0', y='0')
        
        self.update_button_update = tk.Button(self.update_frame)
        self.update_button_update.configure(background='#f78fe4', font='{timesnew} 12 {italic}', foreground='black', justify='right')
        self.update_button_update.configure(text='Update')
        self.update_button_update.place(anchor='nw', relx='0.75', rely='0.85', x='0', y='0')
        self.update_button_update.configure(command=self.update_details)
        
        self.dob_picker_update= Calendar(self.update_frame,selectmode='day',year=2021,month=12,day=22,date_pattern='Y/MM/D')
        self.dob_picker_update.place(anchor='nw', relheight='0.25', relwidth='0.3', relx='0.19', rely='0.4', x='0', y='0')
        
        self.id_input_update = ttk.Label(self.update_frame)
        self.id_input_update.configure(font='{timesnew} 12 {italic}', text='Enter the Id to be update')
        self.id_input_update.place(anchor='nw', relx='0.04', rely='0.08', x='0', y='0')
        self.id_input_entry_update = ttk.Entry(self.update_frame)
        self.id_input_entry_update.configure(font='{timesnew} 12 {italic}')
        self.id_input_entry_update.place(anchor='nw', relheight='0.05',relwidth='0.25', relx='0.35', rely='0.08', x='0', y='0')
        
        self.Ok_button_view = tk.Button(self.update_frame)
        self.Ok_button_view.configure(anchor='sw', background='#f78fe4', font='{timesnew} 12 {italic}', foreground='black')
        self.Ok_button_view.configure(justify='right', text='  OK  ')
        self.Ok_button_view.place(anchor='nw', relx='0.75', rely='0.07', x='0', y='0')
        self.Ok_button_view.configure(command=self.send_text_to_field)
        
        self.clear_default_view = tk.Button(self.update_frame)
        self.clear_default_view.configure(background='#f78fe4', font='{timesnew} 12 {italic}', foreground='black', text=' Clear ')
        self.clear_default_view.configure(command=self.clear_all_view)
        self.clear_default_view.place(anchor='nw', relx='0.60', rely='0.85', x='0', y='0')
        
        self.label5 = ttk.Label(self.update_frame)
        self.label5.configure(text='Note')
        self.label5.place(anchor='nw', relx='0.02', rely='0.85', x='0', y='0')
        
        self.label6 = ttk.Label(self.update_frame)
        self.label6.configure(text='Edit the value to be changed/modified.')
        self.label6.place(anchor='nw', relx='0.05', rely='0.9', x='0', y='0')
        
        self.update_frame.configure(height='200', width='200')
        self.update_frame.pack(side='top')
        
        self.main_frame.add(self.update_frame, text='  Update  ')


    #Delete Frame components....

        
        self.delete_frame = ttk.Frame(self.main_frame)
        
        self.tobe_deleted_label_delete_ = ttk.Label(self.delete_frame)
        self.tobe_deleted_label_delete_.configure(font='{timesnew} 12 {italic}', text='Enter the Id to be Deleted')
        self.tobe_deleted_label_delete_.place(anchor='nw', relx='0.04', rely='0.2', x='0', y='0')
        
        self.tobe_deleted_id_entry_delete = ttk.Entry(self.delete_frame)
        self.tobe_deleted_id_entry_delete.configure(font='{timesnew} 12 {italic}')
        self.tobe_deleted_id_entry_delete.place(anchor='nw', relheight='0.05',relwidth='0.25', relx='0.35', rely='0.2', x='0', y='0')
        
        self.ok_button_delete = tk.Button(self.delete_frame)
        self.ok_button_delete.configure(anchor='sw', background='#f78fe4', font='{timesnew} 12 {italic}', foreground='black')
        self.ok_button_delete.configure(justify='right', text='Delete')
        self.ok_button_delete.place(anchor='nw', relx='0.75', rely='0.8', x='0', y='0')
        self.ok_button_delete.configure(command=self.delete_details)
        
        self.label3 = ttk.Label(self.delete_frame)
        self.label3.configure(text='Note :')
        self.label3.place(anchor='nw', relx='0.02', rely='0.85', x='0', y='0')
        
        self.label4 = ttk.Label(self.delete_frame)
        self.label4.configure(text="Data can't be retrieved once deleted")
        self.label4.place(anchor='nw', relx='0.05', rely='00.9', x='0', y='0')
        
        self.delete_frame.configure(height='200', width='200')
        self.delete_frame.pack(side='top')
        
        self.main_frame.add(self.delete_frame, text='  Delete  ')


    #View Frame components........

        self.View_frame = ttk.Frame(self.main_frame)
        
        self.view_label_view = ttk.Label(self.View_frame)
        self.view_label_view.configure(font='{timesnew} 12 {italic}', text='View by')
        self.view_label_view.place(anchor='nw', relx='0.07', rely='0.09', x='0', y='0')
        
        self.viewby_combobox_view = ttk.Combobox(self.View_frame)
        self.viewby_combobox_view.configure(values=('Id','Gender','Name','Age','Blood_Group','Country','Department'),font='{timesnew} 12 {italic}')
        self.viewby_combobox_view.place(anchor='nw', relheight='0.05', relwidth='0.25',relx='0.18', rely='0.09', x='0', y='0')

        self.treeview = EditableTreeview(self.View_frame)
        self.treeview.place(anchor='nw', relheight='0.7', relwidth='0.98', relx='0.01', rely='0.25', x='0', y='0')

        self.treeview['columns']=('Id','Name','DOB','Age','Gender','Blood_Group','Email','Number','City','Country','Department')
        self.treeview.column('#0',width=0,stretch=0)
        self.treeview.heading('Id',text='Id',anchor='n')
        self.treeview.column('Id',width=25,stretch='NO')
        self.treeview.heading('Name',text='Name',anchor='n')
        self.treeview.column('Name',width=100,stretch='NO')
        self.treeview.heading('DOB',text='DOB',anchor='n')
        self.treeview.column('DOB',width=85,stretch='NO')
        self.treeview.heading('Age',text='Age',anchor='n')
        self.treeview.column('Age',width=75,stretch='NO')
        self.treeview.heading('Gender',text='Gender',anchor='n')
        self.treeview.column('Gender',width=100,stretch='NO')
        self.treeview.heading('Blood_Group',text='Blood_Group',anchor='n')
        self.treeview.column('Blood_Group',width=100,stretch='NO')
        self.treeview.heading('Email',text='Email',anchor='n')
        self.treeview.column('Email',width=275,stretch='NO')
        self.treeview.column('Number',width=100,stretch='NO')
        self.treeview.heading('Number',text='Number',anchor='n')
        self.treeview.heading('City',text='City',anchor='n')
        #self.treeview.column('City',width=75,stretch='NO')
        self.treeview.heading('Country',text='Country',anchor='n')
        self.treeview.column('Country',width=200,stretch='NO')
        self.treeview.heading('Department',text='Department',anchor='n')
        #self.treeview.column('Department',width=90,stretch='NO')

        self.value_entry_view = ttk.Entry(self.View_frame)
        self.value_entry_view.configure(font='{timesnew} 12 {italic}')
        self.value_entry_view.place(anchor='nw', relheight='0.05',relwidth='0.25', relx='0.52', rely='0.09', x='0', y='0')
        
        self.value_label_view = ttk.Label(self.View_frame)
        self.value_label_view.configure(font='{timesnew} 12 {italic}', text='Value')
        self.value_label_view.place(anchor='nw', relx='0.45', rely='0.09', x='0', y='0')
        
        self.view_button_view = tk.Button(self.View_frame)
        self.view_button_view.configure(background='#b2edec', font='{timesnew} 12 {italic}', foreground='black', text='View')
        self.view_button_view.place(anchor='nw', relx='0.86', rely='0.16', x='0', y='0')
        self.view_button_view.configure(command=self.view_details)
        
        self.View_frame.configure(height='200', width='200')
        self.View_frame.pack(side='top')
        
        self.main_frame.add(self.View_frame, text='   View   ')


        self.main_frame.configure(height='500', takefocus=False, width='750')

        self.main_frame.pack(anchor='center', expand='true', fill='both', side='top')

        # Main widget
        self.mainwindow = self.main_frame
    
    def run(self):
        self.mainwindow.mainloop()

#Clearing the Entry in the Update panel.....


#Clear the details inn the viewframe..
    def clear_all_view(self):
        self.name_entry_update.delete(0,'end')
        self.age_entry_update.delete(0,'end')
        self.gender_combobox_updte.delete(0,'end')
        self.contact_entry_update.delete(0,'end')
        self.department_entry_update.delete(0,'end')
        self.address_entry_update.delete(0,'end')
        self.contact_entry_update.delete(0,'end')
        self.id_input_entry_update.delete(0,'end')
        self.blood_entry_update.delete(0,'end')
        self.email_entry_update.delete(0,'end')
        self.nationality_entry_update.delete(0,'end')
        print("\nclearing.....")


#Adding Details to the database Function.....
    def add_to_database(self):

        self.date=str(self.dob_picker_add.selection_get())
        print(self.date)
        self.date=self.date.replace("/","-")
        print(self.date)
       
        self.values=f'{self.id_entry_add.get()},"{self.name_entry.get()}","{self.date}",{self.age_entry.get()},"{self.gender_combobox.get()}","{self.blood_group_entry.get()}","{self.email_entry.get()}","{self.contact_entry.get()}","{self.address_entry.get()}","{self.nationality_entry.get()}","{self.department_entry.get()}"'
        print(self.values)

        #Adding the Details to the database
        c.execute(f'insert into Employees values({self.values})')
       
        added()

        self.id_entry_add.delete(0,'end')
        self.name_entry.delete(0,'end')
        self.age_entry.delete(0,'end')
        self.gender_combobox.delete(0,'end')
        self.address_entry.delete(0,'end')
        self.email_entry.delete(0,'end')
        self.contact_entry.delete(0,'end')
        self.blood_group_entry.delete(0,'end')
        self.nationality_entry.delete(0,'end')
        self.department_entry.delete(0,'end')
        #self.dob_picker_add.selection_set('2002/01/02')
        print("\nDetails Added Successfully......")



#Update details function....
    def update_details(self):
        self.upateid=self.id_input_entry_update.get()
        self.date=str(self.dob_picker_update.selection_get())
        self.date=self.date.replace("/","-")
        print(self.date)
        self.update_values=f'Name="{self.name_entry_update.get()}",Age={self.age_entry_update.get()},DOB="{self.date}",Gender="{self.gender_combobox_updte.get()}",Blood_group="{self.blood_entry_update.get()}",Email="{self.email_entry_update.get()}",Number="{self.contact_entry_update.get()}",City="{self.address_entry_update.get()}",Nationality="{self.nationality_entry_update.get()}",Department="{self.department_entry_update.get()}"'
        c.execute(f"update Employees set {self.update_values} where id={self.upateid}")
        print("\nDetails Updated...")
        updated()
        self.name_entry_update.delete(0,'end')
        self.age_entry_update.delete(0,'end')
        self.gender_combobox_updte.delete(0,'end')
        self.address_entry_update.delete(0,'end')
        self.email_entry_update.delete(0,'end')
        self.contact_entry_update.delete(0,'end')
        self.blood_entry_update.delete(0,'end')
        self.nationality_entry_update.delete(0,'end')
        self.department_entry_update.delete(0,'end')
        self.id_input_entry_update.delete(0,'end')
        global ans
        ans=[]

#Sending text to the field for updation

    def send_text_to_field(self):
        self.idd=self.id_input_entry_update.get()
        c.execute(f'select * from Employees where id={self.idd}')
        global ans
        for x in c:
            ans=list(x)

        print(ans)
        c.reset()
        self.name_entry_update.delete(0,'end')
        self.age_entry_update.delete(0,'end')
        self.gender_combobox_updte.delete(0,'end')
        self.address_entry_update.delete(0,'end')
        self.email_entry_update.delete(0,'end')
        self.contact_entry_update.delete(0,'end')
        self.blood_entry_update.delete(0,'end')
        self.nationality_entry_update.delete(0,'end')
        self.department_entry_update.delete(0,'end')
        print("\nclearing the value and adding the new value...\n")

        self.dob_picker_update.selection_set(ans[2])
        self.name_entry_update.insert(0,ans[1])
        self.age_entry_update.insert(0,ans[3])
        self.gender_combobox_updte.insert(0,ans[4])
        self.blood_entry_update.insert(0,ans[5])
        self.email_entry_update.insert(0,ans[6])
        self.contact_entry_update.insert(0,ans[7])
        self.address_entry_update.insert(0,ans[8])
        self.nationality_entry_update.insert(0,ans[9])
        self.department_entry_update.insert(0,ans[10])

#Clear Text in the enrty box
        
    def clear_all(self):

        self.id_entry_add.delete(0,'end')
        self.name_entry.delete(0,'end')
        self.dob_picker_add.selection_clear()
        self.age_entry.delete(0,'end')
        self.gender_combobox.delete(0,'end')
        self.address_entry.delete(0,'end')
        self.email_entry.delete(0,'end')
        self.contact_entry.delete(0,'end')
        self.blood_group_entry.delete(0,'end')
        self.nationality_entry.delete(0,'end')
        self.department_entry.delete(0,'end')
        print("\nCleared Successfully....")

#Delete the details from the database
        
    def delete_details(self):
        try:
            self.tobe=int(self.tobe_deleted_id_entry_delete.get())
            c.execute(f'select Name from Employees where id={self.tobe};')
            for x in c:
                self.name_wants_to_delete=x[0]

            self.answer=deleted(self.name_wants_to_delete)
            if self.answer:
                c.execute(f"delete from Employees where id={self.tobe}")    
                self.tobe_deleted_id_entry_delete.delete(0, 'end')
                c.execute('commit')
                c.reset()
                print("\nDeleted Successfully....")
                
        except TypeError :

            print("Error occurred.... TypeError in delete_details Function")
        except ConnectionError:
            print("\nConnection Error occured...")
        
#view details in the database

    def view_details(self):
        global ans
        ans=[]
        for f in self.treeview.get_children():
                self.treeview.delete(f)
                print(f)

        print("Removing....")

        self.by=self.viewby_combobox_view.get()
        self.value=self.value_entry_view.get()
        if self.by == 'Country':
            self.by='Nationality'

        if self.by == "" and self.value == "":
            c.execute("select * from Employees;")
            for ns in self.treeview.get_children():
                self.treeview.delete(ns)
    

        else:
            #print(f"{self.by}\n{self.value}")
            c.execute(f'select * from Employees where {self.by}="{self.value}"')
            self.treeview.delete(*self.treeview.get_children())
    
        
        for x in c:
            ans.append(x)
                
        n=1

        for x in ans:
            self.treeview.insert('','end',values=tuple(x))
            n= n+1
        print(ans)
        print("\nValue shown Successfully.....\n")
        c.execute('commit;')
        ans.clear()


#Admin login page class


class Admin:
    def __init__(self, master):
        # build ui
        self.admin_username = str()
        self.admin_password=str()
        self.master = master
        self.main_frame_login= tk.Frame(master)
        self.white_frame_main = tk.Frame(self.main_frame_login)
        self.Admin_login_text = ttk.Label(self.white_frame_main)
        self.Admin_login_text.configure(background='white', font='{Timesnew} 14 {bold italic}', text='Admin Login')
        self.Admin_login_text.place(anchor='nw', relx='0.05', rely='0.06', x='0', y='0')

    #Username label and textbox compnents

        self.username_label_main = ttk.Label(self.white_frame_main)
        self.username_label_main.configure(anchor='n', background='white', font='{timenew} 12 {bold italic}', justify='left')
        self.username_label_main.configure(text='Username')
        self.username_label_main.place(anchor='nw', relx='0.02', rely='0.27', x='0', y='0')
        self.username_entry_main = ttk.Entry(self.white_frame_main)
        self.username_entry_main.configure(font='{timesnew} 12 {}')
        self.username_entry_main.place(anchor='nw', relheight='0.07', relwidth='0.65', relx='0.16', rely='0.34', x='0', y='0')

    #Password Lable and textbox components

        self.password_entry_maim = ttk.Entry(self.white_frame_main,show="*")
        self.password_entry_maim.configure(font='{Timesnew} 12 {}')
        self.password_entry_maim.place(anchor='nw', relheight='0.07', relwidth='0.65', relx='0.16', rely='0.55', x='0', y='0')
        self.password_label = ttk.Label(self.white_frame_main)
        self.password_label.configure(background='white', font='{timesnew} 12 {bold italic}', text='Password')
        self.password_label.place(anchor='nw', relx='0.02', rely='0.48', x='0', y='0')


    #Login button congfig

        self.login_button_main = ttk.Button(self.white_frame_main)
        self.login_button_main.configure(text='Log IN')
        self.login_button_main.place(anchor='nw', relx='0.6', rely='0.75', x='0', y='0')
        self.login_button_main.configure(command=self.check_login)
        self.white_frame_main.configure(background='white', height='200', width='200')
        self.white_frame_main.place(anchor='nw', relheight='1.0', relwidth='0.47', relx='0.53', x='0', y='0')



        self.EMS = tk.Label(self.main_frame_login)
        self.EMS.configure(background='#54e8ff', font='{timesnew} 16 {bold italic}', foreground='black', text='Employee Management System')
        self.EMS.place(anchor='nw', relwidth='0.53', relx='0.0', rely='0.06', x='0', y='0')

    #Image label


        self.image_label_main = ttk.Label(self.main_frame_login)
        self.img_index = tk.PhotoImage(file='index.png')
        self.image_label_main.configure(image=self.img_index)
        self.image_label_main.place(anchor='nw', relx='0.112', rely='0.28', x='0', y='0')

    #Main Frame components

        self.main_frame_login.configure(background='#54e8ff', borderwidth='25', height='500', padx='0')
        self.main_frame_login.configure(pady='0', relief='groove', width='750')
        self.main_frame_login.pack(expand='true', fill='both', side='top')
        self.main_frame_login.pack_propagate(0)

        # Main widgetAdmin_lo
        self.mainwindow = self.main_frame_login
    try:

        def run(self):
            self.mainwindow.mainloop()

        def check_login(self):
            self.admin_username=self.username_entry_main.get()
            self.admin_password=self.password_entry_maim.get()
            if(self.admin_username == "Admin") and (self.admin_password == "Admin"):
                showinfo("Info","Logged IN.\t\t\n")
                root = tk.Tk()
                root.title('Main Page')
                root.geometry('750x500')
                app = Main(root)
                self.master.destroy()
                app.run()
            else:
                self.username_entry_main.delete(0,'end')
                self.password_entry_maim.delete(0,'end')
                showwarning("Warning","Incorrect Credentials.\nTry Again")

    except TypeError:
        print("Error Occured")

 #Main
if __name__ == '__main__':
    app1= Admin(main_root)
    app1.run()