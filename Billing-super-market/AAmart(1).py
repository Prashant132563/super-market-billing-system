# IMPORTING PACKAGES#
import mysql.connector as connector
import tkinter
import os
from tkinter import messagebox
import datetime
import random
from PIL import Image, ImageTk
conn = connector.connect(host="localhost",user="root",passwd="nikilreddy@317",database="AAmart")
cursor = conn.cursor()
cursor.execute("select * from items")
data = cursor.fetchall()
root = tkinter.Tk()
root.title("REDDY MART")
root.iconbitmap("icon.ico")
root.state("zoomed")

# For Top Bar
TopBar = tkinter.Frame(root, bg="orange", borderwidth=3, relief="solid",pady=7)
TopBar.pack(side="top",fill='x',pady=7,padx=7)
Bar_Text = tkinter.Label(TopBar, text="Welcome To REDDY MART!!!", bg="orange",font="Algerian 19")
Bar_Text.pack(pady=4)
# Top Bar End !!!!!

# For Background Image
image = Image.open("shop.jpg")
photo = ImageTk.PhotoImage(image)
img_label = tkinter.Label(root,image=photo,borderwidth=4,relief="solid")
img_label.pack(pady=25)
# Background Image End

# PRICE BAR  #
def price_list():
    list_root = tkinter.Toplevel()
    list_root.title("Price List of REDDY MART ")
    list_root.state("zoomed")
    list_root.iconbitmap("price.ico")
    list_root.geometry("1255x625")
