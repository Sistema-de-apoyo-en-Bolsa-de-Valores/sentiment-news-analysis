# app\domain\model\value_expression.py

from pydantic import BaseModel

class ValueExpression(BaseModel):
    content: str