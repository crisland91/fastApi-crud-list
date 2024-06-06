# from pydantic import BaseModel
# from datetime import datetime
# from typing import Optional

# class pub(BaseModel):
#     id: Optional[str]
#     titulo : str
#     descriocion : str
#     create_at : datetime = datetime.now()
#     status : bool = False
    
from typing import Optional
from datetime import datetime
from pydantic import BaseModel

class pub(BaseModel):
    id: Optional[str] = None
    titulo: str
    descripcion: str
    create_at: datetime = datetime.now()
    status: bool = False