# PRICE BAR END #

    # For List_Bar 
    List_Bar = tkinter.Frame(list_root, bg="orange", borderwidth=3, relief="solid",pady=7)
    List_Bar.pack(side="top",fill='x',pady=7,padx=7)
    List_Bar_Text = tkinter.Label(List_Bar, text="Price List of REDDY MART", bg="orange",font="Algerian 19")
    List_Bar_Text.pack(pady=4)
    # List_Bar End
    List_Frame = tkinter.LabelFrame(list_root,text="Price List Menu !!!",bd=3,borderwidth=3,relief="solid",font="Helvetica 12 bold")
    List_Frame.pack(fill="both",padx=12,pady=25,expand="True")
    
    #PRICE LIST BOX#
    list_box = tkinter.Text(List_Frame,bg="#A9A9A9",font="Helvetica 15 bold",bd=3,borderwidth=5,relief='groove')
    scrollbar = tkinter.Scrollbar(list_box,orient="vertical")
    scrollbar.pack(side="right",fill="y")
    list_box.configure(yscrollcommand=scrollbar.set)
    list_box.pack(anchor="nw",expand="True",padx=200,pady=25,fill="both")
    scrollbar.config(command=list_box.yview)
    
    list_box.insert(tkinter.END,"\n\tSno.\t\tProduct Name \t\t\t\t Price\n")

    for i in data:
        Snodata = i[0]
        namedata = i[1]
        pricedata = i[2]
        list_box.insert(tkinter.END,f"\n\n\t{Snodata}.\t\t{namedata} \t\t\t\t {pricedata} Rs\n")
    list_box['state'] = tkinter.DISABLED
    #PRICE LIST BOX END#
    
    # Function to update the price list display
    def refresh_price_list():
        # Clear the current list_box content
        list_box.config(state=tkinter.NORMAL)
        list_box.delete('1.0', tkinter.END)
        list_box.insert(tkinter.END,"\n\tSno.\t\tProduct Name \t\t\t\t Price\n")
        # Fetch updated data from the database
        cursor.execute("select * from items")
        updated_data = cursor.fetchall()
        # Insert updated data into the list_box
        for i in updated_data:
            Snodata = i[0]
            namedata = i[1]
            pricedata = i[2]
            list_box.insert(tkinter.END,f"\n\n\t{Snodata}.\t\t{namedata} \t\t\t\t {pricedata} Rs\n")
        list_box.config(state=tkinter.DISABLED)
    
    # Button to refresh the price list display
    refresh_button = tkinter.Button(List_Frame, text="Refresh", font="Helvetica 10 bold", bg="#FFFACD", bd=3, borderwidth=2, relief="solid", padx=5, pady=10, command=refresh_price_list)
    refresh_button.pack(anchor='center', pady=20, padx=150)
    
    #CREATING THE UPDATE BAR INSIDE THE PROCE MENU LIST#
    def Update():
        Update_root = tkinter.Toplevel()
        Update_root.title("Update Price List ")
        Update_root.state('zoomed')
        Update_root.iconbitmap("update.ico")
        Update_root.geometry("1255x625")
        Update_TopBar = tkinter.Frame(Update_root, bg="orange", borderwidth=3, relief="solid",pady=7)
        Update_TopBar.pack(side="top",fill='x',pady=7,padx=7)
        Update_Bar_Text = tkinter.Label(Update_TopBar, text="Update Price List !!!", bg="orange",font="Algerian 19")
        Update_Bar_Text.pack(pady=4)
    # UPDATE BAR END #
    
        # For Add Items #
        Add_Frame = tkinter.LabelFrame(Update_root,text="Add Items !!! ",bg="#FFFFE0",borderwidth=2,relief="solid",font="Helvetica 12 bold")
        Add_Frame.pack(anchor="nw",expand="True",fill="x",padx=12,pady=25)
        Item_Name_Text = tkinter.Label(Add_Frame,text="Item Name",font="sanserif 12 bold",bg="#FFFFE0",padx=10,pady=5)
        Item_Name_Text.grid(row=0,column=0,padx=5,pady=10)
        def cap_args(*args):
            Item_Entry_var.set(Item_Entry_var.get().title())
        Item_Entry_var = tkinter.StringVar()
        Item_Entry_var.trace('w',cap_args)
        Add_button=tkinter.Button(Add_Frame,text="Add",font="Helvetica 10 bold",bg="#90EE90",bd=3,borderwidth=2,relief="solid",width=12,pady=3)
        Add_button.grid(row=0,column=4,padx=18)
        Item_Entry = tkinter.Entry(Add_Frame,textvariable=Item_Entry_var,font="Helvetica 15",bd=3,borderwidth=2,relief="solid",width=18)
        Item_Entry.focus_set()
        Item_Entry.grid(row=0,column=1,padx=8)

        Price_Text = tkinter.Label(Add_Frame,text="Price",font="sanserif 12 bold",bg="#FFFFE0",padx=10,pady=5)
        Price_Text.grid(row=0,column=2,padx=5,pady=7)
        Price_Entry_var = tkinter.StringVar()
        Price_Entry = tkinter.Entry(Add_Frame,textvariable=Price_Entry_var,font="Helvetica 15",bd=3,borderwidth=2,relief="solid",width=18)
        Price_Entry.grid(row=0,column=3,padx=8)
        def push_items(event=None):
            Item_Name_Data = Item_Entry.get()
            Price_Data = str(Price_Entry.get())
            query = "insert into Items(ProductName,Price) values('{}',{})".format(Item_Name_Data,Price_Data)
            cursor.execute(query)
            conn.commit()
            Item_Entry.delete(0,tkinter.END)
            Price_Entry.delete(0,tkinter.END)
            Item_Entry.focus_set()
            messagebox.showinfo("Item Added ", f"{Item_Name_Data} with {Price_Data} Rs Price Is Added !!!")
        Add_button.configure(command=push_items)
        Price_Entry.bind('<Return>',push_items)
        def go_to_next_entry(event):
            Price_Entry.focus_set() 
        Item_Entry.bind('<Return>', go_to_next_entry)
        #  END OF ADDING ITEMS #
        
        # For Update 
        Update_Frame = tkinter.LabelFrame(Update_root,text="Update Items !!! ",bg="#ADD8E6",borderwidth=2,relief="solid",font="Helvetica 12 bold")
        Update_Frame.pack(anchor="nw",expand="True",fill="x",padx=12,pady=25)
        UpdateItem_Name_Text = tkinter.Label(Update_Frame,text="Item Name",font="sanserif 12 bold",bg="#ADD8E6",padx=10,pady=5)
        UpdateItem_Name_Text.grid(row=0,column=0,padx=5,pady=10)
        def cap_args(*args):
            UpdateItem_Entry_var.set(UpdateItem_Entry_var.get().title())
        UpdateItem_Entry_var = tkinter.StringVar()
        UpdateItem_Entry_var.trace('w',cap_args)
        Update_button=tkinter.Button(Update_Frame,text="Update",font="Helvetica 10 bold",bg="#90EE90",bd=3,borderwidth=2,relief="solid",width=12,pady=3)
        Update_button.grid(row=0,column=4,padx=18)
        UpdateItem_Entry = tkinter.Entry(Update_Frame,textvariable=UpdateItem_Entry_var,font="Helvetica 15",bd=3,borderwidth=2,relief="solid",width=18)
        UpdateItem_Entry.grid(row=0,column=1,padx=8)

        UpdatePrice_Text = tkinter.Label(Update_Frame,text="Set Price",font="sanserif 12 bold",bg="#ADD8E6",padx=10,pady=5)
        UpdatePrice_Text.grid(row=0,column=2,padx=5,pady=7)
        UpdatePrice_Entry_var = tkinter.StringVar()
        UpdatePrice_Entry = tkinter.Entry(Update_Frame,textvariable=UpdatePrice_Entry_var,font="Helvetica 15",bd=3,borderwidth=2,relief="solid",width=18)
        UpdatePrice_Entry.grid(row=0,column=3,padx=8)
        def update_items(event=None):
            UpdateItem_Name_Data = UpdateItem_Entry.get()
            UpdatePrice_Data = str(UpdatePrice_Entry.get())
            query = "Update Items Set Price = {} where ProductName = '{}'".format(UpdatePrice_Data,UpdateItem_Name_Data)
            cursor.execute(query)
            conn.commit()
            UpdateItem_Entry.delete(0,tkinter.END)
            UpdatePrice_Entry.delete(0,tkinter.END)
            UpdateItem_Entry.focus_set()
            messagebox.showinfo("Item Updated ", f"Price Of {UpdateItem_Name_Data} Is Updated To {UpdatePrice_Data} Rs")
        Update_button.configure(command=update_items)
        UpdatePrice_Entry.bind('<Return>',update_items)
        def go_to_next_entry(event):
            UpdatePrice_Entry.focus_set() 
        UpdateItem_Entry.bind('<Return>', go_to_next_entry)
        #  END OF UDATE ITEMS #
        
        # FOR REMOVE ITEM
        Remove_Frame = tkinter.LabelFrame(Update_root,text="Remove Items !!! ",bg="#F75D59",borderwidth=2,relief="solid",font="Helvetica 12 bold")
        Remove_Frame.pack(anchor="nw",expand="True",fill="x",padx=12,pady=25)
        Remove_Item_Name_Text = tkinter.Label(Remove_Frame,text="Item Name",font="sanserif 12 bold",bg="#F75D59",padx=10,pady=5)
        Remove_Item_Name_Text.grid(row=0,column=0,padx=5,pady=10)
        def cap_args(*args):
            Remove_Item_Entry_var.set(Remove_Item_Entry_var.get().title())
        Remove_Item_Entry_var = tkinter.StringVar()
        Remove_Item_Entry_var.trace('w',cap_args)
            
        Remove_button=tkinter.Button(Remove_Frame,text="Remove",font="Helvetica 10 bold",bg="#90EE90",bd=3,borderwidth=2,relief="solid",width=12,pady=3)
        Remove_button.grid(row=0,column=4,padx=18)
        Remove_Item_Entry = tkinter.Entry(Remove_Frame,textvariable=Remove_Item_Entry_var,font="Helvetica 15",bd=3,borderwidth=2,relief="solid",width=18)
        Remove_Item_Entry.grid(row=0,column=1,padx=8)
        def remove_items(event=None):
            cursor.execute("select Count(SNO) from Items;")
            data = cursor.fetchone()
            Remove_Item_Name_Data = Remove_Item_Entry.get()
            query = "delete from Items where ProductName = '{}'".format(Remove_Item_Name_Data)
            cursor.execute(query)
            conn.commit()
            Remove_Item_Entry.delete(0,tkinter.END)
            query2 = "alter table Items Auto_Increment = {}".format(data[0])
            cursor.execute(query2)
            conn.commit()
            messagebox.showinfo("Item Removed ", f"{Remove_Item_Name_Data} Is Removed From Price List !!!")
        Remove_button.configure(command=remove_items)
        Remove_Item_Entry.bind('<Return>',remove_items)

        Update_root.mainloop() 


    Update_items=tkinter.Button(List_Frame,text=" Update Price List !!!",font="Helvetica 10 bold",bg="#FFFACD",bd=3,borderwidth=2,relief="solid",padx=5,pady=10,command=Update)
    Update_items.pack(anchor='center',pady=20,padx=150)

    list_root.mainloop()
