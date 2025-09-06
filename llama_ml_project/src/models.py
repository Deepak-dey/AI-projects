from pydantic import BaseModel

class PromptRequest(BaseModel):
    prompt:str
    max_length:int = 200
    temperature:float = 0.7
    top_p:float = 0.9
    
    
    