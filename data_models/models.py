from pydantic import BaseModel

class RagToolSchema(BaseModel):
    """Schema for RAG Tool"""
    question: str

class QuestionRequest(BaseModel):
    """Schema for Question Request"""
    question: str