#END OF REOMOVE

def bill():
    bill_root = tkinter.Toplevel()
    bill_root.title("Product Bill")
    bill_root.iconbitmap("bill.ico")
    bill_root.state("zoomed")
    
    # For Bill_Bar
    Bill_Bar = tkinter.Frame(bill_root, bg="orange", borderwidth=3, relief="solid",pady=7)
    Bill_Bar.pack(side="top",fill='x',pady=7,padx=7)
    Bill_Bar_Text = tkinter.Label(Bill_Bar, text="Product Bill of REDDY MART !!!", bg="orange",font="Algerian 19")
    Bill_Bar_Text.pack(pady=4)

    # For Customer Details
    Details_Frame = tkinter.LabelFrame(bill_root,bg="#ADD8E6",borderwidth=2,relief="solid",text="Customer Details !!!",font="Helvetica 12 bold")
    Details_Frame.pack(anchor="nw",padx=10,pady=12)

    Name_Label = tkinter.Label(Details_Frame,text="Customer Name",font="sanserif 12 bold",bg="#ADD8E6",padx=10,pady=5)
    Name_Label.grid(row=0,column=0)
    Phone_Label = tkinter.Label(Details_Frame,text="Customer Mobile No.",font="sanserif 12 bold" ,bg="#ADD8E6",padx=10,pady=5)
    Phone_Label.grid(row=0,column=2)
    def cap_args(*args):
        namevalue.set(namevalue.get().title())
    namevalue = tkinter.StringVar()
    namevalue.trace('w',cap_args)
    phonevalue = tkinter.StringVar()
    Name_Entry = tkinter.Entry(Details_Frame,textvariable=namevalue,font="Helvetica 15",bd=3,borderwidth=2,relief="solid",width=18)
    Phone_Entry = tkinter.Entry(Details_Frame,textvariable=phonevalue,font="Helvetica 15",bd=3,borderwidth=2,relief="solid",width=18)
    Name_Entry.grid(row=0,column=1,padx=20,pady=5)
    Phone_Entry.grid(row=0,column=3,padx=20,pady=5)
    Name_Entry.focus_set()
    def go_to_next_entry(event):
        Phone_Entry.focus_set() 
    Name_Entry.bind('<Return>', go_to_next_entry)

         # For Bill Area
    BillBox = tkinter.LabelFrame(bill_root,text="Bill Generator",borderwidth=3,font="Helvetica 12 bold",relief="solid",bd=3)
    BillBox.pack(side="right",anchor="ne",fill='both',padx=15,pady=15,expand="True")
    Bill_Area_Label = tkinter.Label(BillBox,text="Bill Area",font="Algerian 19",borderwidth=5,relief="groove",anchor="center") 
    Bill_Area_Label.pack(fill="x",padx=12)

    Generator_Frame = tkinter.Text(BillBox,bg="#A9A9A9",borderwidth=5,relief="groove",font="sanserif 12 bold")
    scrollbar = tkinter.Scrollbar(Generator_Frame,orient="vertical")
    scrollbar.pack(side="right",fill="y")
    Generator_Frame.configure(yscrollcommand=scrollbar.set)
    Generator_Frame.pack(fill="both",expand="True",padx=12,pady=10)
    scrollbar.config(command=Generator_Frame.yview)

    # For Details in Bill
    Cust_det_button=tkinter.Button(Details_Frame,text="Next",font="Helvetica 10 bold",bg="#90EE90",bd=3,borderwidth=2,relief="solid")
    Cust_det_button.grid(row=0,column=4,padx=12,pady=5)
    def getdetails(event=None):
        # global Phone_Detail
        current_time = datetime.datetime.now()
        Name_Detail = (Name_Entry.get()).title()
        Phone_Detail = Phone_Entry.get()
        
        # Adding validation for mobile number
        if len(Phone_Detail) != 10:
            messagebox.showerror("Invalid Mobile Number", "Mobile number should be exactly 10 digits.")
            return
        global Bill_No
        Bill_No = random.randint(2112,18325)
        Cust_det_button["state"]=tkinter.DISABLED
        Cust_det_button.configure(bg="grey",disabledforeground="black")
        Name_of_Products_Entry.focus_set()
        Generator_Frame.insert(tkinter.END,f"\n   Customer Name   :  {Name_Detail}")
        Generator_Frame.insert(tkinter.END,f"\n   Phone Number    :  {Phone_Detail}")
        Generator_Frame.insert(tkinter.END,f"\n   Purchase Time   :  {current_time}")
        Generator_Frame.insert(tkinter.END,f"\n   Bill Number     :  {Bill_No}")
        Generator_Frame.insert(tkinter.END,"\n\n====================================================================================")
        Generator_Frame.insert(tkinter.END,f"\n\t\tProduct Name\t\t\tQuantity(kgs)\t\t\tPrice")
        Generator_Frame.insert(tkinter.END,"\n====================================================================================")
    Cust_det_button.configure(command=getdetails)
    Phone_Entry.bind('<Return>',getdetails)
    # Customer Details End

    # For Billing Details
    Bill_Details_Frame = tkinter.LabelFrame(bill_root,bg="#CF9FFF",borderwidth=2,relief="solid",text="Billing Details !!!",font="Helvetica 12 bold")
    Bill_Details_Frame.pack(anchor="nw",padx=10,pady=12)
        
    # For Product Name
    Prod_Name_Label = tkinter.Label(Bill_Details_Frame,text="Enter Name Of Products",bg="#CF9FFF",font="Sanserif 12 bold")
    Prod_Name_Label.grid(row=0,column=0)
    def cap_args(*args):
        name_of_products_value.set(name_of_products_value.get().title())
    name_of_products_value = tkinter.StringVar()
    name_of_products_value.trace('w',cap_args)
    Name_of_Products_Entry = tkinter.Entry(Bill_Details_Frame,textvariable=name_of_products_value,font="Helvetica 15",bd=3,borderwidth=2,relief="solid",width=18)
    Name_of_Products_Entry.grid(row=0,column=1,padx=20,pady=5)
    def getProdName():
        ProductData= Name_of_Products_Entry.get()
        Qty_Entry.focus_set()
        return(ProductData)
    name_op_button=tkinter.Button(Bill_Details_Frame,text="Next",font="Helvetica 10 bold",bg="#90EE90",bd=3,borderwidth=2,relief="solid",command=getProdName)
    name_op_button.grid(row=0,column=2,padx=7,pady=5)
    
    # For No of Products
    Qty_Label = tkinter.Label(Bill_Details_Frame,text="Enter Quantity(kg)                  ",bg="#CF9FFF",font="Sanserif 12 bold")
    Qty_Label.grid(row=1,column=0)
    Qty_value = tkinter.StringVar()
    Qty_Entry = tkinter.Entry(Bill_Details_Frame,textvariable=Qty_value,font="Helvetica 15",bd=3,borderwidth=2,relief="solid",width=18)
    Qty_Entry.grid(row=1,column=1,padx=20,pady=5)

    def go_to_next_entry(event):
        Qty_Entry.focus_set() # focus_set() switches the focus to the new widget
    Name_of_Products_Entry.bind('<Return>', go_to_next_entry)
    Total_Label = tkinter.Label(Bill_Details_Frame,text="Total\t\t",bg="#CF9FFF",font="Sanserif 12 bold")
    Total_Label.grid(row=2,column=0)
    Total_value = tkinter.StringVar()
    Total_Entry = tkinter.Entry(Bill_Details_Frame,textvariable=Total_value,font="Helvetica 15",bd=3,borderwidth=2,relief="solid",width=18)
    Total_Entry.grid(row=2,column=1,padx=20,pady=5)

    #  No of Product End
    total_button=tkinter.Button(Bill_Details_Frame,text="Total",font="Helvetica 10 bold",bg="#F75D59",bd=3,borderwidth=2,relief="solid")
    total_button.grid(row=2,column=2,padx=7,pady=5)
    logo_photo = Image.open("logo.png")
    logo_photo = logo_photo.resize((250,200))
    photo_Image = ImageTk.PhotoImage(logo_photo)
    logo = tkinter.Label(bill_root,image=photo_Image,anchor="center")
    logo.pack(fill="x",anchor='nw',expand="True")
    Bill_Button_Frame = tkinter.LabelFrame(bill_root,text="Action Buttons",border=3,bg="#FFB6C1",borderwidth=2,relief="solid",font="Helvetiva 12 bold")
    Bill_Button_Frame.pack(anchor='nw',padx=10,pady=17,expand="True",fill="both")

    Bill_Button = tkinter.Button(Bill_Button_Frame,text="Generate Bill !!!",bg="#90EE90",bd=5,borderwidth=4,relief="groove",width=13,pady=12,activebackground="#ff9248",font="Helvetica 11 bold")
    Bill_Button.pack(side="left",padx=20)
    Save_Button = tkinter.Button(Bill_Button_Frame,text="Save Bill !!!",bg="#90EE90",bd=5,borderwidth=4,relief="groove",width=13,pady=12,activebackground="#ff9248",font="Helvetica 11 bold")
    Save_Button.pack(side="left",anchor="center",padx=(10,0))
    l = []
    def getvals(event = None):
        ProductData= (getProdName()).title()
        qty = int(Qty_Entry.get())  
        Name_of_Products_Entry.delete(0,tkinter.END)
        Qty_Entry.delete(0,tkinter.END)
        Name_of_Products_Entry.focus_set()
        for i in data:
            if i[1].lower() == ProductData.lower():
                PriceData = i[2]
                price= PriceData*qty
                Generator_Frame.insert(tkinter.END,f"\n\t\t{ProductData}\t\t\t{qty}\t\t\t{price} Rs")
                l.append(price)
                def getotal():
                    total = sum(l)
                    Total_Entry.delete(0,tkinter.END)
                    Total_Entry.insert(0,f"{total} Rs")
                    def generate_bill():
                        Generator_Frame.insert(tkinter.END,"\n\n\n\n====================================================================================")
                        Generator_Frame.insert(tkinter.END,f"\n\t\t\t\t      Total : {total} Rs")
                        Generator_Frame.insert(tkinter.END,"\n====================================================================================")
                        Generator_Frame.insert(tkinter.END,"\n\n\t\t\t\tThanks For Visiting Us !!")
                   
                    Bill_Button.configure(command=generate_bill)
                total_button.configure(command=getotal)

    nof_button=tkinter.Button(Bill_Details_Frame,text="Next",font="Helvetica 10 bold",bg="#90EE90",bd=3,borderwidth=2,relief="solid",command=getvals)
    nof_button.grid(row=1,column=2,padx=7,pady=5)
    Qty_Entry.bind('<Return>',getvals)
    if not os.path.exists('Bills'):
        os.mkdir('Bills')
    def save():
        Bill_data = Generator_Frame.get(1.0,tkinter.END)
        file = open(f"Bills/{Bill_No}.txt",'w')
        file.write(Bill_data)
        messagebox.showinfo("Bill Saved", f"Your Bill With Bill No. {Bill_No} Is Saved In Bills Folder") 
    Save_Button.configure(command=save)
    def clear():
        Generator_Frame.delete("1.0",tkinter.END)
        Cust_det_button.config(text="Next",font="Helvetica 10 bold",bg="#90EE90",bd=3,borderwidth=2,relief="solid")
        Cust_det_button["state"]=tkinter.NORMAL
        Name_Entry.delete(0,tkinter.END)
        Phone_Entry.delete(0,tkinter.END)
        Total_Entry.delete(0,tkinter.END)
        Name_Entry.focus_set()
        l.clear()
    
    Clear_Button = tkinter.Button(Bill_Button_Frame,text="Clear Bill !!!",bg="#90EE90",bd=5,borderwidth=4,relief="groove",width=13,pady=12,activebackground="#ff9248",font="Helvetica 11 bold",command=clear)
    Clear_Button.pack(side="right",padx=20)

    bill_root.mainloop()

# For Button Label
f2 = tkinter.Frame(root)
f2.pack(side="bottom",fill="x",pady=12)
b1 = tkinter.Button(f2,text="Price List !!!", bg="#90EE90",borderwidth=3,padx=15,pady=16,relief="solid",font="Helvetica 10 bold",command=price_list)
b1.pack(side="left",padx=260,pady=60)
b2 = tkinter.Button(f2,text="Create Bill !!!", bg="#FFD580",borderwidth=3,padx=10,pady=16,relief="solid",font="Helvetica 10 bold",command=bill)
b2.pack(side="right",padx=260,pady=60)

root.mainloop()