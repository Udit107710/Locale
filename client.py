from socketIO_client import SocketIO, BaseNamespace
import csv
import json

class NewsNamespace(BaseNamespace):
    def on_connect(self):
        print('connect')

    def on_disconnect(self):
        print('disconnect')

    def on_reconnect(self):
        print('reconnect')

    def on_my_response(self, *args):
        print('on_response', args)

socketIO = SocketIO('localhost', 5000)
booking_namespace = socketIO.define(NewsNamespace, '/test')

socketIO.wait(seconds=1)

with open('Data.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            booking_namespace.emit('my_event', json.dumps(row))
            line_count += 1
    socketIO.wait(seconds=2)
    print(f'Processed {line_count} lines.')