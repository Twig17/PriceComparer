from websitesOnboard.ManageNewegg import ManageNewegg as newegg

type = "Newegg"


def chooseStorageType():
    if(type == "Newegg"):
        return newegg()
