from database.ManageCSV import ManageCSV as csvStorage

type = "CSV"


def chooseStorageType():
    if(type == "CSV"):
        return csvStorage
