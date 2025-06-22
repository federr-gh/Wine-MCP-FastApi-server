from pydantic import BaseModel

class Wine(BaseModel):
    """
    Model for wine features.
    """
    Alcohol: float
    ácido_málico: float
    Ceniza: float
    Alcalinidad_de_la_ceniza: float
    magnesio: int  
    fenoles_totales: float
    Flavonoides: float
    Fenoles_no_flavonoides: float
    Proantocianinas: float
    intensidad_del_color: float
    Tono: float
    OD280_OD315_de_vinos_diluidos: float
    Prolina: int