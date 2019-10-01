#all of these need inputs



#better to set this in the environment (computer) fixed permanentlyset path=% path %;C:\temp\mysqlsetup\mysql-8.0.17-winx64\bin

import tkinter as tk
from tkinter import ttk
import os
import sys

dos_command=''

def show_entry_fields():
    global var_out_feedback
    global var_sqldump_file
    global var_database
    global var_host
    global var_port
    global var_username
    global var_password
    global dos_command

    dos_command=f'mysqldump --host={var_host.get()} --port={var_port.get()} --user={var_username.get()} --password={var_password.get()} --force --databases {var_database.get()} --lock-all-tables=FALSE --add-drop-table --result-file={var_output_folder.get()}baseline_{var_database.get()}.sql --log-error=mysql_error_{var_database.get()}.txt --skip-column-statistics --no-data --skip-quote-names --skip-add-drop-table  --no-data=true --dump-date --routines=false --no-create-db=TRUE'


    print("Host and port :", var_host.get(), var_port.get())
    print("Login credentials:",var_username.get(),"secret password")
    print("database selected:",var_database.get())
    print("dos command:",dos_command)

    # e1.delete(0, tk.END)
    # e2.delete(0, tk.END)

def call_dos_mysqldump():
    global var_out_feedback
    global var_sqldump_file
    global var_database
    global var_host
    global var_port
    global var_username
    global var_password
    global wg_out_message
    global var_mysql_path
    global var_output_folder

    #it should be automatically setnt to var_database comboDomains.get()

    dos_command=f'mysqldump.exe --host={var_host.get()} --port={var_port.get()} --user={var_username.get()} --password={var_password.get()} --force --databases {var_database.get()} --lock-all-tables=FALSE --result-file={var_output_folder.get()}baseline_{var_database.get()}.sql --log-error=mysql_error_{var_database.get()}.txt --skip-column-statistics --no-data --skip-quote-names --skip-add-drop-table --skip-quote-names --no-data=true --dump-date --routines=false --no-create-db=TRUE'
    print(dos_command)

    var_out_feedback.set("Running mysqldump")
    var_sqldump_file.set("")
    wg_out_message.configure(background='yellow')
    wg_sqldump_result.delete(1.0, tk.END)

    try:
        os.chdir(f'{var_mysql_path.get()}')
        print('Folder for mysql is valid')

        returnvalue=os.system(dos_command)
        print('reach this point(a)')
        vfile = open(f'{var_output_folder.get()}baseline_{var_database.get()}.sql', 'r')
        v_file_contents = vfile.read()
        var_sqldump_file.set(v_file_contents)
        wg_sqldump_result.insert(tk.END,v_file_contents)
        xlen = len(v_file_contents)
        if xlen >= 1280:
            var_out_feedback.set("OK:Valid database and file generated successfully")
            wg_out_message.configure(background='green')
        else:
            var_out_feedback.set("ERROR:File not generated successfully, please check settings and try again")
            wg_out_message.configure(background='red')

    except OSError as err:
        print("OS error: {0}".format(err))
        var_out_feedback.set("OS error: {0}".format(err))
        print("OS error: {0}".format(err))
        print('reach this point(B)')
    except:
        print("Unexpected error running Mysqldump.exe:", sys.exc_info()[0])
        var_out_feedback.set("Unexpected error running Mysqldump.exe:")
        raise





# def clear_message():
#     global var_out_feedback
#     var_out_feedback.set('')

window=tk.Tk()
window.geometry("1300x800+100+100")
vmycellsize="                       "
tk.Label(window, text=vmycellsize).grid(row=0,column=1)
tk.Label(window, text=vmycellsize).grid(row=0,column=2)
tk.Label(window, text=vmycellsize).grid(row=0,column=3)
tk.Label(window, text=vmycellsize).grid(row=0,column=4)
tk.Label(window, text=vmycellsize).grid(row=0,column=5)
tk.Label(window, text=vmycellsize).grid(row=0,column=6)
tk.Label(window, text=vmycellsize).grid(row=0,column=7)
tk.Label(window, text=vmycellsize).grid(row=0,column=8)

window.winfo_toplevel().title("PYMYSQLDUMP-Export schema for Aurora MYSQL database")

vStaticInstructions="INSTRUCTIONS:\nSet the variables to match the configuration of the computer running the software \n Pick your database and enter login credentials"


tk.Label(window, text="Host").grid(row=2)
tk.Label(window, text="Port").grid(row=3)
tk.Label(window, text="Username").grid(row=4)
tk.Label(window, text="Password").grid(row=5)
tk.Label(window, text="Database").grid(row=6)

tk.Label(window, text="Mysql.exe path").grid(row=7)
tk.Label(window, text="Output Folder:").grid(row=8)


var_database=tk.StringVar()  # Holds a string; default value ''
var_host=tk.StringVar()  # Holds a string; default value ''
var_port=tk.IntVar()  # Holds an int; default value 0
var_username=tk.StringVar()  # Holds a string; default value ''
var_password=tk.StringVar()  # Holds a string; default value ''
#var_classpath=tk.StringVar()  # Holds a string; default value ''
var_out_feedback=tk.StringVar()
var_sqldump_file=tk.StringVar()
var_mysql_path=tk.StringVar()
var_output_folder=tk.StringVar()

