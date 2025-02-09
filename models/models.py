from practice.dependencies.database import Base
from sqlalchemy import Column, Integer, String, Text, Float 


from sqlalchemy import Column

# String => 고정된 길이 (길이제한)
# Text => 길이제한이 없다.


class Todo(Base):
    __tablename__ = 'calculations'
    # 컬럼 설정 
    id = Column(Integer, primary_key=True, index=True)
    num1 = Column(Float)
    num2 = Column(Float, nullable=True)
    operation = Column(String, index=True)
    result = Column(Float)
