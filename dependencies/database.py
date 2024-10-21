
# SQLALchemy를 사용한 데이터 베이스 연동하기

from sqlalchemy import creatae_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# 파이썬에 내장되어 있는 DB 라이브러리
DB_URL = 'sqlite:///todo.sqlite3'


# 데이터베이스 엔진 생성
# sqlite는 동시에 한 스레드에서만 접근이 가능하다.
engine = create_engine(DB_URL)


# 데이터 베이스 연결 세션 설정
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 모든 모델 클래스가 상속받을 기본 모델 클래스를 지정
Base = declarative_base()
