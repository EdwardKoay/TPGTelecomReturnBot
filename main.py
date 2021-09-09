# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import PySimpleGUI as sg
import Selenium
#
# ------ Menu Definition ------ #

def make_window(theme):
    sg.theme(theme)

    menu_def = [
        ['&Help', ['&About...']]]

    right_click_menu_def = [[], ['Nothing', 'More Nothing', 'Exit']]

    # Table Data
    data = [["John", 10], ["Jen", 5]]
    headings = ["Name", "Score"]

    input_layout = [[sg.Menu(menu_def, key='-MENU-')],
                    [sg.Radio('TPG', "RadioDemo", default=True, size=(10, 1), k='-R1-'),
                     sg.Radio('iiNet', "RadioDemo", default=True, size=(10, 1), k='-R2-')],
                    [sg.Text('CN:'), sg.Input(key='-INPUT CN-')],
                    [sg.Text('CID:'), sg.Input(key='-INPUT CID-')],
                    [sg.Text('S/N|MAC:'), sg.Input(key='-INPUT S/N-')],
                    [sg.Button('Run'), sg.Button('Clear')],
                    [sg.Image(data=sg.DEFAULT_BASE64_LOADING_GIF, enable_events=True, key='-GIF-IMAGE-')]]

    logging_layout = [[sg.Text("Anything printed will display here!")], [sg.Output(size=(60, 15), font='Courier 8')]]

    theme_layout = [[sg.Text("See how elements look under different themes by choosing a different theme here!")],
                    [sg.Listbox(values=sg.theme_list(),
                                size=(20, 12),
                                key='-THEME LISTBOX-',
                                enable_events=True)],
                    [sg.Button("Set Theme")]]

    layout = [[sg.Text('Returns Program', size=(38, 1), justification='center', font=("Helvetica", 16),
                       relief=sg.RELIEF_RIDGE, k='-TEXT HEADING-', enable_events=True)]]
    layout += [[sg.TabGroup([[sg.Tab('Input Elements', input_layout),
                              sg.Tab('Output Screen', logging_layout),
                              sg.Tab('Theming', theme_layout)]], key='-TAB GROUP-')]]

    return sg.Window('Eddywardward Return Bot 0.1', layout, right_click_menu=right_click_menu_def)


def main():
    CN = 'CN'
    CID = 'CID'
    SN = 'SN'

    window = make_window(sg.theme())

    while True:
        event, values = window.read(timeout=100)
        # keep an animation running so show things are happening
        window['-GIF-IMAGE-'].update_animation(sg.DEFAULT_BASE64_LOADING_GIF, time_between_frames=100)
        if event not in (sg.TIMEOUT_EVENT, sg.WIN_CLOSED):
            print('============ Event = ', event, ' ==============')
            print('-------- Values Dictionary (key=value) --------')
            for key in values:
                print(key, ' = ', values[key])

        if event in (None, 'Exit'):
            print("[LOG] Clicked Exit!")
            break

        elif event == 'About...':
            print("[LOG] Clicked About!")
            sg.popup('Eddywardward Return Bot', 'E-mail: Edward.Koay@tpgtelecom.com.au', '©2021 Edward Koay',
                     grab_anywhere=True)

        elif event == "Set Theme":
            print("[LOG] Clicked Set Theme!")
            theme_chosen = values['-THEME LISTBOX-'][0]
            print("[LOG] User Chose Theme: " + str(theme_chosen))
            window.close()
            window = make_window(theme_chosen)

        elif event == 'Run':
            CN = values['-INPUT CN-']
            CID = values['-INPUT CID-']
            SN = values['-INPUT S/N-']
            print("[LOG] You entered ", CN, CID, SN)
            Selenium.main(CN, CID, SN)
    window.close()
    exit(0)


if __name__ == '__main__':
    main()
