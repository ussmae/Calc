import pandas as pd

def input_to_Excel(user_data):
    Pb_Ch = user_data["Pb_Ch"]
    Pb_Num = user_data["Pb_Num"]
    Pb_Mtd = user_data["Pb_Mtd"]
    Shade_On = user_data["Shade_On"]
    AllGraph = user_data["AllGraph"]
    contour_line = user_data["contour_line"]


    Pb_path = f"\엑셀\\15.{Pb_Ch}.xlsx"
    df = pd.read_excel(Pb_path, sheet_name=Pb_Mtd, dtype = str)
    Pb_xlsx = df.iloc[Pb_Num + 1].tolist()

    Pb_temp = {
        "Coordinates": Pb_Mtd,
        "0var": {"from": Pb_xlsx[1], "to": Pb_xlsx[2]},
        "1var": {"from": Pb_xlsx[3], "to": Pb_xlsx[4]},
        "2var": {"from": Pb_xlsx[5], "to": Pb_xlsx[6]},
        "AllGraph" : AllGraph,
        "Shade" : Shade_On,
        "contour" : contour_line
    }
    return Pb_temp

    # Pb_path = "C:\coding\\templates\Prbl_db.json"

    # with open(Pb_path, "w") as Pbp:
    #     json.dump(Pb_temp, Pbp, indent=4)