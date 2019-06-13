# -*- coding: utf-8 -*-
"""
Created on Tue May  1 08:29:18 2018

@author: kemal
"""
from ItineraryList import ItineraryList
from AirportAtlas import AirportAtlas
from tkinter import *
import csv


class mainGUI:
    
    def __init__(self,root):
        
        frame=Frame(root,bg='#7A0F0F')
        root.geometry("850x550")
        frame.pack(expand=YES,fill=BOTH)

        
        self.label_1=Label(root,text="Home Airport",bg='#7A0F0F',fg='white',font='Helvetica 10 bold')
        self.label_2=Label(root,text="Airport 1",bg='#7A0F0F',fg='white',font='Helvetica 10 bold')
        self.label_3=Label(root,text="Airport 2",bg='#7A0F0F',fg='white',font='Helvetica 10 bold')
        self.label_4=Label(root,text="Airport 3",bg='#7A0F0F',fg='white',font='Helvetica 10 bold')
        self.label_5=Label(root,text="Airport 4",bg='#7A0F0F',fg='white',font='Helvetica 10 bold')
        self.label_6=Label(root,text="--FUEL OPT--",bg='#7A0F0F',fg='white',font='Helvetica 40 bold')
        self.label_7=Label(root,text="Aircraft",bg='#7A0F0F',fg='white',font='Helvetica 10 bold')
        self.entry_1=Entry(root) 
        self.entry_2=Entry(root)
        self.entry_3=Entry(root)
        self.entry_4=Entry(root)
        self.entry_5=Entry(root)
        
        self.label_1.place(x=24,y=100)
        self.label_2.place(x=42,y=140)
        self.label_3.place(x=42,y=180)
        self.label_4.place(x=42,y=220)
        self.label_5.place(x=42,y=260)
        self.label_6.place(x=250,y=20)
        self.label_7.place(x=212,y=100)
        
        self.entry_1.place(x=10,y=120)
        self.entry_2.place(x=10,y=160)
        self.entry_3.place(x=10,y=200)
        self.entry_4.place(x=10,y=240)
        self.entry_5.place(x=10,y=280)
        
        picture=PhotoImage(file='pic.png')
        label_pic=Label(image=picture,bg='#7A0F0F')
        label_pic.place(x=370,y=420)
        label_pic.image=picture
        
        self.listbox=Listbox(root,width=20, height=16)
        
        info_board_frame = Frame(root)
        info_board_frame.place(x=350, y=120)

        scrollbar = Scrollbar(info_board_frame,orient=VERTICAL)
        scrollbar.pack(side=RIGHT, fill=Y)
        
        self.info_board = Text(info_board_frame, width=60, height=16, wrap=WORD, font=('arial',10), bg='#D0CBCA')
        self.info_board.pack()
        self.info_board.insert(END, '-----WELCOME TO AIRCRAFT FUEL OPTIMIZATION PROBLEM-----\n\nPLEASE INPUT HOME AIRPORT, FOUR STOPS THAT YOU WISH TO TRAVEL AND THE AIRCRAFT TYPE ON TO THE ENTRY BOXES LOCATED LEFT HAND-SIDE')

        self.info_board.config(yscrollcommand = scrollbar.set)
        scrollbar.config(command = self.info_board.yview)
        
        for aircraft in ["A319" ,"A320", "A321", "A330", "737", "747", "757", "767", "777", "BAE146", "DC8", "F50", "MD11", "A400M", "C212", "V22"]:
            self.listbox.insert(END, aircraft)
        self.listbox.place(x=177,y=120)
        
        
        
        
        self.write=Button(frame, text="Submit Airports & Aircraft", command=self.addToListandDisplay)
        self.write.place(x=80,y=410)
        
        self.write=Button(frame, text="Write to a CSV file", command=self.writeToCsv)
        self.write.place(x=101,y=450)
        
 
    def addToListandDisplay(self):
        
        try:
            airport=AirportAtlas('airport.csv')
        except FileNotFoundError:
            messagebox.showinfo("Loading error airport.csv file", "Unable to load 'airport.csv' file please make sure this file and airport.csv located on the same file and filename is 'airport.csv'")
            
        Data=[]
        
        Data.append(self.entry_1.get().upper())#gets all the inputs from the user makes them capital if not and appends them to a list
        
        try: #checks whether the IATA code is valid by sending code to airport class and try to get a result
            where=airport.getAirportCountry(Data[0])
        except:
            messagebox.showinfo("Invalid IATA code", "Home airport is not valid IATA code please enter one that exists")
        
        Data.append(self.entry_2.get().upper())
        
        try: #checks whether the IATA code is valid by sending code to airport class and try to get a result
            where=airport.getAirportCountry(Data[1])
        except:
            messagebox.showinfo("Invalid IATA code", "Airport 1 is not valid IATA code please enter one that exists")
        
        Data.append(self.entry_3.get().upper())
        
        try: #checks whether the IATA code is valid by sending code to airport class and try to get a result
            where=airport.getAirportCountry(Data[2])
        except:
            messagebox.showinfo("Invalid IATA code", "Airport 2 is not valid IATA code please enter one that exists")
        
        Data.append(self.entry_4.get().upper())
        
        try: #checks whether the IATA code is valid by sending code to airport class and try to get a result
            where=airport.getAirportCountry(Data[3])
        except:
            messagebox.showinfo("Invalid IATA code", "Airport 3 is not valid IATA code please enter one that exists")
        
        Data.append(self.entry_5.get().upper())
        
        try: #checks whether the IATA code is valid by sending code to airport class and try to get a result
            where=airport.getAirportCountry(Data[4])
        except:
            messagebox.showinfo("Invalid IATA code", "Airport 4 is not valid IATA code please enter one that exists")
        
        try:
            Data.append(self.listbox.get(self.listbox.curselection()[0]))
        except:
            messagebox.showinfo("Select an aircraft", "You haven't selected an aircraft please click one")
        
        
        obj=ItineraryList(Data) #sends all the airports and aircraft to ItineraryList for shortest and cheapest route calculation
        
        cheapestroutelist=obj.getCheapestRouteList()
        mincost=obj.getMinCost()
        cheapestroutedist=obj.getCheapestRouteDist()
        shortestroutelist=obj.getShortestRouteList()
        shortestroutecost=obj.getShortestRouteCost()
        shortestroutedist=obj.getShortestRouteDist()
        usedaircraft=obj.getAircraft()
        
        if cheapestroutedist==shortestroutedist: #if shortest and cheapest are same
            
            self.info_board.delete(1.0,END)
            self.info_board.insert(1.0, '-----CHEAPEST ROUTE INFO-----')
            self.info_board.insert(2.0, ('\n'))
            self.info_board.insert(3.0, 'Cheapest Route : ')
            self.info_board.insert(4.0, cheapestroutelist, )
            self.info_board.insert(5.0, ('\n'))
            self.info_board.insert(6.0, 'Cost of the cheapest route : ')
            self.info_board.insert(7.0,round(mincost,2))
            self.info_board.insert(7.0, ' euros\n')
            if mincost==0:
                self.info_board.insert(8.0, 'Chosen aircraft can complete this route without refuelling\n')
            self.info_board.insert(8.0, 'Cheapest Route Distance: ')
            self.info_board.insert(9.0, round(cheapestroutedist,2))
            self.info_board.insert(9.0, ' km\n')
            self.info_board.insert(10.0, ('----------------------------'))
            self.info_board.insert(10.0, ('\n'))
            self.info_board.insert(11.0,('Cheapest route is also the shortest route'))
            self.info_board.insert(11.0, ('\n'))
            self.info_board.insert(12.0, 'Equipment used : ')
            self.info_board.insert(12.0, usedaircraft)
            
        elif shortestroutecost>0: #if shortest and cheapest are different from eachoter and there is a valid shortest
            
            self.info_board.delete(1.0,END)
            self.info_board.insert(1.0, '-----CHEAPEST ROUTE INFO-----')
            self.info_board.insert(2.0, ('\n'))
            self.info_board.insert(3.0, 'Cheapest Route : ')
            self.info_board.insert(4.0, cheapestroutelist, )
            self.info_board.insert(5.0, ('\n'))
            self.info_board.insert(6.0, 'Cost of the cheapest route : ')
            self.info_board.insert(7.0,round(mincost,2))
            self.info_board.insert(7.0, ' euros\n')
            if mincost==0:
                self.info_board.insert(8.0, 'Chosen aircraft can complete this route without refuelling\n')
            self.info_board.insert(8.0, 'Cheapest Route Distance: ')
            self.info_board.insert(9.0, round(cheapestroutedist,2))
            self.info_board.insert(9.0, ' km\n')
            self.info_board.insert(10.0, ('----------------------------'))
            self.info_board.insert(10.0, ('\n\n\n'))
            self.info_board.insert(11.0, '-----SHORTEST ROUTE INFO-----')
            self.info_board.insert(12.0, ('\n'))
            self.info_board.insert(13.0, 'Shortest Route : ')
            self.info_board.insert(14.0, shortestroutelist, )
            self.info_board.insert(15.0, ('\n'))
            self.info_board.insert(16.0, 'Cost of the shortest route : ')
            self.info_board.insert(17.0,round(shortestroutecost,2))
            self.info_board.insert(17.0, ' euros\n')
            if shortestroutecost==0:
                self.info_board.insert(8.0, 'Chosen aircraft can complete this route without refuelling\n')
            self.info_board.insert(18.0, 'Shortest Route Distance: ')
            self.info_board.insert(19.0, round(shortestroutedist,2))
            self.info_board.insert(19.0, ' km\n')
            self.info_board.insert(20.0, ('----------------------------'))
            self.info_board.insert(20.0, ('\n'))
            self.info_board.insert(21.0, 'Equipment used : ')
            self.info_board.insert(21.0, usedaircraft)
            
        else: #shortest and cheapest are same but shortest is not valid
            
            self.info_board.delete(1.0,END)
            self.info_board.insert(1.0, '-----CHEAPEST ROUTE INFO-----')
            self.info_board.insert(2.0, ('\n'))
            self.info_board.insert(3.0, 'Cheapest Route : ')
            self.info_board.insert(4.0, cheapestroutelist, )
            self.info_board.insert(5.0, ('\n'))
            self.info_board.insert(6.0, 'Cost of the cheapest route : ')
            self.info_board.insert(7.0,round(mincost,2))
            self.info_board.insert(7.0, ' euros\n')
            if mincost==0:
                self.info_board.insert(8.0, 'Chosen aircraft can complete this route without refuelling\n')
            self.info_board.insert(8.0, 'Cheapest Route Distance : ')
            self.info_board.insert(9.0, round(cheapestroutedist,2))
            self.info_board.insert(9.0, ' km\n')
            self.info_board.insert(10.0, ('----------------------------'))
            self.info_board.insert(11.0, ('\n'))
            self.info_board.insert(12.0, 'Equipment used : ')
            self.info_board.insert(12.0, usedaircraft)
      
    def writeToCsv(self):
        listt=[]
        try:
            airport=AirportAtlas('airport.csv') #try to open airport csv and pops out a message box unless opens
        except FileNotFoundError:
            messagebox.showinfo("Loading error airport.csv file", "Unable to load 'airport.csv' file please make sure this file and airport.csv located on the same file and filename is 'airport.csv'")
            
        Data=[]
        
        Data.append(self.entry_1.get().upper())#gets all the inputs from the user makes them capital if not and appends them to a list
        
        try: #checks whether the IATA code is valid by sending code to airport class and try to get a result
            where=airport.getAirportCountry(Data[0])
        except:
            messagebox.showinfo("Invalid IATA code", "Home airport is not valid IATA code please enter one that exists")
        
        Data.append(self.entry_2.get().upper())
        
        try: #checks whether the IATA code is valid by sending code to airport class and try to get a result
            where=airport.getAirportCountry(Data[1])
        except:
            messagebox.showinfo("Invalid IATA code", "Airport 1 is not valid IATA code please enter one that exists")
        
        Data.append(self.entry_3.get().upper())
        
        try: #checks whether the IATA code is valid by sending code to airport class and try to get a result
            where=airport.getAirportCountry(Data[2])
        except:
            messagebox.showinfo("Invalid IATA code", "Airport 2 is not valid IATA code please enter one that exists")
        
        Data.append(self.entry_4.get().upper())
        
        try: #checks whether the IATA code is valid by sending code to airport class and try to get a result
            where=airport.getAirportCountry(Data[3])
        except:
            messagebox.showinfo("Invalid IATA code", "Airport 3 is not valid IATA code please enter one that exists")
        
        Data.append(self.entry_5.get().upper())
        
        try: #checks whether the IATA code is valid by sending code to airport class and try to get a result
            where=airport.getAirportCountry(Data[4])
        except:
            messagebox.showinfo("Invalid IATA code", "Airport 4 is not valid IATA code please enter one that exists")
        
        try:
            Data.append(self.listbox.get(self.listbox.curselection()[0]))
        except:
            messagebox.showinfo("Select an aircraft", "You haven't selected an aircraft please click one")
        
        
        obj=ItineraryList(Data) #sends all the airports and aircraft to ItineraryList for shortest and cheapest route calculation
        
        cheapestroutelist=obj.getCheapestRouteList()
        mincost=obj.getMinCost()
        cheapestroutedist=obj.getCheapestRouteDist()
        usedaircraft=obj.getAircraft()
        
        listt = [['-----CHEAPEST ROUTE INFO-----'],
        [cheapestroutelist],
        ['Cost of the cheapest route : '],
        [mincost],
        ['Cheapest Route Distance : '],
        [cheapestroutedist],
        ['Equipment used : '],
        [usedaircraft]]
        
        with open('bestroute.csv','w') as file:
            
            writer=csv.writer(file)
            
            for row in listt:
                writer.writerow(row)
        
def main():
       
    root=Tk()
    objectGUI=mainGUI(root) 
    root.mainloop()
    

main()







        
    

