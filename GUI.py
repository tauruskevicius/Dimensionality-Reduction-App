import PySimpleGUI as sg
sg.ChangeLookAndFeel('dark blue 2')

# GUI layout
PCA_frame_layout = [
[sg.Text(text = 'PCA Parameters', font = ('TimesNewRoman',10,'bold'))],
[sg.Text(text = 'Number of Variables' + ' '*15), sg.Input(default_text = '2', key = '-NUMOFVARPCA-',
                                                      disabled = True,size = (4,1))]
]

FA_frame_layout = [
    [sg.Text(text = 'FAMD Parameters', font = ('TimesNewRoman',10,'bold'))],
    [sg.Text(text = 'Number of Variables' + ' '*15), sg.Input(default_text = '2', key = '-NUMOFVARFA-',
                                                          disabled = True, size = (4,1))],
]

graph_settings_frame = [
    [sg.Text('Color by:')],
    [sg.Listbox(values = (),
                    select_mode = 'single', enable_events = True, 
                   key = '-LISTBOX-', disabled = True, size = (20,20))]
]

settings_column = [
    [sg.Text(text = 'Dimensionality Reduction', text_color = 'white', font = ('Arial',14,'bold'), pad = (0,25))],
    [sg.Image(r'image.png', pad = (10,10))],
    [sg.Input(key='-UPLOADDATA-', enable_events=True, visible=False)],
    [sg.FileBrowse('Upload Dataset', target = '-UPLOADDATA-', button_color=('white', 'Slategray4'),
                   pad =(0,5), size = (14,1), file_types=(("CSV Files", '*.csv'),)),
     sg.Button(button_text = 'View Dataset', key = '-VIEWDATA-', button_color=('white', 'Slategray4'),
               enable_events = True, disabled = True, size = (14,1))],
    [sg.Text(' '*65, key='-FILEUPLOADTEXT-', font = ('Arial',10,'bold'), text_color= 'white')],
    [sg.Frame(title='Numerical Data Set',font = ('TimesNewRoman',10,'bold'), layout = PCA_frame_layout)],
    [sg.Text()], #formatting
    [sg.Frame(title='Mixed Data Set',font = ('TimesNewRoman',10,'bold'), layout = FA_frame_layout)],
    [sg.Text()], #formatting
    [sg.Button(button_text = 'Apply Algorithm', key='-APPLY-', size = (19,1),
               disabled = True, button_color=('White', 'Green'), pad = (38,1))],
    [sg.Text()], [sg.Text()], [sg.Text()],[sg.Text()],[sg.Text()], [sg.Text()],
]
   
graph_column =[
    [sg.Text(' '*62),sg.Text('Graph', text_color='white', font=('Arial',14,'bold'), pad=(0,10))],
    [sg.Canvas(size=(600,500), key = '-CANVAS-')],
    [sg.Text(text = ' ' * 50, k='-VARTEXT-', font=('TimesNewRoman',10,'bold'))],
    [sg.Text(text = ' ' * 100, k='-NOGRAPHTEXT-', font=('TimesNewRoman',10,'bold'))],
    [sg.Text(' '*10),sg.Button("Save Graph", size=(19,1), pad = (5,0), k="-SAVEGRAPH-",
               button_color=('white', 'Slategray4'), disabled = True,),
     sg.Button("Save Reduced Dataset", size=(19,1), pad = (5,0), k="-SAVEDATA-",
               button_color=('white', 'Slategray4'), disabled = True,),
     sg.Button("Exit", size=(19, 1), k='-EXIT-', pad = (5,0), button_color=('White', 'Red')),
     ]
]

grap_settings_column = [
    [sg.Frame(title = 'Graph Parameters',font = ('TimesNewRoman',10,'bold'), layout = graph_settings_frame)]
]

class Gui:    
    # Constructor
    def __init__(self):
        self.layout = [
            [sg.Column(settings_column),
             sg.VSeparator(pad = (10,10)),
             sg.Column(graph_column),
            sg.VSeparator(pad = (10,10)),
            sg.Column(layout = grap_settings_column)]]
        
        self.window = sg.Window("Statistics Tool", self.layout)
        
        
    