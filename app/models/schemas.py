from pydantic import BaseModel
from typing import List

class Message(BaseModel):
    user: str
    content: str

class ChatCompletion(BaseModel):
    message: List[Message]
  
class ChatCompletionResponse(BaseModel):
    message: Message