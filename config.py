import os

BASE_DIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))   # 데이터 베이스 주소
SQLALCHEMY_TRACK_MODIFICATIONS = False                                               #SQLAlchemy의 이벤트 처리옵션
                                                                                     # 비활 False

# SQLite는 어떤 데이터베이스일까?
#  파이썬 기본 패키지에 포함된 SQLite는 주로 소규모 프로젝트에서 사용하는 가벼운 파일을 기반으로 한 데이터베이스다.
#  보통은 SQLite로 개발을 빠르게 진행하고 이후 실제 운영 시스템에 반영할 때에는 좀 더 규모가 큰 데이터베이스를 사용한다.


