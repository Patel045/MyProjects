from tkinter import *
from tkinter import colorchooser
#from PIL import ImageTk, Image
from tkinter import messagebox

#Some Global Variables
bgcolour="#cdf8f7"
bgcolourlight="#f2ffff"
colour=["pink","light grey","yellow","sky blue"]

#Text Variables for Blocks
s_text="""
GENERAL INFORMATION ABOUT THE S-BLOCK\n\n
1. The S-block name is taken because the elements that are put under s block their last electron
   is present in the furthest S orbital.
2. The elements in the S block consists of alkali metals and alkali earth metals.
3. The block contains 2 groups,that are  group no.1 and 2.
6. The S block is placed towards the extreme left of the modern periodic table\n
GENERAL INFORMATION ABOUT GROUP 1
1. Group 1 consist of 6 metallic elements these elements are called alkali metals because they readily
   dissolve in water to form soluble hydroxides, which are strongly alkaline in nature.
2. The alkali metals are strong reducing agents .
3. Atomic and ionic radii of alkali metals increase on moving down the group.
4. These element exhibit ionic nature\n
GENERAL INFORMATION ABOUT GROUP 2
1. Group 2 consist of 6 elements also known as Alkali Earth metals.
2. Atomic and ionic radii of alkaline earth metals are comparatively smaller than alkali metals and
   increases down the group. 
3. These metals also have low ionization enthalpies due to fairly large size of atoms.
4. These elements exhibit ionic nature.
"""
p_text="""
GENERAL INFORMATION ABOUT THE P-BLOCK\n\n
1. The P-block name is taken because in the elements that are put under p block the
   because the last electron is present in the furthest P orbital.
2. The elements in the P block consists of metals,non-metal and metalliods.
3. The block contains 6 groups,that are from group no.13 to 18.(including both)
4. The general valance shell configration varies from ns2 np1 to ns2np6 where 
   n is natural number.
5. helium is the exception to the above valance shell configration 
6-P block is placed towards the extreme right of th modern periodic table\n
GENERAL INFORMATION ABOUT GROUP 13
1. Group 13 consist of 6(considering Nh) metallic elements this group is also
   known as boron family.
2. The traditional periodic table's group 13 had only 5 elements however
   a new synthetic element nhonium is added to the period table with the atomic
   number 113 replacing Uut.
3. All of them except Nh exhibit covalent nature.\n
GENERAL INFORMATION ABOUT GROUP 14
1. Group 14 consist of 6(considering Fl) elements also known as Carbon family.
2. flerovium (Fl) is the latest addition to the group 14 its a synthetic 
   highly radioactive element with atomic number 114.
3. The covalent nature is best examined in C followed by Si then Ge after 
   them ionic nature is observed in Sn and Pb\n
GENERAL INFORMATION ABOUT GROUP 15
1. Group 15 consist of 5 elements this group is also known as nitrogen family.
2. Moving down the group, the ionic radii, and atomic radii increases.
3. The electro negativity diminishes bit by bit on moving down the group because
   of the increase in atomic radius.\n
GENERAL INFORMATION ABOUT GROUP 16
1. Group 16 consist of 5 elements this group is also known as oxygen family.
2. The atomic and ionic radius increasesas we move from oxygen to polonium.
3. There is a progressive decline in electro negativity as we move down the group
   Oxygen is the sencond most electronegative element in periodic table.\n
GENERAL INFORMATION ABOUT GROUP 17
1. Group 17 consist of 5 elements this group is also known as Halogen family.
2. Astatine is radioactive in nature (atomic no.85) and is also synthetic element.
3. As we move down the group, the nuclear radii, and ionic radii increases.
4. These elements demonstrate high estimations of ionization enthalpy.\n
GENERAL INFORMATION ABOUT GROUP 18
1. Group 18 consist of 6 elements this group is also known as Noble Gases.
2. They are non reactive in nature.
3. They have zero tendencies to accept any electron. Consequently, they have high 
   positive values of electron gain enthalpy.
4. Due to their closed electronic configurations they have high ionization potentials.
"""
d_text="""
GENERAL INFORMATION ABOUT THE D-BLOCK\n\n
1. The D-block name is taken because the valance D orbital of the elements are progressively filled.
2. The elements in the D block consists of transition metals
3. The block contains 10 groups,that are from group no.3 to 12.(including both)
4. There are three transition series each of 10 elements in the D block.
5. There are mainly three series of the elements, 3d-series (Sc to Zn) 4d-series (Y to Cd) and 5d-series
   (La to Hg omitting Ce to Lu). The fourth 6d-series which begins with Ac is still incomplete.
6. D block is placed in the centre of the modern periodic table. Between S block and P block\n\n
GENERAL INFORMATION ABOUT 3d transition series.
1. It involves filling of 3d-orbitals. It starts from scandium (Z = 21) and goes upto zinc (Z = 30). 
2. Atomic and ionic size decreases while moving left to right .However the last transition element is
   bigger in size due to electron repulsion in the fully filled d orbital.
3. The electronegativity increases while moving left to right in the series.\n\n
GENERAL INFORMATION ABOUT 4d transition series
1. 4d – transition series. It consists of elements with atomic number 39(Y) to 48 (Cd) and having
   incomplete 4d orbitals. It is called second transition series.
2. Atomic and ionic size decreases while moving left to right .However the last transition element is
   bigger in size due to electron repulsion in the fully filled d orbital. 
3. Due to higher oxidation of 4d transition metals they're more stable then 3d transition mettals.\n\n
GENERAL INFORMATION ABOUT 5d transition series
1. 5d – transition series. It consists of elements with atomic number 57(La), 72(Hf) to 80(Hg)
   having incomplete 5d orbitals. It is called third transition series. 
2. Atomic and ionic size decreases while moving left to right .However from lr to Hg the size increses
   due to electron repulsion in the higly filled d orbital.
3. The Ionization Enthalpy of 5d transition series is higher than 3d and 4d transition series because of
   Lanthanoid Contraction.
"""
f_text="""
GENERAL INFORMATION ABOUT THE F-BLOCK\n\n
1. The F-block name is taken because the valance f orbital of the elements are progressively filled.
2. There are two series in the f block corresponding to the filling up of 4f and 5f orbitals. The
   elements are 4f series of (Ce to Lu) and 5f series of (Th to Lw). There are 14 elements filling up
   the ‘f’ orbital in each series. 
3. There are mainly three series of the elements, 3d-series (Sc to Zn) 4d-series (Y to Cd) and 5d-series
   (La to Hg omitting Ce to Lu). The fourth 6d-series which begins with Ac is still incomplete.
4. F block elements are placed separately at the bottom of the periodic table. They are a subset of 6th
   and 7th periods. \n
GENERAL INFORMATION ABOUT LANTHANIDES 
1. The first series of elements are called lanthanides and include elements with atomic numbers
   beginning from 57 and ending at 71.
2. These elements are non-radioactive (except for promethium, which is radioactive).    
3. A decrease in atomic and ionic radii from lanthanum to lutetium is observed. This is called the
   lanthanoid contraction.\n
GENERAL INFORMATION ABOUT ACTINIDES 
1. The second series of elements are called actinides and include elements with atomic numbers
   beginning from 89 and ending at 103. 
2. These elements generally have a radioactive nature. 
3. A decrease in atomic and ionic radii from Actinium to Lawrencium is observed. This is called the
   actinoid contraction.
"""
about_text="""
Creator :
	Aayush Patel

About The Project:
	I have created a python based application which
	would be helpful for science students.
	Our app has a Tkinter-based window that would
	display all the elements of the Periodic Table.
	If someone wants to know about any element,
	our app will be the best platform for him/her.
	Our app will provide the user with all the information
	regarding the chemistry of the elements.
	It would contain information about :
	1. Atomic Number
	2. Atomic Mass
	3. Symbol of the element
	4. Full Name
	5. Electronic Configuration
	6. Number of electrons, protons, and neutrons
	7. Radioactive Nature
	8. Electronegativity
	9. Group Number
	10. Period Number
	11. Colour
	12. State
	13. Melting Point
	14. Boiling Point
"""
intro_text="""
GENERAL INFORMATION ABOUT THE PERIODIC TABLE\n
The modern periodic table in today's modern world is a common term for every
student but if we look back in time. No doubt it can be termed as a pinnacle
of modern science mixed with the anicent knowledge from the times unknown.\n
The periodic table is a tabular display of the chemical elements, which are arranged
by atomic number,electron configuration, andrecurring chemical properties.
The structure of the table shows periodic trends.
The seven rows of the table, called periods,generally have metals on the left and nonmetals on the right.
The columns, called groups, contain elements with similar chemical behaviours.
Six groups have accepted names as well as assigned numbers: for example, group 17 elements are the halogens;
and group 18 are the noble gases.Also displayed are four simple
rectangular areas or blocks associated with the filling of different atomic orbitals.\n
The elements from atomic numbers 1 (Hydrogen) through 118 (Oganesson) have been discovered
or synthesized, completing seven full rows of the periodic table. The first 94 elements,
hydrogen through plutonium, all occur naturally, though some are found only in trace amounts and
a few were discovered in nature only after having first been synthesized.
Elements 95 to 118 have only been synthesized in laboratories or nuclear reactors.
The synthesis of elements having higher atomic numbers is currently being pursued:
these elements would begin an eighth row, and theoretical work has been
done to suggest possible candidates for this extension. Numerous synthetic radioisotopes of
naturally occurring elements have also been produced in laboratories.\n\n
HISTORY OF PERIODIC TABLE:-\n
DMITRI MANDELEEV - THE FATHER OF PERIODIC TABLE\n
Dmitri Mendeleev is often referred to as the Father of the Periodic
Table because In March 1869, Mendeleev delivered a full paper to the Russian
Chemical Society spelling out the most significant aspect of his system, that
characteristics of the elements recur at a periodic interval as a function of
their atomic weight and later which led to the rise of what we see today in
this application.\n
MANDELEEV'S PERIODIC TABLE\n
Mendeleev was far from the first chemist to attempt to organize the elements
by atomic weight or to recognize that characteristics recurred on some sort of regular
basis.Through much of the nineteenth century, chemists had worked to find an organizing
principle that encompassed all of the known elements and that could be considered a law
of nature. 
Mendeleevís system was not perfect but it had the hallmarks of a scientific law, one
that would hold true through new discoveries and against all challenges.
One of the unique aspects of Mendeleevís table was the gaps he left.  In these places
he not only predicted there were as-yet-undiscovered elements, but he predicted their
atomic weights and their characteristics. The discovery of new elements in the 1870s that
fulfilled several of his predictions brought increased interest to the periodic system
and it became not only an object of study but a tool for research.
The mandeleev's periodic law and periodic table both easily accomodated the discovery of
noble gases but later in 1896 when radio activity was discoverd it poised to destroy the
periodic system and this later gave way to the modern periodic table.\n
RISE OF MODERN PERIODIC TABLE\n
The discovery of radioactivity in 1896 seemed poised to destroy the periodic system.
Chemists had always considered elements to be substances that could not break down into
smaller parts.How could radioactive elements, which decayed into other substances, be
considered elements?  And if they were, how could so many fit into the very few gaps left in
the table? 
Chemists and physicists working together began to understand the structure of the atom and were
soon able to explain how the periodic system worked on an atomic level. 
that rather than atomic weight, atomic numberóthe number of protons in the nucleus of an
atomódetermined the characteristics of an element.  Rather miraculously, organizing the elements
by their atomic number rather than their atomic weight did not change the arrangement of the
periodic table.  In fact, understanding how electrons fill the shells orbiting a nucleus explained
some of the anomalies that had plagued the periodic system from the start.
The periodic tableóthe visual representation of the periodic lawóis recognized as one of the great 
achievements of chemistry and as a uniting scientific concept, relevant to the physical and life 
sciences alike. 
But the periodic table is also an important aspect of science education
And with this application we're trying to enhance it even further by making the 
periodic table more informative and interactive which was far lacking when we used
to see the flat 2 Dimensional periodic table that used to hang on the wall of most chemistry
classrooms or appears inside the cover of most chemistry textbooks.
"""
def main_program():
    global bgcolour, bgcolourlight, colour
    global s_text,p_text,d_text,f_text,about_text,intro_text
    #5+splash_root.destroy()
    root=Tk()
    root.config(bg=bgcolour)
    # Gets the requested values of the height and widht.
    windowWidth = root.winfo_reqwidth()
    windowHeight = root.winfo_reqheight()
    # Gets both half the screen width/height and window width/height
    positionRight = int(root.winfo_screenwidth()/4 - windowWidth/2)
    positionDown = int(root.winfo_screenheight()/7 - windowHeight/2)
    # Positions the window in the center of the page.
    root.geometry("+{}+{}".format(positionRight, positionDown))
    root.title("Periodic Table")
    root.iconbitmap("Pticon.ico")
    rootframe=Frame(root)
    rootframe.grid(row=1,column=1)
    rootframe.config(bg=bgcolourlight)
    mainframe=LabelFrame(rootframe,padx=20,pady=20,border=50)
    mainframe.grid(row=1,column=1,rowspan=5)
    mainframe.config(bg=bgcolour)
    lframe1=LabelFrame(rootframe,padx=20,pady=20)
    lframe2=LabelFrame(rootframe,padx=20,pady=20)
    lframe1.config(bg=bgcolour)
    lframe1.config(bg=bgcolour)
    def introduction():
        rootframe.grid_forget()
        pt_frame=Frame(root,padx=20,pady=20,bg=bgcolour)
        pt_frame.grid(row=1,column=1)
        scroll_y=Scrollbar(pt_frame)
        scroll_y.pack(side=RIGHT,fill=Y)
        tbox=Text(pt_frame,font="aerial 15",width=50,height=20,wrap=WORD,padx=20,pady=20,yscrollcommand=scroll_y.set,bg=bgcolourlight)
        tbox.pack()
        scroll_y.config(command=tbox.yview)
        tbox.insert(1.0,intro_text)
        tbox.config(state=DISABLED)
        def hide_pt_frame():
            pt_frame.grid_forget()
            rootframe.grid(row=1,column=1)
        Button(pt_frame,text="Back",font="aerial 15",command=hide_pt_frame,bg=bgcolourlight).pack(anchor=E)
    heading=Button(mainframe,text="Periodic Table",font="aerial 30 bold",bg="white",fg="grey",border=0.1,command=introduction)
    heading.pack(anchor=N)

    #Menu
    main_menu=Menu(root)
    root.config(menu=main_menu)
    format_menu=Menu(main_menu)
    main_menu.add_cascade(label="Format",menu=format_menu)

    #Colour Change
    def change_colour():
        lframe1.grid(row=1,column=0) 
        def get_colour():
            colour[0]=e1.get()
            colour[1]=e2.get()
            colour[2]=e3.get()
            colour[3]=e4.get()
            mainbody()
        def default():
            e1.set("pink")
            e2.set("light grey")
            e3.set("yellow")
            e4.set("sky blue")
            get_colour()
        e1=StringVar()
        e2=StringVar()
        e3=StringVar()
        e4=StringVar()
        E1=Entry(lframe1,textvariable=e1,bg=bgcolourlight)
        E1.grid(row=1,column=2)
        E2=Entry(lframe1,textvariable=e2,bg=bgcolourlight)
        E2.grid(row=2,column=2)
        E3=Entry(lframe1,textvariable=e3,bg=bgcolourlight)
        E3.grid(row=3,column=2)
        E4=Entry(lframe1,textvariable=e4,bg=bgcolourlight)
        E4.grid(row=4,column=2)
        e1.set(colour[0])
        e2.set(colour[1])
        e3.set(colour[2])
        e4.set(colour[3])
        def choose0():
            c=colorchooser.askcolor()[1]
            e1.set(c)
        def choose1():
            c=colorchooser.askcolor()[1]
            e2.set(c)
        def choose2():
            c=colorchooser.askcolor()[1]
            e3.set(c)
        def choose3():
            c=colorchooser.askcolor()[1]
            e4.set(c)
        Button(lframe1,text="Choose",command=choose0,bg=bgcolourlight).grid(row=1,column=3)
        Button(lframe1,text="Choose",command=choose1,bg=bgcolourlight).grid(row=2,column=3)
        Button(lframe1,text="Choose",command=choose2,bg=bgcolourlight).grid(row=3,column=3)
        Button(lframe1,text="Choose",command=choose3,bg=bgcolourlight).grid(row=4,column=3)
        Label(lframe1,text="S Block ",bg=bgcolour).grid(row=1,column=1)
        Label(lframe1,text="P Block",bg=bgcolour).grid(row=2,column=1)
        Label(lframe1,text="D Block",bg=bgcolour).grid(row=3,column=1)
        Label(lframe1,text="F Block ",bg=bgcolour).grid(row=4,column=1)        
        Button(lframe1,text="Apply",command=get_colour,bg=bgcolourlight).grid(row=5,column=2)
        Button(lframe1,text="Default",command=default,bg=bgcolourlight).grid(row=5,column=3)
        def hide_lframe1():
            lframe1.grid_forget() 
        Button(lframe1,text="Back",command=hide_lframe1,bg=bgcolourlight).grid(row=6,column=2)
    colour_menu=Menu(format_menu)
    format_menu.add_cascade(label="Colour",menu=colour_menu)
    colour_menu.add_command(label="Change Colour of Blocks",command=change_colour)
    def About():
        rootframe.grid_forget()
        root.title("About")
        About_frame=Frame(root,padx=20,pady=20,bg=bgcolour)
        About_frame.grid(row=1,column=1)
        scroll_y=Scrollbar(About_frame)
        scroll_y.pack(side=RIGHT,fill=Y)
        tbox=Text(About_frame,font="aerial 15",width=50,height=20,wrap=WORD,padx=20,pady=20,yscrollcommand=scroll_y.set,bg=bgcolourlight)
        tbox.pack()
        scroll_y.config(command=tbox.yview)
        tbox.insert(1.0,about_text)
        tbox.config(state=DISABLED)
        def hide_About_frame():
            About_frame.grid_forget()
            root.title("Periodic Table")
            rootframe.grid(row=1,column=1)
        Button(About_frame,text="Back",font="aerial 15",command=hide_About_frame,bg=bgcolourlight).pack(anchor=E)      
    main_menu.add_command(label="About",command=About)
    def destroy_root():
        answer=messagebox.askquestion("Exit","Do You Want To Exit.")
        if (answer=="yes"):
            root.destroy()
    main_menu.add_command(label="Exit",command=destroy_root)

    #Making frames for Main Window
    f1=Frame(mainframe,bg=bgcolour)
    f1.pack()
    f2=Frame(mainframe,bg=bgcolour)
    f2.pack(pady=30)

    #List of symbol
    l=['','H','He','Li','Be','B','C','N','O','F','Ne','Na','Mg','Al','Si','P','S','Cl','Ar','K','Ca','Sc','Ti','V','Cr','Mn','Fe','Co','Ni','Cu','Zn','Ga','Ge','As','Se',
    'Br','Kr','Rb','Sr','Y','Zr','Nb','Mo','Tc','Ru','Rh','Pd','Ag','Cd','In','Sn','Sb','Te','I','Xe',
    'Cs','Ba','La','Ce','Pr','Nd','Pm','Sm','Eu','Gd','Tb','Dy','Ho','Er','Tm','Yb','Lu','Hf','Ta','W','Re','Os','Ir','Pt','Au','Hg','Tl','Pb','Bi','Po','At',
    'Rn','Fr','Ra','Ac','Th','Pa','U','Np','Pu','Am','Cm','Bk','Cf','Es','Fm','Md','No','Lr','Rf','Db','Sg','Bh','Hs','Mt','Ds','Rg','Cn','Nh','Fl','Mc','Lv','Ts','Og']
            

    #List of masses        
    no="Not Available"
    l_mass=["",1.008,4.003,6.941,9.012,10.811,12.011,14.007,15.999,18.998,20.180,22.990,24.305,26.982,28.086,30.974,32.065,35.453,39.948,39.098,40.078,44.956,47.867,
            50.942,51.996,54.938,55.845,58.933,58.693,63.546,65.390,69.723,72.640,74.922,78.960,79.904,83.800,85.468,87.620,88.906,91.224,92.906,95.940,98.000,
            101.070,102.906,106.420,107.868,112.411,114.818,118.710,121.760,127.600,126.905,131.293,132.906,137.327,138.906,140.116,140.908,144.240,145.000,150.360,
            151.964,157.250,158.925,162.500,164.930,167.259,168.934,173.040,174.967,178.490,180.948,183.840,186.207,190.230,192.217,195.078,196.967,200.590,204.383,
            207.200,208.980,209.000,210.000,222.000,223.000,226.000,227.000,232.038,231.036,238.029,237.000,244.000,243.000,247.000,247.000,251.000,252.000,
            257.000,258.000,259.000,262.000,261.000,262.000,266.000,264.000,277.000,268.000,no,no,no,no,no,no,no,no,no]

    #List of Names
    l_name=['','Hydrogen','Helium','Lithium','Beryllium','Boron','Carbon','Nitrogen','Oxygen',
    'Fluorine','Neon','Sodium','Magnesium','Aluminum','Silicon','Phosphorus','Sulfur','Chlorine',
    'Argon','Potassium','Calcium','Scandium','Titanium','Vanadium','Chromium','Manganese','Iron','Cobalt','Nickel','Copper','Zinc',
    'Gallium','Germanium','Arsenic','Selenium','Bromine','Krypton','Rubidium','Strontium','Yttrium',
    'Zirconium','Niobium','Molybdenum','Technetium','Ruthenium','Rhodium','Palladium','Silver','Cadmium','Indium',
    'Tin','Antimony','Tellurium','Iodine','Xenon','Cesium','Barium','Lanthanum','Cerium','Praseodymium','Neodymium','Promethium',
    'Samarium','Europium','Gadolinium','Terbium','Dysprosium','Holmium','Erbium','Thulium','Ytterbium','Lutetium','Hafnium',
    'Tantalum','Tungsten','Rhenium','Osmium','Iridium','Platinum','Gold','Mercury','Thallium','Lead','Bismuth','Polonium','Astatine',
    'Radon','Francium','Radium','Actinium','Thorium','Protactinium','Uranium','Neptunium','Plutonium','Americium','Curium',
    'Berkelium','Californium','Einsteinium','Fermium','Mendelevium','Nobelium','Lawrencium','Rutherfordium',
    'Dubnium','Seaborgium','Bohrium','Hassium','Meitnerium','Darmstadium','Rogentenium','Copernicum','Nihonium',
    'Flerovium','Moscovium','Livermorium','Tennessine','Oganesson']

    #list of ionization energy
    l_IE=["",13.60,24.59,5.39,9.32,8.30,11.26,14.53,13.62,17.42,21.56,5.14,7.65,5.99,8.15,10.49,10.36,
            12.97,15.76,4.34,6.11,6.56,6.83,6.75,6.77,7.43,7.90,7.88,7.64,7.73,9.39,6.00,7.90,
            9.79,9.75,11.81,14.00,4.18,5.69,6.22,6.63,6.76,7.09,7.28,7.36,7.46,8.34,7.58,8.99,5.79,7.34,8.61,9.01,
            10.45,12.13,3.89,5.21,5.58,5.54,5.47,5.53,5.58,5.64,5.67,6.15,5.86,5.94,6.02,6.11,6.18,6.25,5.43,6.83,7.55,
            7.86,7.83,8.44,8.97,8.96,9.23,10.44,6.11,7.42,7.29,8.42,9.30,10.75,4.07,5.28,5.17,6.31,5.89,
            6.19,6.27,6.03,5.97,5.99,6.20,6.28,6.42,6.50,6.58,6.65,4.90,0.00,0.00,0.00,0.00,0.00,0.00,no,no,no,no,no,no,no,no,no]

    #list for electronic configuration
    l_configuration=["",'1s\u00b9','1s\u00b2','[He] 2s1','[He] 2s2',
    '[He] 2s2 2p1','[He] 2s2 2p2','[He] 2s2 2p3','[He] 2s2 2p4','[He] 2s2 2p5','[He] 2s2 2p6','[Ne] 3s1','[Ne] 3s2','[Ne] 3s2 3p1',
    '[Ne] 3s2 3p2','[Ne] 3s2 3p3','[Ne] 3s2 3p4','[Ne] 3s2 3p5','[Ne] 3s2 3p6','[Ar] 4s1','[Ar] 4s2','[Ar] 3d1 4s2','[Ar] 3d2 4s2','[Ar] 3d3 4s2',
    '[Ar] 3d5 4s1','[Ar] 3d5 4s2','[Ar] 3d6 4s2','[Ar] 3d7 4s2','[Ar] 3d8 4s2','[Ar] 3d10 4s1','[Ar] 3d10 4s2','[Ar] 3d10 4s2 4p1','[Ar] 3d10 4s2 4p2',
    '[Ar] 3d10 4s2 4p3','[Ar] 3d10 4s2 4p4','[Ar] 3d10 4s2 4p5','[Ar] 3d10 4s2 4p6','[Kr] 5s1','[Kr] 5s2','[Kr] 4d1 5s2','[Kr] 4d2 5s2','[Kr] 4d4 5s1',
    '[Kr] 4d5 5s1','[Kr] 4d5 5s2','[Kr] 4d7 5s1','[Kr] 4d8 5s1','[Kr] 4d10','[Kr] 4d10 5s1','[Kr] 4d10 5s2','[Kr] 4d10 5s2 5p1','[Kr] 4d10 5s2 5p2',
    '[Kr] 4d10 5s2 5p3','[Kr] 4d10 5s2 5p4','[Kr] 4d10 5s2 5p5','[Kr] 4d10 5s2 5p6','[Xe] 6s1','[Xe] 6s2','[Xe] 5d1 6s2','[Xe] 4f1 5d1 6s2',
    '[Xe] 4f3 6s2','[Xe] 4f4 6s2','[Xe] 4f5 6s2','[Xe] 4f6 6s2','[Xe] 4f7 6s2','[Xe] 4f7 5d1 6s2','[Xe] 4f9 6s2','[Xe] 4f10 6s2','[Xe] 4f11 6s2',
    '[Xe] 4f12 6s2','[Xe] 4f13 6s2','[Xe] 4f14 6s2','[Xe] 4f14 5d1 6s2','[Xe] 4f14 5d2 6s2','[Xe] 4f14 5d3 6s2','[Xe] 4f14 5d4 6s2',
    '[Xe] 4f14 5d5 6s2','[Xe] 4f14 5d6 6s2','[Xe] 4f14 5d7 6s2','[Xe] 4f14 5d9 6s1','[Xe] 4f14 5d10 6s1','[Xe] 4f14 5d10 6s2',
    '[Xe] 4f14 5d10 6s2 6p1','[Xe] 4f14 5d10 6s2 6p2','[Xe] 4f14 5d10 6s2 6p3','[Xe] 4f14 5d10 6s2 6p4','[Xe] 4f14 5d10 6s2 6p5',
    '[Xe] 4f14 5d10 6s2 6p6','[Rn] 7s1','[Rn] 7s2','[Rn] 6d1 7s2','[Rn] 6d2 7s2','[Rn] 5f2 6d1 7s2','[Rn] 5f3 6d1 7s2',
    '[Rn] 5f4 6d1 7s2','[Rn] 5f6 7s2','[Rn] 5f7 7s2','[Rn] 5f7 6d1 7s2','[Rn] 5f9 7s2','[Rn] 5f10 7s2','[Rn] 5f11 7s2','[Rn] 5f12 7s2',
    '[Rn] 5f13 7s2','[Rn] 5f14 7s2','[Rn] 5f14 6d1 7s2','[Rn] 5f14 6d2 7s2','[Rn] 5f14 6d3 7s2','[Rn] 5f14 6d4 7s2','[Rn] 5f14 6d5 7s2',
    '[Rn] 5f14 6d6 7s2','[Rn] 5f14 6d7 7s2','[Rn] 5f14 6d8 7s2','[Rn] 5f14 6d10 7s1','[Rn] 5f14 6d10 7s2','[Rn] 5f14 6d10 7s2 7p1',
    '[Rn] 5f14 6d10 7s2 7p2','[Rn] 5f14 6d10 7s2 7p3','[Rn] 5f14 6d10 7s2 7p4','[Rn] 5f14 6d10 7s2 7p5','[Rn] 5f14 6d10 7s2 7p6']

    #List of Physical State
    physical_state=['','gas', 'gas', 'solid', 'solid', 'solid', 'solid', 'gas', 'gas', 'gas', 'gas', 'solid', 'solid', 'solid', 'solid', 'solid',
                    'solid', 'gas', 'gas', 'solid', 'solid', 'solid', 'solid','solid', 'solid', 'solid', 'solid', 'solid', 'solid', 'solid', 'solid', 'solid',
                    'solid', 'solid', 'solid', 'liquid', 'gas', 'solid', 'solid', 'solid', 'solid', 'solid', 'solid', 'solid', 'solid', 'solid', 'solid',
                    'solid', 'solid', 'solid', 'solid', 'solid', 'solid', 'solid', 'gas', 'solid', 'solid', 'solid', 'solid', 'solid', 'solid',
                    'solid', 'solid', 'solid', 'solid', 'solid', 'solid', 'solid', 'solid', 'solid', 'solid', 'solid', 'solid', 'solid', 'solid',
                    'solid', 'solid', 'solid', 'solid', 'solid', 'liquid', 'solid', 'solid', 'solid', 'solid', 'solid', 'gas', 'solid', 'solid',
                    'solid', 'solid', 'solid', 'solid', 'solid', 'solid', 'solid', 'solid', 'solid', 'solid', 'solid', 'solid', 'solid', 'solid',
                    'solid', 'solid', 'solid', 'solid', 'solid', 'solid', 'solid', 'solid', 'solid', 'solid', 'solid', 'solid', 'solid', 'solid', 'solid', 'solid']
    #List of Colours
    elem_colour=['','white', 'white to orange', 'silvery', 'gray', 'brown', 'black', 'colorless', 'colorless', 'pale-yellow green', 'orange',
                  'silvery', 'gray-white', 'silvery-white', 'grayish', 'white', 'pale-yellow', 'yellow-green', 'violet', 'silvery-white', 'silvery',
                  'silvery-white', 'silver', 'yellow-violet', 'steely-grey', 'gray-white', 'silvery-gray', 'blue', 'silvery-white', 'reddish brown',
                  'bluish-gray', 'silvery', 'white', 'silvery-gray', 'brick-red', 'red', 'red-green-black', 'white', 'silvery-yellow', 'silvery-white',
                  'silver-gray', 'grey', 'grey', 'gray', 'silvery', 'silvery-white', 'silvery', 'silvery', 'yellow', 'silvery-white', 'silvery-white',
                  'bluish-white', 'silvery-white', 'violet-black', 'colorless', 'silvery golden', 'silvery-white', 'silvery-white', 'gray', 'green',
                  'white', 'white', 'silvery-white', 'silvery-white', 'silvery-white', 'white', 'silvery', 'silvery-white', 'pink', 'silvery white',
                  'white', 'silvery-white', 'silver-gray', 'blue-gray', 'grayish-white', 'white', 'white', 'white', 'grayish-white', 'golden',
                  'silvery-white', 'silvery-white', 'silvery-bluish', 'gray-white', 'silvery-gray', 'black', 'colorless', 'silver gray',
                  'silvery-white', 'silvery-white', 'silvery-white', 'silvery', 'silvery-white', 'silvery', 'silvery', 'silvery', 'silvery-white',
                  'silvery-white', 'white', 'silvery', 'silver', 'silvery-gray', 'silver', 'silvery-white', 'silvery-white', 'silvery-gray', 'silvery-white',
                  'silvery-gray', 'silvery-white', 'unknown', 'unknown', 'unknown', 'unknown', 'unknown', 'unknown', 'unknown',
                  'unknown', 'unknown', 'unknown']
    #List of Boiling Point
    elem_bp=['','-252.9', '-268.9', '1330', '2471', '3927', '4827', '-195,5', '-182,962', '-188.11', '-246', '883', '1091', '2470', '3265',
             '280.5', '444.6', '-34.04', '-185.8', '760', '1484', '2836', '3287', '3407', '2671', '2061', '2862', '2927', '2730', '2562', '907',
             '2400', '2833', '613', '685', '58.8', '-152.3', '688', '1384', '2927', '4371', '4744', '4639', '4877', '4150', '3727', '2963', '2162',
             '767', '2080', '2602', '1380', '988', '185', '-108', '671', '1805', '3464', '3443', '3130', '3074', '3000', '1900', '1529', '3000', '3123',
             '2562', '2600', '2868', '1950', '1196', '3402', '4603', '5458', '10220', '5630', '5000', '4130', '3825', '2807', '365.73', '1473',
             '1479', '1564', '962', '337', '-61.7', '676.8', '1140', '3200', '4790', '4000', '4131', '3902', '3228', '2607', '3110', '2590', '1470',
             '996', 'unknown', 'unknown', 'unknown', 'unknown', '5500', 'unknown', 'unknown', 'unknown', 'unknown', 'unknown',
             'unknown', 'unknown', 'unknown', 'unknown', 'unknown', 'unknown', 'unknown', 'unknown', 'unknown']
    #List of Melting Point
    elem_mp=['','-259.16', '-272.20', '180.5', '1287', '2076', 'unknown', '-210', '-218,79', '-219,67', '-248,67', '98', '650',
             '660.32', '1414', '44.15', '115.21', '-101.5', '-189.48', '63.28', '842', '1541', '1668', '1910', '1907', '1246', '1538', '1495',
             '1455', '1084', '420', '30', '938.25', '816.8', '221', '-7.2', '-156.6', '39,3', '769', '1509', '1855', '2477', '2623', '2200',
             '2334', '1966', '1554.9', '961.78', '321.07', '156.6', '231.93', '630.5', '449.51', '133.5', '-111.9', '28.5', '727', '920', '795',
             '935', '1024', '1042', '1072', '826', '1312', '1356', '1407', '1461', '1529', '1545', '824', '1652', '2233', '3017', '6152', '3186',
             '3000', '2446', '1768.3', '1063', '-38.8', '304', '327,46', '271.5', '254', '307', '-71', '27', '700', '1050', '1750', '1570', '1132.2',
             '640', '639.4', '1176', '1340', '1050', '900', '860', '1800', '827', '827', '1627',
             '2100', 'unknown', 'unknown', 'unknown', 'unknown', 'unknown', 'unknown', 'unknown',
             'unknown', 'unknown', 'unknown', 'unknown', 'unknown', 'unknown', 'unknown']
    
    #Labelling
    Label(f1,text="Groups\nPeriods\n",font="aerial 10",bg=bgcolour).grid(row=1,column=1)
    Label(f2,text="Lanthanoids ",font="aerial 20",bg=bgcolour).grid(row=1,column=0)
    Label(f2,text="Actinoids ",font="aerial 20",bg=bgcolour).grid(row=2,column=0)

    #Group Numbering
    Label(f1,text="1",font="aerial 20",bg=bgcolour).grid(row=1,column=2)    
    Label(f1,text="2",font="aerial 20",bg=bgcolour).grid(row=2,column=3)
    Label(f1,text="3",font="aerial 20",bg=bgcolour).grid(row=4,column=4)
    Label(f1,text="4",font="aerial 20",bg=bgcolour).grid(row=4,column=5)
    Label(f1,text="5",font="aerial 20",bg=bgcolour).grid(row=4,column=6)
    Label(f1,text="6",font="aerial 20",bg=bgcolour).grid(row=4,column=7)
    Label(f1,text="7",font="aerial 20",bg=bgcolour).grid(row=4,column=8)
    Label(f1,text="8",font="aerial 20",bg=bgcolour).grid(row=4,column=9)
    Label(f1,text="9",font="aerial 20",bg=bgcolour).grid(row=4,column=10)
    Label(f1,text="10",font="aerial 20",bg=bgcolour).grid(row=4,column=11)
    Label(f1,text="11",font="aerial 20",bg=bgcolour).grid(row=4,column=12)
    Label(f1,text="12",font="aerial 20",bg=bgcolour).grid(row=4,column=13)
    Label(f1,text="13",font="aerial 20",bg=bgcolour).grid(row=2,column=14)
    Label(f1,text="14",font="aerial 20",bg=bgcolour).grid(row=2,column=15)
    Label(f1,text="15",font="aerial 20",bg=bgcolour).grid(row=2,column=16)
    Label(f1,text="16",font="aerial 20",bg=bgcolour).grid(row=2,column=17)
    Label(f1,text="17",font="aerial 20",bg=bgcolour).grid(row=2,column=18)
    Label(f1,text="18",font="aerial 20",bg=bgcolour).grid(row=1,column=19)

    #Period Numbering
    Label(f1,text="1",font="aerial 20",bg=bgcolour).grid(row=2,column=1)
    Label(f1,text="2",font="aerial 20",bg=bgcolour).grid(row=3,column=1)
    Label(f1,text="3",font="aerial 20",bg=bgcolour).grid(row=4,column=1)
    Label(f1,text="4",font="aerial 20",bg=bgcolour).grid(row=5,column=1)
    Label(f1,text="5",font="aerial 20",bg=bgcolour).grid(row=6,column=1)
    Label(f1,text="6",font="aerial 20",bg=bgcolour).grid(row=7,column=1)
    Label(f1,text="7",font="aerial 20",bg=bgcolour).grid(row=8,column=1)

    #Blocks
    def sblock():
        global bgcolour, bgcolourlight
        rootframe.grid_forget()
        root.title("S Block")
        sblock_frame=Frame(root,padx=20,pady=20,bg=bgcolour)
        sblock_frame.grid(row=1,column=1)
        scroll_y=Scrollbar(sblock_frame)
        scroll_y.pack(side=RIGHT,fill=Y)
        tbox=Text(sblock_frame,font="aerial 15",width=50,height=20,wrap=WORD,padx=20,pady=20,yscrollcommand=scroll_y.set,bg=bgcolourlight)
        tbox.pack()
        scroll_y.config(command=tbox.yview)
        tbox.insert(1.0,s_text)
        tbox.config(state=DISABLED)
        def hide_sblock_frame():
            sblock_frame.grid_forget()
            root.title("Periodic Table")
            rootframe.grid(row=1,column=1)
        Button(sblock_frame,text="Back",font="aerial 15",command=hide_sblock_frame,bg=bgcolourlight).pack(anchor=E)
    def pblock():
        global bgcolour, bgcolourlight
        rootframe.grid_forget()
        root.title("P Block")
        pblock_frame=Frame(root,padx=20,pady=20,bg=bgcolour)
        pblock_frame.grid(row=1,column=1)
        scroll_y=Scrollbar(pblock_frame)
        scroll_y.pack(side=RIGHT,fill=Y)
        tbox=Text(pblock_frame,font="aerial 15",width=50,height=20,wrap=WORD,padx=20,pady=20,yscrollcommand=scroll_y.set,bg=bgcolourlight)
        tbox.pack()
        scroll_y.config(command=tbox.yview)
        tbox.insert(1.0,p_text)
        tbox.config(state=DISABLED)
        def hide_pblock_frame():
            pblock_frame.grid_forget()
            root.title("Periodic Table")
            rootframe.grid(row=1,column=1)
        Button(pblock_frame,text="Back",font="aerial 15",command=hide_pblock_frame,bg=bgcolourlight).pack(anchor=E)
    def dblock():
        global bgcolour, bgcolourlight
        rootframe.grid_forget()
        root.title("D Block")
        dblock_frame=Frame(root,padx=20,pady=20,bg=bgcolour)
        dblock_frame.grid(row=1,column=1)
        scroll_y=Scrollbar(dblock_frame)
        scroll_y.pack(side=RIGHT,fill=Y)
        tbox=Text(dblock_frame,font="aerial 15",width=50,height=20,wrap=WORD,padx=20,pady=20,yscrollcommand=scroll_y.set,bg=bgcolourlight)
        tbox.pack()
        scroll_y.config(command=tbox.yview)
        tbox.insert(1.0,d_text)
        tbox.config(state=DISABLED)
        def hide_dblock_frame():
            dblock_frame.grid_forget()
            root.title("Periodic Table")
            rootframe.grid(row=1,column=1)
        Button(dblock_frame,text="Back",font="aerial 15",command=hide_dblock_frame,bg=bgcolourlight).pack(anchor=E)
    def fblock():
        global bgcolour, bgcolourlight
        rootframe.grid_forget()
        root.title("F Block")
        fblock_frame=Frame(root,padx=20,pady=20,bg=bgcolour)
        fblock_frame.grid(row=1,column=1)
        scroll_y=Scrollbar(fblock_frame)
        scroll_y.pack(side=RIGHT,fill=Y)
        tbox=Text(fblock_frame,font="aerial 15",width=50,height=20,wrap=WORD,padx=20,pady=20,yscrollcommand=scroll_y.set,bg=bgcolourlight)
        tbox.pack()
        scroll_y.config(command=tbox.yview)
        tbox.insert(1.0,f_text)
        tbox.config(state=DISABLED)
        def hide_fblock_frame():
            fblock_frame.grid_forget()
            root.title("Periodic Table")
            rootframe.grid(row=1,column=1)
        Button(fblock_frame,text="Back",font="aerial 15",command=hide_fblock_frame,bg=bgcolourlight).pack(anchor=E)
    border_width=3
    Button(f1,text="S Block",font="aerial 15",command=sblock,bd=border_width,bg=bgcolourlight).grid(row=0,column=2,columnspan=2)
    Button(f1,text="P Block",font="aerial 15",command=pblock,bd=border_width,bg=bgcolourlight).grid(row=0,column=14,columnspan=8)
    Button(f1,text="D Block",font="aerial 15",command=dblock,bd=border_width,bg=bgcolourlight).grid(row=3,column=4,columnspan=10)
    Button(f2,text="F Block",font="aerial 15",command=fblock,bd=border_width,bg=bgcolourlight).grid(row=0,column=1,columnspan=14)

    def conv_into_superscript(confg):
        l=list(confg.split())
        x=len(l)
        def con_unicode(digit):
            if (digit==0):
                sup="\u2070"
            if (digit==1):
                sup="\u00b9"
            if (digit == 2) :
                sup="\u00b2"
            if (digit == 3) :
                sup="\u00b3"
            if (digit==4):
                sup="\u2074"
            if (digit==5):
                sup="\u2075"
            if (digit==6):
                sup="\u2076"
            if (digit==7):
                sup="\u2077"
            if (digit==8):
                sup="\u2078"
            if (digit==9):
                sup="\u2079"
            return sup
        for i in range(1,x):
            num=int(l[i][2:])
            if num > 9 :
                digit1=int(str(num)[0])
                digit2=int(str(num)[1])
                superscript=con_unicode(digit1)+con_unicode(digit2)
            else:
                digit1=num
                superscript=con_unicode(digit1)
            l[i]=l[i][:2]+superscript
        confg2=""
        for each in l:
            confg2+=each+" "
        return confg2
    def data (n):
        global bgcolour, bgcolourlight
        fgcolour="black"
        dataframe=LabelFrame(root,bg=bgcolour,bd=30)
        rootframe.grid_forget()
        dataframe.grid(row=1,column=1,columnspan=3)
        root.title(l_name[n])
        group=group_count(n)
        period=period_count(n)
        frame1=Frame(dataframe,bg=bgcolour)
        frame1.grid(row=0,column=0)
        frame2=Frame(dataframe,bg=bgcolour,padx=50)
        frame2.grid(row=0,column=1)
        frame3=Frame(dataframe,bg=bgcolour,padx=50)
        frame3.grid(row=0,column=2)
        for count in range(0,5):
            Label(frame1,text=" : ",font="bold",bg=bgcolour).grid(row=count,column=2)
        for count in range(0,6):
            Label(frame2,text=" : ",font="bold",bg=bgcolour).grid(row=count,column=2)
        for count in range(1,5):
            Label(frame3,text=" : ",font="bold",bg=bgcolour).grid(row=count,column=2)
        y_dist=15
        Label(frame1,text="Element",fg=fgcolour,font="aerial 20",bg=bgcolour,padx=10,pady=y_dist).grid(row=0,column=1)
        Label(frame1,text=l[n],bg=bgcolour,font="aerial 20",pady=y_dist).grid(row=0,column=3)
        Label(frame1,text="Full Name",font="aerial 20",bg=bgcolour,padx=10,pady=y_dist).grid(row=1,column=1)
        Label(frame1,text=l_name[n],bg=bgcolour,font="aerial 20",pady=y_dist).grid(row=1,column=3)
        Label(frame1,text="Atomic Number",font="aerial 20",bg=bgcolour,padx=10,pady=y_dist).grid(row=2,column=1)
        Label(frame1,text=n,bg=bgcolour,font="aerial 20",pady=y_dist).grid(row=2,column=3)
        Label(frame1,text="Atomic Mass",font="aerial 20",bg=bgcolour,padx=10,pady=y_dist).grid(row=3,column=1)
        Label(frame1,text=l_mass[n],bg=bgcolour,font="aerial 20",pady=y_dist).grid(row=3,column=3)
        if(n>=84):
            fact1="It is Radioactive."
            neutrons=no
        elif(n<84):
            fact1="It is not Radioactive."
            neutrons=int(l_mass[n])-n
        Label(frame3,text="Protons",bg=bgcolour,font="aerial 20",pady=y_dist).grid(row=1,column=1)
        Label(frame3,text=n,bg=bgcolour,font="aerial 20",pady=y_dist).grid(row=1,column=3)
        Label(frame3,text="Neutrons",font="aerial 20",bg=bgcolour,pady=y_dist).grid(row=2,column=1)
        Label(frame3,text=neutrons,font="aerial 20",bg=bgcolour,pady=y_dist).grid(row=2,column=3)
        Label(frame3,text="Electrons",font="aerial 20",bg=bgcolour,pady=y_dist).grid(row=3,column=1)
        Label(frame3,text=n,font="aerial 20",bg=bgcolour,pady=y_dist).grid(row=3,column=3)
        confg=l_configuration[n]
        confg2=conv_into_superscript(confg)
        Label(frame3,text="Electronic\nConfiguration",font="aerial 20",bg=bgcolour,pady=y_dist).grid(row=4,column=1)
        Label(frame3,text=confg2,font="aerial 20",bg=bgcolour,pady=y_dist).grid(row=4,column=3)
        Label(frame1,text="Ionization Energy\n(eV)",font="aerial 20",bg=bgcolour,pady=y_dist).grid(row=4,column=1)
        Label(frame1,text=l_IE[n],font="aerial 20",bg=bgcolour,pady=y_dist).grid(row=4,column=3)
        Label(frame2,text="Group",font="aerial 20",bg=bgcolour,pady=y_dist).grid(row=0,column=1)
        Label(frame2,text=group,font="aeroal 20",bg=bgcolour,pady=y_dist).grid(row=0,column=3)
        Label(frame2,text="Period",font="aerial 20",bg=bgcolour,pady=y_dist).grid(row=1,column=1)
        Label(frame2,text=period,font="aerial 20",bg=bgcolour,pady=y_dist).grid(row=1,column=3)
        Label(frame2,text="State",font="aerial 20",bg=bgcolour,pady=y_dist).grid(row=2,column=1)
        Label(frame2,text=physical_state[n].capitalize(),font="aerial 20",bg=bgcolour,pady=y_dist).grid(row=2,column=3)
        Label(frame2,text="Colour",font="aerial 20",bg=bgcolour,pady=y_dist).grid(row=3,column=1)
        Label(frame2,text=elem_colour[n].capitalize(),font="aerial 20",bg=bgcolour,pady=y_dist).grid(row=3,column=3)
        Label(frame2,text="Melting Point",font="aerial 20",bg=bgcolour,pady=y_dist).grid(row=4,column=1)
        Label(frame2,text=f'{elem_mp[n]} °C',font="aerial 20",bg=bgcolour,pady=y_dist).grid(row=4,column=3)
        Label(frame2,text="Boiling Point",font="aerial 20",bg=bgcolour,pady=y_dist).grid(row=5,column=1)
        Label(frame2,text=f'{elem_bp[n]} °C',font="aerial 20",bg=bgcolour,pady=y_dist).grid(row=5,column=3)
        Label(frame3,text=fact1,font="aerial 20",bg=bgcolour,pady=y_dist).grid(row=5,column=1,columnspan=3)
        def back_on_rootframe():
            root.title("Periodic Table")
            dataframe.grid_forget()
            rootframe.grid(row=1,column=1)
        def next_element(n):
            n=n+1
            if (n==119):
                n=1
            dataframe.grid_forget()
            data(n)
        def prev_element(n):
            n=n-1
            if(n==0):
                n=118
            dataframe.grid_forget()
            data(n)
        bgcolour2="#a9d3be"
        Button(dataframe,bd=10,text="View Periodic Table",font="aerial 20",bg=bgcolour2,command=back_on_rootframe).grid(row=3,column=1)
        Button(dataframe,bd=10,text="    Next Element   ",font="aerial 20",bg=bgcolour2,command=lambda : next_element(n)).grid(row=3,column=2)    
        Button(dataframe,bd=10,text="  Previous Element ",font="aerial 20",bg=bgcolour2,command=lambda : prev_element(n)).grid(row=3,column=0)
    def group_count(n):
        if( (n>=58 and n<=71) or (n>=90 and n<=103) ):
            group=3
        else:
            lcount=[2,8,8,18,18,32,32]
            lmain=[[1],[4],[21],[22],[23],[24],[25],[26],[27],[28],[29],[30],[5],[6],[7],[8],[9],[2]]
            count=0
            for elist in lmain:
                q=elist[0]
                lperiod=[2,10,18,36,54,86,118,q]
                lperiod.sort()
                p=lperiod.index(q)
                if(count in [0,1,2]):
                    l1=lcount[0:6]
                else:
                    l1=lcount[1:]
                for i in range(p,len(l1)):
                    q=q+l1[i]
                    elist.append(q)
                if (n in elist):
                    group=count+1
                count+=1
        return group
    def period_count(n):
        lp=[2,10,18,36,54,86,118,n]
        lp.sort()
        period=lp.index(n)+1
        return period  
    #loop for body
    def mainbody():
        for atomic_number in range(1,118+1):
            n=atomic_number
            group=group_count(n)
            period=period_count(n)
            w=3
            if group in [1,2]:
                index=-4
            elif group in range(13,19):
                index=-3
            elif group in range(3,13):
                index=-2
            if n not in (list(range(58,72))+list(range(90,104))) :
                b=Button(f1,text=l[n],font="aerial 15",width=3)
                b.grid(row=period+1,column=group+1)
            elif n in range(58,72):
                index=-1
                b=Button(f2,text=l[n],font="aerial 15",width=w)
                b.grid(row=1,column=n-57)
            elif n in range(90,104):
                index=-1
                b=Button(f2,text=l[n],font="aerial 15",width=w)
                b.grid(row=2,column=n-89)
            b['command']= lambda b=b : data(l.index(b['text']))
            b['bg']=colour[index]
    mainbody()
main_program()
mainloop()
