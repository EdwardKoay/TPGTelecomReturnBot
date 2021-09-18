from selenium import webdriver
from selenium.webdriver.firefox.options import Options

import xlwings as xw


def run(consignment_note, customer_id, serial_number):
    options = Options()
    options.binary_location = r'C:/Program Files/Mozilla Firefox/firefox.exe'
    driver = webdriver.Firefox(firefox_options=options,
                               executable_path=r'C:/Users/Aweso/PycharmProjects/TPGTelecomReturnBot/geckodriver.exe')
    driver.get('https://google.com')

    # Gets the first letter of the serial number
    part_sn1 = serial_number[:1]
    # Gets the first two letters of the serial number
    part_sn2 = serial_number[:2]
    # Gets the first three letters of the serial number
    part_sn3 = serial_number[:3]

    # Defines variables
    modem_type = ''
    auspost_check = False
    equip_found = False

    # Finds the model of the modem/router and sets modem/router type
    if part_sn3 == '984':
        modem_type = 'C1200'
        equip_found = True

    elif (part_sn2 == '00' or part_sn2 == 'CC' or part_sn2 == '1C' or part_sn2 == '50'
          or part_sn2 == '34' or part_sn2 == '7C' or part_sn2 == '74'
          or part_sn2 == '98' or part_sn2 == 'C4' or part_sn2 == 'B0'
          or part_sn2 == 'D8' or part_sn2 == '3C' or part_sn2 == '60'
          or part_sn2 == 'E8' or part_sn2 == 'E4' or part_sn2 == '90'
          or part_sn2 == '28' or part_sn2 == '40' or part_sn2 == 'C0'
          or part_sn2 == '68' or part_sn2 == '00' or part_sn2 == '10'):

        modem_type = 'VR1600v'
        equip_found = True

    elif part_sn2 == '32':
        modem_type = 'VX420'
        equip_found = True
    elif part_sn2 == 'Z2':
        modem_type = 'Dongle'
        equip_found = True
    elif part_sn2 == 'FU':
        modem_type = 'Dongle E5576'
        equip_found = True
    elif part_sn2 == '39':
        modem_type = 'NL1902'
        equip_found = True
    elif part_sn2 == 'CP':
        modem_type = 'TG789'
        equip_found = True
    elif part_sn2 == '89':
        modem_type = 'SIM'
        equip_found = True
    elif part_sn2 == 'BS':
        modem_type = 'CG2200'
        equip_found = True
    elif part_sn2 == '19' or part_sn2 == 'LB':
        modem_type = 'NCD'
        equip_found = True
    elif part_sn3 == '210' or part_sn3 == '95B':
        modem_type = 'NTU'
        equip_found = True
    elif (part_sn2 == '12' or part_sn2 == '78' or part_sn2 == 'A4' or part_sn2 == '13'
          or part_sn2 == '14' or part_sn2 == 'A6' or part_sn2 == 'A5'):
        modem_type = 'NTD'
        equip_found = True
    elif part_sn2 == '33' or part_sn2 == '28':
        modem_type = 'EPC3940L'
        equip_found = True
    elif part_sn2 == '73':
        modem_type = 'H626T'
        equip_found = True
    elif part_sn2 == '93':
        modem_type = 'M616T'
        equip_found = True
    elif part_sn2 == '84' or part_sn2 == '83' or part_sn2 == '82':
        modem_type = 'M605T'
        equip_found = True
    elif part_sn1 == 'H' or part_sn1 == 'E' or part_sn1 == 'K' or part_sn1 == 'J':
        modem_type = 'Fritz!Box7490'
        equip_found = True
    elif part_sn2 == 'A1':
        modem_type = 'BoBLite'
        equip_found = True
    elif part_sn3 == '160':
        modem_type = 'NF12'
        equip_found = True
    elif part_sn3 == '000':
        modem_type = 'A220'
        equip_found = True
    elif part_sn2 == 'J3':
        modem_type = 'HG659'
        equip_found = True
    elif part_sn2 == 'E7':
        modem_type = 'HG658'
        equip_found = True
    elif part_sn2 == 'R6':
        modem_type = 'HG630'
        equip_found = True
    elif part_sn2 == '21':
        modem_type = 'HG532d'
        equip_found = True

    # checks if CID has a .
    if '.' in customer_id:
        auspost_check = True

    # checks if everything is all set and ready to be executed
    if equip_found is True and len(customer_id) < 11 and auspost_check is False:

        # specifies excel spreadsheet to operate on
        filename = 'C:/Users/Aweso/Desktop/2021 09 16 Returns.xlsm'
        wb = xw.Book(filename)
        ws = wb.sheets[0]
        ws.screen_updating = False

        # Sets variables
        staff_name = ws.range('K3').value
        below_last_row = str(ws.range(1, 1).end('down').row + 1)

        # sets the specific variables into the correct column and row of cells
        ws.range('A' + below_last_row).value = serial_number
        ws.range('B' + below_last_row).value = modem_type
        ws.range('H' + below_last_row).value = consignment_note
        ws.range('C' + below_last_row).value = customer_id
        ws.range('K' + below_last_row).value = staff_name
        ws.screen_updating = True
    else:
        print("[LOG] ERROR, Double Check Inputs")


if __name__ == '__main__':
    run()
