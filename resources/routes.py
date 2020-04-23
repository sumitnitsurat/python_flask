from .recipe import RecipeApi

def initialize_routes(api):
    api.add_resource(RecipeApi, '/api/recipes')
