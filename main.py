import PySimpleGUI as sg
import web_automation


#
# ------ Menu Definition ------ #
# Table Data

def make_window(theme):
    sg.theme(theme)

    menu_def = [
        ['&Menu', ['&About...', '&Keep on Top', '&Not Keep on Top']]]

    right_click_menu_def = [[], ['Paste', 'Exit']]

    input_layout = [[sg.Menu(menu_def, key='-MENU-')],
                    [sg.Checkbox('Enable OneWarehouse', default=False, key='-INPUT enable_onewarehouse-')],
                    [sg.Text('     POST:', size=(7, 1)), sg.Input(key='-INPUT consignment_note-')],
                    [sg.Text('        CID:', size=(7, 1)), sg.Input(key='-INPUT customer_id-')],
                    [sg.Text(' SN/MAC:', size=(7, 1)), sg.Input(key='-INPUT serial_number-')],
                    [sg.Button('Run', size=(10, 1)), sg.Button('Clear', size=(10, 1))],
                    [sg.Image(data=sg.DEFAULT_BASE64_LOADING_GIF, enable_events=True, key='-GIF-IMAGE-')],
                    [sg.Button('Covid Screening', size=(13, 1))]]

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

    return sg.Window('Eddywardward Return Bot V0.7', layout, keep_on_top=True, finalize=True, right_click_menu=right_click_menu_def)


def main():
    consignment_note = ''
    customer_id = ''
    serial_number = ''
    isp_checker = False
    setting = {'Keep on Top': 1, 'Not Keep on Top': 0}
    keys_to_clear = ['-INPUT consignment_note-', '-INPUT customer_id-', '-INPUT serial_number-']

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

        elif event == 'Paste':
            print("[LOG] Clicked Paste!")

        elif event == 'About...':
            print("[LOG] Clicked About!")
            sg.popup('Eddywardward Return Bot', 'E-mail: Edward.Koay@tpgtelecom.com.au', '??2021 Edward Koay',
                     grab_anywhere=True)

        elif event == 'Set Theme':
            print("[LOG] Clicked Set Theme!")
            theme_chosen = values['-THEME LISTBOX-'][0]
            print("[LOG] User Chose Theme: " + str(theme_chosen))
            window.close()
            window = make_window(theme_chosen)

        elif event == 'Run':
            print("[LOG] Clicked Run!")
            consignment_note = values['-INPUT consignment_note-']
            customer_id = values['-INPUT customer_id-']
            serial_number = values['-INPUT serial_number-']
            onewarehouse_checker = values['-INPUT enable_onewarehouse-']
            web_automation.run(consignment_note, customer_id, serial_number, onewarehouse_checker)

        elif event == 'Covid Screening':
            print("[LOG] Clicked Covid Screening!")
            web_automation.covid_screening()

        elif event == 'Clear':
            print("[LOG] Clicked Clear!")
            for key in keys_to_clear:
                window[key]('')

        elif event in setting:
            window.TKroot.wm_attributes("-topmost", setting[event])

    window.close()
    exit(0)


if __name__ == '__main__':
    main()
