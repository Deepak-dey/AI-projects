from fastapi import APIRouter
from fastapi import HTTPException
from .models import PromptRequest
from .services import (generate_text_services,
                       summarize_text_services,
                       sentiment_analyze_services)




router = APIRouter()


@router.get("/")
async def root():
    return {"message": "Hello from FastAPI routes"}


@router.post("/generate")
async def generate_text_endpoint(request:PromptRequest):
    if not request.prompt.strip():
        raise HTTPException(status_code = 400, detail="Prompt cannot be empty")
    
    if request.max_length < 1 or request.max_length >1024:
        raise HTTPException(status_code = 400, detail = "max_lenth msut be in between 1 to 1024")
    
    try:
        result = await generate_text_services(request.prompt,
                           max_length = request.max_length,
                           temperature = request.temperature, 
                           top_p = request.top_p
                           )
        return{"response":result}
    except Exception as e:
        raise HTTPException(status_code = 500, detail = f"Generation failed:{str(e)}")
    
    
    
@router.post("/summarize")
async def summarize_endpoint(request:PromptRequest):
    if not request.prompt.strip():
        raise HTTPException(status_code = 400, detail="Prompt cannot be empty")
    
    try:
        prompt = f"Summarize the following text:\n\n{request.prompt}"
        result = await summarize_text_services(
                                         request.prompt,
                                         max_length = request.max_length
                           )
        return{"summary":result}
    except Exception as e:
        raise HTTPException(status_code = 500, detail = f"Generation failed:{str(e)}")
    
    
    


@router.post("/sentiment")
async def analyze_sentiment(request:PromptRequest):
    if not request.prompt.strip():
        raise HTTPException(status_code = 400, detail="Prompt cannot be empty")
    
    try:
        result= await sentiment_analyze_services(request.prompt)
        return result
    except Exception as e:
        raise HTTPException(status_code = 500, detail = f"Sentiment analysis failed:{str(e)}")  


@router.get("/")
def read_root():
    return {"Hello":"World"}


@router.get("/health")
def health_check():
    return{"status":"ok"}