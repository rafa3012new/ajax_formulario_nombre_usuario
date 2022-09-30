#se importa el app
from unittest import result
from winreg import FlushKey
from wsgiref.util import request_uri
from flask_nombre_usuario import app
#se importa el modelo que contiene la clase
from flask_nombre_usuario.models.usuario import Usuario
#se importa las funciones de flask
from flask import render_template, redirect, request, session, flash, jsonify
#se importan el modulo de fechas
from datetime import datetime


@app.route("/limpiar")
def limpiar():
   session.clear()
   print("se limpio la sesion",flush=True)
   return redirect("/")

@app.route('/')
def menu_principal():
  return render_template("main_usuarios.html")


#Funcion para obtener los registros de todos los dojos
# obtiene todos los dojos y las devuelve en una lista de objetos de los dojos
@app.route('/getall')
def mostrar_autores():
#   print("antes",flush=True)
  resultado = Usuario.get_all_json()
  
  return jsonify(data_json = resultado)


@app.route('/agregarusuariojsondict',methods=['POST'])
def agregar_usuario_json_dict():

   data = request.json
   
   # print(data,flush=True)

   id = Usuario.save(data)
   resultado = []
   
   resultado.append( Usuario.get_by_id_json(id))
   
   print(resultado,flush=True)
   
   if resultado == None:
        print(f"error al crear el usuario {data['username']}",flush=True)

   else:
        print(f"exito al crear el usuario {data['username']}",flush=True)


   return jsonify(data_respuesta_json = resultado)



# #Funcion para crear un dojo en la db con los datos que vienen de un formulario
# #Merodo Post para recibir los datos de un formulario o popupinput
# @app.route('/crearautor',methods=['POST'])
# def crear_autor():

#    data = {"name" : request.form['nombre_autor'],
#            "created_at" : datetime.today(),
#            "updated_at" : datetime.today()}

#    resultado = author.Author.save(data)

#    if resultado == False:
#      print(f"exito al crear el autor {data['name']}",flush=True)
#    else:
#      print(f"error al crear el autor {data['name']}",flush=True)


#    return redirect('/limpiar')


# #Funcion para editar un Autor en la db con los datos que vienen de un formulario o popupinput
# #Metodo Post para recibir los datos de un formulario o popupinput
# @app.route("/actualizarautor", methods=["POST"])
# def actualizar_autor():

#    #la variable data obtiene via request.jason la variable data enviada por fetch desde javascript
#    data =  request.json

#    print(data,flush=True)

#    resultado = author.Author.update(data)

#    if resultado == False:
#       print(f"Error al actualizar el Autor {data['name']}",flush=True)
#    else:
#       print(f"Exito al actualizar el Autor {data['name']}!!!",flush=True)

#    return jsonify(nombre_autor_json = resultado.name)


# #Funcion para eliminar un Autor en la base de datos
# @app.route('/eliminarautor/<int:id>')
# def eliminar_autor(id):

#    #se elimina en el el objeto de la clase Autor
#    author.Author.delete(id)



#    return redirect('/limpiar')




# #Funcion para insertar un nuevo libro
# # se llama al formulario para insertar
# @app.route('/insertarlibro')
# def insertar_libro():
#    return render_template("main_nombre_usuario.html", nombre_usuario=book.Book.get_all())


# #Funcion para crear un registro de un libro
# #Metodo Post
# @app.route('/editarlibro/<int:id>')
# def editar_ninja(id):
#    return render_template("libro_editar.html", nombre_usuario=book.Book.get_all())


# #Funcion para crear un ninja en la db con los datos que vienen de un formulario
# #Metodo Post para recibir los datos de un formulario o popupinput
# @app.route('/crearlibro', methods=['POST'])
# def crear_libro():


#   data = {"title" : request.form['titulo_libro'],
#           "num_of_pages"  : request.form['numero_paginas'],
#           "created_at" : datetime.today(),
#           "updated_at" : datetime.today()}


#   resultado = book.Book.save(data)


#   return redirect('/insertarlibro')



# #Funcion para editar un ninja en la db con los datos que vienen de un formulario
# #Metodo Post para recibir los datos de un formulario o popupinput
# @app.route('/actualizarlibro',methods=['POST'])
# def actualizar_libro():

