# from app import app

# # @app.route('/')
# # def index():
# #     return "Hello, World!"

# @app.route('/<name>') # ADDED
# def greet(name): # ADDED
#     return f"Hello {name}!"  # ADDED

from app import app

@app.route('/')
# AS BEFORE


@app.route('/<name>') # ADDED
def greet(name): # ADDED
    return f"Hello {name}!"  # ADDED