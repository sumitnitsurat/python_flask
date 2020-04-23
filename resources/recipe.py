from flask import Response, jsonify, request
from flask_restful import Resource
from database.models import Recipe
from pyexcel_xls import get_data
from services.spreadsheet import fetchExcelFoodList
import os
import json

class RecipeApi(Resource):
    def get(self):
        foodlist = fetchExcelFoodList()
        return foodlist