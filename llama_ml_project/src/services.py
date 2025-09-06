import asyncio
from transformers import pipeline

generator = pipeline("text-generation",model = "gpt2") #meta-llama/Llama-2-7b-chat-hf
sammarizer = pipeline("summarization",model="sshleifer/distilbart-cnn-12-6")
sentiment = pipeline("sentiment-analysis")


async def generate_text_services(prompt:str,max_length:int = 200 ,temperature:float = 0.7,top_p:float = 0.9):
    def run():
        return generator(prompt,
                        max_length = max_length,
                        do_sample =True,
                        temperature = temperature,
                        top_p = top_p)
    result = await asyncio.to_thread( run )
    text = result[0]['generated_text'] or result[0].get('text') or str(result[0])
    return{"response":text}


async def summarize_text_services(prompt:str,max_length:int):
    input_len = len(prompt.split())
    max_len = min(max_length,max(10,input_len//2))
    min_len = min(20,max_length-1)
    
    prompt = f"Summarize the following text:\n\n{prompt}"
    result = await asyncio.to_thread( sammarizer,
                                        prompt,
                                        max_length = max_len,
                                        min_length=min_len
                        )
    return{"summary":result[0]["summary_text"]}



async def sentiment_analyze_services(prompt:str):
    output = await asyncio.to_thread(sentiment, prompt)
    label = output[0]['label']
    score = output[0]['score']
    return{"label":label,"score":score}
    
    



    