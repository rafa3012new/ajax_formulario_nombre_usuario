from re import T
from tkinter.tix import Tree
from flask_nombre_usuario.config.mysqlconnection import connectToMySQL
import json

#se hace referencia al archivo para evitar el error de referencia circular

NOMBRE_BASE_DATOS = 'ajax_coding_dojo'

# modelar la clase después de la tabla usuario de nuestra base de datos
class Usuario:
    def __init__( self , data ):
        self.id = data['id']
        self.username = data['username']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # ahora usamos métodos de clase para consultar nuestra base de datos
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM usuario;"
        # asegúrate de llamar a la función connectToMySQL con el esquema al que te diriges
        results = connectToMySQL(NOMBRE_BASE_DATOS).query_db(query)
        #print(results,flush=True)
        # crear una lista vacía para agregar nuestras instancias de usuario
        list_results = []
        # Iterar sobre los resultados de la base de datos y crear instancias de authors con cls
        for result in results:
            #print(result,flush=True)
            list_results.append(cls(result) )
        #print(list_results,flush=True)
        #print(list_results[0],flush=True)
        #print(dir(list_results[0]),flush=True)
        #print("antes del return")
        return list_results


    # ahora usamos métodos de clase para consultar nuestra base de datos
    @classmethod
    def get_all_json(cls):
        query = "SELECT * FROM usuario order by id desc;"
        # asegúrate de llamar a la función connectToMySQL con el esquema al que te diriges
        results = connectToMySQL(NOMBRE_BASE_DATOS).query_db(query)
        return results


    # ahora usamos métodos de clase para consultar nuestra base de datos
    @classmethod
    def get_by_id(cls,id):
        #armar la consulta con cadenas f
        query = f"SELECT * FROM usuario where id = %(id)s;"
        #armar el diccionario data con solo el campo id
        data = { 'id' : id }
        # asegúrate de llamar a la función connectToMySQL con el esquema al que te diriges
        results = connectToMySQL(NOMBRE_BASE_DATOS).query_db(query, data)
        #devolver el primer registro de los resultados si resultados devuelve algo sino que devuelva None
        return cls(results[0]) if len(results) > 0 else None

    # ahora usamos métodos de clase para consultar nuestra base de datos
    @classmethod
    def get_by_id_json(cls,id):
        #armar la consulta con cadenas f
        query = f"SELECT * FROM usuario where id = %(id)s;"
        #armar el diccionario data con solo el campo id
        data = { 'id' : id }
        # asegúrate de llamar a la función connectToMySQL con el esquema al que te diriges
        results = connectToMySQL(NOMBRE_BASE_DATOS).query_db(query, data)
        #devolver el primer registro de los resultados si resultados devuelve algo sino que devuelva None
        return results[0] if len(results) > 0 else None



    @classmethod
    def save(cls, data):
        query = f"INSERT INTO usuario (username , email,  created_at, updated_at ) VALUES ( %(username)s , %(email)s, NOW() , NOW() );"
        # data es un diccionario que se pasará al método de guardar desde server.py
        result = connectToMySQL(NOMBRE_BASE_DATOS).query_db( query, data )
        return result



    @classmethod
    def update(cls, data):
        query = f"UPDATE usuario SET username = %(username)s , email = %(email)s updated_at = NOW() WHERE id = %(id)s;"
        resultado = connectToMySQL(NOMBRE_BASE_DATOS).query_db( query, data )
        result = None
        if resultado == None:
            result = cls.get_by_id(data['id'])
        # data es un diccionario que se pasará al método de guardar desde server.py
        return result


    @classmethod
    def delete(cls, id):
        query = "DELETE FROM usuario WHERE id = %(id)s;"
        data = {'id': id}

        print("ejecutando consulta de borrado",end='\n\n',flush=True)
        # print(query)

        resultado = connectToMySQL(NOMBRE_BASE_DATOS).query_db(query, data)

        return resultado
