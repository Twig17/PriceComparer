from database.ManageCSV import ManageCSV as csvStorage
from database.ManageJSON import ManageJSON as jsonStorage

type = "JSON"


def chooseStorageType():
    if(type == "CSV"):
        return csvStorage
    if (type == "JSON"):
        return jsonStorage
