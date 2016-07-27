import helper.winutils as winutils, datetime
from helper.manage import FileManagement
import shutil


def main_station():
    msg = {
        's1': '...copying now',
        's2': '...copy complete',
        'e1': 'path looks to be invalid',
        'e2': '...error occurred while transferring',
    }

    file_name = "\\"

    unc_target = '\\\' + file_name
    unc_destination = '\\\'
    file = FileManagement()

    if file.confirm(unc_target):
        print('{}'.format(msg['s1']))

        date_format = "%Y_%b_%d_%M_%S"  # 2016_Jul_27_12_08
        today = datetime.datetime.today()
        #  print('{}'.format(today.strftime(format)))
        folder_creation_name = unc_destination + '\\' + today.strftime(date_format)
        print(folder_creation_name)
        file.create(folder_creation_name)

        try:
            winutils.copy(src=unc_target, dst=folder_creation_name)
        # shutil.copy2(UNC, Destination) #
        except:
            print("unable to completed")

    else:
        print('{}'.format(msg['e1']))
        return False

    if file.confirm(folder_creation_name + file_name):
        print('{}'.format(msg['s2']))

    else:
        print('{}'.format(msg['e2']))
        return False