#   data = {"title"          :request.form['titulo_libro'],
#           "num_of_pages"   :request.form['numero_paginas'],
#           "updated_at"     :datetime.today(),
#           "id"             :request.form['libro_id']
#           }

#   resultado = book.Book.update(data)


#   return redirect('/limpiar')


# #Funcion para eliminar un libro en la base de datos
# @app.route('/eliminarlibro/<int:id>')
# def eliminar_libro(id):

#    #se elimina en el el objeto de la clase libro
#    book.Book.delete(id)


#    return redirect('/insertarlibro')




# #Funcion para obtener los registros de todos los nombre_usuario favoritos de un autor
# @app.route('/mostrarnombre_usuariofavoritosautor/<int:id>')
# def mostrar_nombre_usuario_favoritos_autor(id):
#    nom_lib_fav = []

#    data = {'author_id':id}

#    autoresconnombre_usuariofavoritos = author.Author.get_books_with_authors(data)

#    for i in autoresconnombre_usuariofavoritos.favorites_books:
#       nom_lib_fav.append(i.title)

#    books = book.Book.get_all()


#    return render_template('nombre_usuario_favoritos_autor.html',autores_con_nombre_usuario_favoritos=autoresconnombre_usuariofavoritos,nombre_usuario=books,lista_nombre_usuario_favoritos=nom_lib_fav)




# #Funcion para agregar un libro como favorito de un autor en la db
# # con los datos que vienen de un formulario
# #Metodo Post para recibir los datos de un formulario o popupinput
# @app.route('/agregarlibrofavorito',methods=['POST'])
# def agregarlibrofavorito():

#   data = {"book_id"        :request.form['libro_favorito'],
#           "author_id"      :request.form['autor_favorito'],
#           }

#   favorite.Favorite.save(data)


#   return redirect(f"/mostrarnombre_usuariofavoritosautor/{data['author_id']}")





# #Funcion para agregar un libro como favorito de un autor en la db
# # con los datos que vienen de un formulario
# #Metodo Post para recibir los datos de un formulario o popupinput
# @app.route('/quitarlibrofavorito/<int:book_id>/<int:author_id>')
# def quitarlibrofavorito(book_id, author_id):

#   data = {"book_id"        :book_id,
#           "author_id"      :author_id
#           }

#   favorite.Favorite.delete(data)


#   return redirect(f"/mostrarnombre_usuariofavoritosautor/{data['author_id']}")




# #Funcion para obtener los registros de todos los autores favoritos de un libro
# @app.route('/mostrarautoresfavoritoslibro/<int:id>')
# def mostrar_autores_favoritos_libro(id):
#    nom_aut_fav = []

#    data = {'book_id':id}

#    nombre_usuarioconautoresfavoritos = book.Book.get_authors_with_books(data)

#    for i in nombre_usuarioconautoresfavoritos.favorites_authors:
#       nom_aut_fav.append(i.name)

#    authors = author.Author.get_all()


#    return render_template('autores_favoritos_nombre_usuario.html',nombre_usuario_con_autores_favoritos=nombre_usuarioconautoresfavoritos,autores=authors,lista_autores_favoritos=nom_aut_fav)


# #Funcion para agregar un autor como favorito de un libro en la db
# # con los datos que vienen de un formulario
# #Metodo Post para recibir los datos de un formulario o popupinput
# @app.route('/agregarautorfavorito',methods=['POST'])
# def agregarautorfavorito():

#   data = {"book_id"        :request.form['libro_favorito'],
#           "author_id"      :request.form['autor_favorito'],
#           }

#   favorite.Favorite.save(data)


#   return redirect(f"/mostrarautoresfavoritoslibro/{data['book_id']}")


# #Funcion para agregar un libro como favorito de un autor en la db
# # con los datos que vienen de un formulario
# #Metodo Post para recibir los datos de un formulario o popupinput
# @app.route('/quitarautorfavorito/<int:author_id>/<int:book_id>')
# def quitarautorfavorito( author_id,book_id):

#   data = {"book_id"        :book_id,
#           "author_id"      :author_id
#           }

#   favorite.Favorite.delete(data)


#   return redirect(f"/mostrarautoresfavoritoslibro/{data['book_id']}")

