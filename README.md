# - 패키지 구조
```
C:\Users\80417\Desktop\bohyun/fastapi homework

|   calculation.sqlite3
|   main.py
|
+---dependencies
|       database.py
|
+---models
|       models.py
|
+---schemas
|       schemas.py
|
+---service
|       calculate_crud.py
|
\---__pycache__
        calculate_crud.cpython-312.pyc
        database.cpython-312.pyc
        main.cpython-312.pyc
        models.cpython-312.pyc
        schemas.cpython-312.pyc
```


# - 패키지 분리 이유

1. 모듈화 : 패키지를 사용해 각 모듈이 책임을 지도록 했다.

2. 재사용성 : 특정 기능을 수행하는 코드를 다른 프로젝트에서도 재사용할 수 있도록 했다.

3. 유지보수 : 코드의 특정 부분을 수정할때, 해당 패키지만 수정 하면 되서 유지보수가 용이하다.

4. 가독성: 관련된 기능들을 그룹화해서 코드의 가독성을 향상시켰다.


# - 추가기능 설명
- 계산한 내용을 데이터베이스에 저장하여 기록들을 볼 수 있게 추가했다. 

