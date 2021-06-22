from flask import Blueprint

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/hello')
def hello_pybo():
    return 'Hello , Pybo!'


# bp는 Blueprint  클래스로 생성한 객체를 의미한다. Blueprint 클래스로 생성할때는
# 이름 모듈명 URL 프리픽스 값을 전달해야한다.
# 블루 프린트는 큰 application 단순화 시키는 역할을 하고 fk extension(확장 프로그램) 등록을 위한 수단으로 쓰인다.
# fk 는 jgo 와달리 url을 파일 단위에서 따로 간리하지 않고 controller 의 endpoint 함수에 데코레이터를 붙여서 관리한다.
# 라우트함수 @app,route 들 기능이 필요할 때마다 계속 추가되어야 하기 때문에 create_app 함수내에 함수가 많을 경우 번거럽다.
# Blueprint을 이용하면 라우트 보다  구조적으로 관리할 수있다 .

@bp.route('/')
def index():
    return 'Pybo index'