def set_direct_default():
    var_host.set("bwp-gms-dev-aurora-0.cztswafip9oo.us-east-1.rds.amazonaws.com")
    var_port.set(3306)
    var_username.set("admin")
    var_password.set("MoosoBFWZ8BScw") #passwords must be provided by user
    var_database.set("accounting")  # this can be a dropbox
    var_out_feedback.set("Results coming up...")
    var_sqldump_file.set("File not generated yet")
    var_mysql_path.set("C:\\Program Files\\MySQL\\MySQL Workbench 8.0 CE")
    var_output_folder.set("C:\\temp\\")

def set_local_putty_default():
    var_host.set("127.0.0.1")
    var_port.set(3308)
    var_username.set("admin")
    var_password.set("MoosoBFWZ8BScw") #passwords must be provided by user
    var_database.set("accounting")  # this can be a dropbox
    var_out_feedback.set("Results coming up...")
    var_sqldump_file.set("File not generated yet")
    var_mysql_path.set("C:\\temp\\mysqlsetup\\mysql-8.0.17-winx64\\bin")
    var_output_folder.set("C:\\temp\\")


textscrollbar = tk.Scrollbar(window)

#"C:\Users--ramons\.DataGrip2019.1\config\jdbc-drivers\MySQL Connector\J 8\8.0.15\mysql-connector-java-8.0.15.jar")

#PENDING NO INPUT NEEDED- var_changeLogFile.set(="C:\liquibase_baseline\%database%\\baseline\\views.yaml")
#PENDING NO INPUT NEEDED-var_output_file.set("liqui_results_baseline%database%.txt")
#PENDING NO INPUT NEEDED var_url.set("jdbc:mysql://localhost:**PORT HERE**/bwpgmsdefault")


#input_host=tk.Entry(window,textvariable=var_host)
input_port=tk.Entry(window,textvariable=var_port)
input_username=tk.Entry(window,textvariable=var_username)
input_password=tk.Entry(window,textvariable=var_password,show="*")
input_path_exe=tk.Entry(window,textvariable=var_mysql_path,width=100)
input_out_folder=tk.Entry(window,textvariable=var_output_folder,width=100)
#input_path_exe=tk.Entry(window,textvariable=var_classpath)

wg_static1_msg=tk.Message(window, text=vStaticInstructions, width=600, relief='sunken')
wg_sqldump_result=tk.Text(window,background="grey90") #, textvariable=var_sqldump_file) #, text='Status goes here', width=800, relief='sunken',textvariable=var_sqldump_file) #7
wg_out_message=tk.Message(window, text='Initial test', width=800, relief='sunken',textvariable=var_out_feedback) #7

#This could be enhanced by loading all the domains after reading the metadata
comboDomains=ttk.Combobox(window,values=["accounting","billing",  "contract", "pipelinemodel","entity","location","nomination","rates","rfs"],textvariable=var_database,width=60)
comboHost=ttk.Combobox(window,values=["bwp-gms-dev-aurora-0.cztswafip9oo.us-east-1.rds.amazonaws.com","bwp-gms-dev-aurora-dwtestbed-temp.cztswafip9oo.us-east-1.rds.amazonaws.com","127.0.0.1"],textvariable=var_host,width=60)

# e1.insert(10, "Miller")
# e2.insert(10, "Jill")

wg_static1_msg.grid(row=0,column=0 ,columnspan=7,sticky=tk.W) #The columnspan is important because it makes it very wide.
comboHost.grid(row=2, column=1,sticky=tk.W)
input_port.grid(row=3, column=1,sticky=tk.W)
input_username.grid(row=4, column=1,sticky=tk.W)
input_password.grid(row=5, column=1,sticky=tk.W)
comboDomains.grid(row=6,column=1,sticky=tk.W) #Database is line$3

input_path_exe.grid(row=7, column=1,columnspan=4,sticky=tk.W)
input_out_folder.grid(row=8, column=1,columnspan=4,sticky=tk.W)

#FRAME FOR BUTTON

fr_button=tk.Frame(window)

tk.Button(window, text='Call MysqlDump.exe', command=call_dos_mysqldump).grid(row=1,column=7,sticky=tk.W, pady=4)
tk.Button(window, text='Set local defaults', command=set_local_putty_default).grid(row=2,column=7,sticky=tk.W, pady=4)
tk.Button(window, text='Set server defaults', command=set_direct_default).grid(row=3,column=7,sticky=tk.W, pady=4)
tk.Button(window, text='Quit',command=window.quit).grid(row=5, column=7, sticky=tk.W, pady=4)

tk.Label(window, text="                         ").grid(row=10)
tk.Label(window, text="                         ").grid(row=11)

wg_out_message.grid(row=12,column=0 ,columnspan=4,sticky=tk.W) #The columnspan is important because it makes it very wide.
wg_sqldump_result.grid(row=13,column=0 ,columnspan=8,sticky=tk.W) #The columnspan is important because it makes it very wide.

textscrollbar.config(command=wg_sqldump_result.yview)

wg_sqldump_result.insert(tk.END,"MYSQL dump flat file preview will be displayed here")
wg_sqldump_result.config(yscrollcommand=textscrollbar.set)


set_direct_default()
window.mainloop()

