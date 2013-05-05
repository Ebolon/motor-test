from motor import MotorClient, Op
from tornado import gen, ioloop

db = MotorClient(host="127.0.0.1").open_sync()['motor_example']

@gen.engine
def push_user(name):
    c = {'name': name, 'fields': []}
    yield Op(db.user.insert, c)

@gen.engine
def get_user(name):
    user = yield Op(db.user.find_one, {'name': name})
    print user


if __name__ == '__main__':
    #push_user('Simon')
    #get_user('Simon')
    ioloop.IOLoop.instance().start()
