from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps
import multiprocessing

app = Flask(__name__)
api = Api(app)

class Predictor(Resource):
    def get(self,A1,A2,A3,A4,A5,A6,A7,A8,A9,A10,A11,A12):
        t = [int(A1),int(A2),int(A3),int(A4),int(A5),int(A6),int(A7),int(A8),int(A9),int(A10),int(A11),int(A12)]
        return exported_pipeline.predict(t)[0]
class Test(Resource):
    def get(self):
        return "Ok!"
    
class Server(Resource):
    def get(self):
        print("Stopping server")
        server.terminate()
        server.join()
        print("Server stopped")
        
api.add_resource(Predictor, '/predict/<A1>/<A2>/<A3>/<A4>/<A5>/<A6>/<A7>/<A8>/<A9>/<A10>/<A11>/<A12>') # Route_1
api.add_resource(Server, '/stop')
api.add_resource(Test, '/test')

def run_server():
    print("Running server in separate thread")
    app.run(port='5002')
    
if __name__ == "__main__":
    print("Staring server")
    server = multiprocessing.Process(target=run_server)
    server.start()
     