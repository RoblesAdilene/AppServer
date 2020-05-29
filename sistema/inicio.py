from flask import Flask, render_template, request, redirect, url_for
import pymysql


app = Flask(__name__)

# sesion
app.secret_key = 'mysecretkey'


# Menu Principal
@app.route('/')
def home():
    return render_template("index.html")


## home 
@app.route('/home')

##inicio sesion
@app.route('/iniciar', methods=['POST'])
def iniciar():
    if request.method=='POST':
        usuario = request.form['usuario']
        contra = request.form['contra']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='r_humanos')
        cursor = conn.cursor()
        cursor.execute('select usuario, contraseña from usuarios where usuario=%s and contraseña=%s',(usuario,contra))
        return render_template("home.html")

##Habilidad
@app.route('/habilidad')
def habilidad():
    return render_template("habilidad.html")

@app.route('/habilidad_agr', methods=['POST'])
def habilidad_agr():
    if request.method == 'POST':
        aux_descripcion = request.form['descripcion']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='r_humanos')
        cursor = conn.cursor()
        cursor.execute('insert into habilidad (Descripcion) values (%s)', (aux_descripcion))
        conn.commit()
    return redirect(url_for('agr_datos_habilidad'))

@app.route('/agr_datos_habilidad')
def agr_datos_habilidad():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='r_humanos')
    cursor = conn.cursor()
    cursor.execute('select idHabilidad, Descripcion from habilidad order by Descripcion')
    datos=cursor.fetchall()
    return render_template("tabla_habilidad.html", habs = datos )

@app.route('/bo_habilidad/<string:id>')
def bo_habilidad(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='r_humanos')
    cursor = conn.cursor()
    cursor.execute('delete from habilidad where idHabilidad = {0}'.format(id))
    conn.commit()
    return redirect(url_for('agr_datos_habilidad'))

@app.route('/ed_habilidad/<string:id>')
def ed_habilidad(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='r_humanos')
    cursor = conn.cursor()
    cursor.execute('select idHabilidad, Descripcion from habilidad where idHabilidad = %s', (id))
    dato=cursor.fetchall()
    return render_template("edi_habilidad.html", habs = dato[0])

@app.route('/modifica_habilidad/<string:id>', methods=['POST'])
def modifica_habilidad(id):
    if request.method == 'POST':
        descrip=request.form['descripcion']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='r_humanos')
        cursor = conn.cursor()
        cursor.execute('update habilidad set  Descripcion=%s where idHabilidad=%s',(descrip,id))
        conn.commit()
    return redirect(url_for('agr_datos_habilidad'))


# Carrera
@app.route('/carrera')
def carrera():
    return render_template("carrera.html")

@app.route('/carrera_agr', methods=['POST'])
def carrera_agr():
    if request.method == 'POST':
        aux_descripcion = request.form['descripcion']

        conn = pymysql.connect(host='localhost', user='root', passwd='', db='r_humanos')
        cursor = conn.cursor()
        cursor.execute('insert into carrera (Descripcion) values (%s)', (aux_descripcion))
        conn.commit()
    return redirect(url_for('agr_datos_carrera'))

@app.route('/agr_datos_carrera')
def agr_datos_carrera():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='r_humanos')
    cursor = conn.cursor()
    cursor.execute('select idCarrera, Descripcion from carrera order by Descripcion')
    datos=cursor.fetchall()
    return render_template("tabla_carrera.html", niveles = datos )

@app.route('/bo_carrera/<string:id>')
def bo_carrera(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='r_humanos')
    cursor = conn.cursor()
    cursor.execute('delete from Carrera where idCarrera = {0}'.format(id))
    conn.commit()
    return redirect(url_for('agr_datos_carrera'))

@app.route('/ed_carrera/<string:id>')
def ed_carrera(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='r_humanos')
    cursor = conn.cursor()
    cursor.execute('select idCarrera, Descripcion from Carrera where idCarrera = %s', (id))
    dato=cursor.fetchall()
    return render_template("edi_carrera.html", nivel = dato[0])

@app.route('/modifica_carrera/<string:id>', methods=['POST'])
def modifica_carrera(id):
    if request.method == 'POST':
        descrip=request.form['descripcion']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='r_humanos')
        cursor = conn.cursor()
        cursor.execute('update Carrera set  Descripcion=%s where idCarrera=%s',(descrip,id))
        conn.commit()
    return redirect(url_for('agr_datos_carrera'))


# Medio Publicidad
@app.route('/publicidad')
def publicidad():
    return render_template("publicidad.html")

@app.route('/publicidad_agr', methods=['POST'])
def publicidad_agr():
    if request.method == 'POST':
        aux_descripcion = request.form['nombre_e']

        conn = pymysql.connect(host='localhost', user='root', passwd='', db='r_humanos')
        cursor = conn.cursor()
        cursor.execute('insert into mediopublicidad (Descripcion) values (%s)',
        (aux_descripcion))
        conn.commit()
    return redirect(url_for('agr_datos_publicidad'))

@app.route('/bo_publicidad/<string:id>')
def bo_publicidad(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='r_humanos')
    cursor = conn.cursor()
    cursor.execute('delete from mediopublicidad where idMedioPublicidad = {0}'.format(id))
    conn.commit()
    return redirect(url_for('agr_datos_publicidad'))

@app.route('/agr_datos_publicidad')
def agr_datos_publicidad():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='r_humanos')
    cursor = conn.cursor()
    cursor.execute('select idMedioPublicidad, Descripcion from mediopublicidad order by idMedioPublicidad')
    datos=cursor.fetchall()
    return render_template("tabla_publicidad.html", niveles = datos )

@app.route('/ed_publicidad/<string:id>')
def ed_publicidad(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='r_humanos')
    cursor = conn.cursor()
    cursor.execute('select idMedioPublicidad, Descripcion from mediopublicidad where idMedioPublicidad = %s', (id))
    dato=cursor.fetchall()
    return render_template("edi_publicidad.html", nivel=dato[0])

@app.route('/modifica_publicidad/<string:id>', methods=['POST'])
def modifica_publicidad(id):
    if request.method == 'POST':
        aux_descripcion = request.form['nombre_e']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='r_humanos')
        cursor = conn.cursor()
        cursor.execute('update mediopublicidad set Descripcion=%s where idMedioPublicidad=%s',
                       (aux_descripcion, id))
        conn.commit()
    return redirect(url_for('agr_datos_publicidad'))


# Nivel Academico
@app.route('/nivel_academico')
def nivel_academico():
    return render_template("nivel_academico.html")

@app.route('/nivel_agr', methods=['POST'])
def nivel_agr():
    if request.method == 'POST':
        aux_descripcion = request.form['descripcion']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='r_humanos')
        cursor = conn.cursor()
        cursor.execute('insert into nivelacademico (Descripcion) values (%s)', (aux_descripcion))
        conn.commit()
    return redirect(url_for('agr_datos_nivel_academico'))

@app.route('/bo_nivel/<string:id>')
def bo_nivel(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='r_humanos')
    cursor = conn.cursor()
    cursor.execute('delete from nivelacademico where idNivelAcademico = {0}'.format(id))
    conn.commit()
    return redirect(url_for('agr_datos_nivel_academico'))

@app.route('/agr_datos_nivel_academico')
def agr_datos_nivel_academico():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='r_humanos')
    cursor = conn.cursor()
    cursor.execute('select idNivelAcademico, descripcion from nivelacademico order by descripcion')
    datos=cursor.fetchall()
    return render_template("tabla_nivel_academico.html", niveles = datos )

@app.route('/ed_nivel/<string:id>')
def ed_nivel(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='r_humanos')
    cursor = conn.cursor()
    cursor.execute('select idNivelAcademico, Descripcion from nivelacademico where idNivelAcademico = %s', (id))
    dato=cursor.fetchall()
    return render_template("edi_nivel_academico.html", nivel = dato[0])

@app.route('/modifica_nivel/<string:id>', methods=['POST'])
def modifica_nivel(id):
    if request.method == 'POST':
        descrip=request.form['descripcion']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='r_humanos')
        cursor = conn.cursor()
        cursor.execute('update nivelacademico set  descripcion=%s where idNivelAcademico=%s',(descrip,id))
        conn.commit()
    return redirect(url_for('agr_datos_nivel_academico'))


# Datos de la empresa
@app.route('/datos_empresa')
def datos_empresa():
    return render_template("datos_empresa.html")


@app.route('/datos_empresa_agr', methods=['POST'])
def datos_empresa_agr():
    if request.method == 'POST':
        aux_nombre = request.form['nom_empresa']
        aux_descripcion = request.form['descripcion']
        aux_estructura = request.form['estructura_juridica']
        aux_razon = request.form['razon_social']
        aux_correo = request.form['correo']
        aux_domicilio = request.form['domicilio']
        aux_telefono = request.form['tel']
        aux_encargado = request.form['encargado']
        aux_CIF = request.form['CIF']

        conn = pymysql.connect(host='localhost', user='root', passwd='', db='r_humanos')
        cursor = conn.cursor()
        cursor.execute('insert into datos_de_empresa '
                       '(Nombre_de_empresa, Descripcion, Telefono, Domicilio, E_Mail, RazonSocial, Estructura_Juridica, Encargado, CIF_Empresa) '
                       'values (%s, %s, %s, %s, %s, %s, %s, %s, %s)',
                       (aux_nombre, aux_descripcion, aux_estructura, aux_razon, aux_correo,
                        aux_domicilio, aux_telefono, aux_encargado, aux_CIF))
        conn.commit()
        return redirect(url_for('agr_datos_empresa'))

@app.route('/agr_datos_empresa')
def agr_datos_empresa():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='r_humanos')
    cursor = conn.cursor()
    cursor.execute('select Nombre_de_empresa, Descripcion, Telefono, Domicilio, E_Mail, RazonSocial, '
                   'Estructura_Juridica, Encargado, CIF_Empresa from datos_de_empresa order by Nombre_de_empresa')
    datos=cursor.fetchall()
    return render_template("tabla_datos_empresa.html", niveles = datos )

@app.route('/modificar_datos_empresa/<string:id>', methods=['POST'])
def modificar_datos_empresa(id):
   if request.method == 'POST':
      aux_nombre = request.form['nom_empresa']
      aux_descripcion = request.form['descripcion']
      aux_estructura = request.form['estructura_juridica']
      aux_razon = request.form['razon_social']
      aux_correo = request.form['correo']
      aux_domicilio = request.form['domicilio']
      aux_telefono = request.form['tel']
      aux_encargado = request.form['encargado']
      aux_CIF = request.form['CIF']

      conn = pymysql.connect(host='localhost', user='root', passwd='', db='r_humanos')
      cursor = conn.cursor()
      cursor.execute('update datos_de_empresa set Nombre_de_empresa=%s, '
                     'Descripcion=%s, Telefono=%s, Domicilio=%s, E_Mail=%s, RazonSocial=%s, Estructura_Juridica=%s, '
                     'Encargado=%s, CIF_Empresa=%s where Nombre_de_empresa=%s', (aux_nombre, aux_descripcion, aux_estructura,
                                                                        aux_razon, aux_correo, aux_domicilio,
                                                                        aux_telefono, aux_encargado, aux_CIF, id))
      conn.commit()
   return redirect(url_for('agr_datos_empresa'))

@app.route('/bo_datos_empresa/<string:id>')
def bo_datos_empresa(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='r_humanos')
    cursor = conn.cursor()
    cursor.execute('delete from datos_de_empresa where Nombre_de_empresa = {0}'.format(id))
    conn.commit()
    return redirect(url_for('agr_datos_empresa'))

@app.route('/ed_datos_empresa/<string:id>')
def ed_datos_empresa(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='r_humanos')
    cursor = conn.cursor()
    cursor.execute('select Nombre_de_empresa, Descripcion, Telefono, Domicilio, E_Mail, RazonSocial, '
                   'Estructura_Juridica, Encargado, CIF_Empresa '
                   'from datos_de_empresa where Nombre_de_empresa = %s', (id))
    dato=cursor.fetchall()
    return render_template('edi_datos_empresa.html', nivel=dato[0])


# Puesto

#------------------------------- puesto -------------------------------------------------
@app.route('/puesto')
def puesto():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='r_humanos')
    cursor = conn.cursor()
    cursor.execute('select idPuesto, Descripcion, SalarioAnual, Beneficios, Bonos, Aprobacion from puesto '
                   'order by Descripcion')
    datos = cursor.fetchall()
    return render_template("tabla_puesto.html", puestos=datos)

@app.route('/agrega_puesto', methods=['POST'])
def agrega_puesto():
    if request.method == 'POST':
        aux_des = request.form['descripcion']
        aux_sal = request.form['salario']
        aux_ben = request.form['beneficios']
        aux_bon = request.form['bonos']
        aux_aut = request.form['autorizar']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='r_humanos')
        cursor = conn.cursor()
        cursor.execute('insert into puesto (Descripcion, SalarioAnual, Beneficios, Bonos, Aprobacion) '
                       'values (%s,%s,%s,%s,%s)',(aux_des, aux_sal,aux_ben, aux_bon, aux_aut))
        conn.commit()
        cursor.execute('select idPuesto, Descripcion, SalarioAnual, Beneficios, Bonos, Aprobacion '
                       'from puesto where idPuesto=(select max(idPuesto) from puesto)')
        datos = cursor.fetchall()
        cursor.execute('select a.idPuesto, b.idHabilidad,b.Descripcion,c.idPuesto,c.idHabilidad, c.Experiencia '
                       ' from puesto a, habilidad b,puesto_has_habilidad c '
                       ' where a.idPuesto=c.idPuesto and b.idHabilidad=c.idHabilidad and c.idPuesto=(select max(idPuesto) from puesto)')
        datos1=cursor.fetchall()
        cursor.execute('select a.idPuesto, b.idIdioma,b.Lenguaje,c.idPuesto, c.idIdioma,c.Nivel '
                       'from puesto a, idioma b,puesto_has_idioma c '
                       'where a.idPuesto=c.idPuesto and b.idIdioma=c.idIdioma '
                       'and c.idPuesto=(select max(idPuesto) from puesto)')
        datos2=cursor.fetchall()
        cursor.execute('select idhabilidad, Descripcion from habilidad order by Descripcion')
        datos3 = cursor.fetchall()
        cursor.execute('select idIdioma, Lenguaje from idioma order by Lenguaje')
        datos4 = cursor.fetchall()
        return render_template("edi_puesto.html", puestos = datos, pue_habs=datos1,pue_idis=datos2, habs=datos3, idiomas=datos4 )

@app.route('/nvo_puesto')
def nvo_puesto():
    return render_template("puesto.html")

@app.route('/modifica_puesto/<string:id>', methods=['POST'])
def modifica_puesto(id):
    if request.method == 'POST':
        aux_des =request.form['descripcion']
        aux_sal = request.form['salario']
        aux_ben = request.form['beneficios']
        aux_bon = request.form['bonos']
        aux_aut = request.form['autorizar']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='r_humanos')
        cursor = conn.cursor()
        cursor.execute('update puesto set Descripcion=%s, SalarioAnual=%s, Beneficios=%s, Bonos=%s, Aprobacion=%s '
                       'where idpuesto=%s', (aux_des, aux_sal,aux_ben, aux_bon,aux_aut,id))
        conn.commit()
        return redirect(url_for('puesto'))


@app.route('/ed_puesto/<string:id>')
def ed_puesto(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='r_humanos')
    cursor = conn.cursor()
    cursor.execute('select idPuesto, Descripcion, SalarioAnual, Beneficios, Bonos, Aprobacion '
    'from puesto where idPuesto=%s', (id))
    datos=cursor.fetchall()
    cursor.execute('select a.idPuesto, b.idHabilidad,b.Descripcion,c.idPuesto, c.idHabilidad, c.Experiencia '
    ' from puesto a, habilidad b,puesto_has_habilidad c '
    ' where a.idPuesto=c.idPuesto and b.idHabilidad=c.idHabilidad and c.idPuesto=%s', (id))
    datos1 = cursor.fetchall()
    cursor.execute('select a.idPuesto, b.idIdioma,b.Lenguaje,c.idPuesto, c.idIdioma, c.Nivel '
    'from puesto a, idioma b,puesto_has_idioma c '
    'where a.idPuesto=c.idPuesto and b.idIdioma=c.idIdioma and c.idPuesto=%s', (id))
    datos2=cursor.fetchall()
    cursor.execute('select idhabilidad, Descripcion from habilidad order by Descripcion')
    datos3 = cursor.fetchall()
    cursor.execute('select idIdioma, Lenguaje from idioma order by Lenguaje')
    datos4 = cursor.fetchall()
    return render_template("edi_puesto.html", puestos = datos, pue_habs=datos1,
    pue_idis=datos2, habs=datos3, idiomas=datos4 )

@app.route('/bo_puesto/<string:id>')
def bo_puesto(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='r_humanos')
    cursor = conn.cursor()
    cursor.execute('delete from puesto_has_Idioma where idPuesto = {0}'.format(id))
    conn.commit()
    cursor.execute('delete from puesto_has_habilidad where idPuesto = {0}'.format(id))
    conn.commit()
    cursor.execute('delete from puesto where idPuesto = {0}'.format(id))
    conn.commit()
    return redirect(url_for('puesto'))

@app.route('/agrega_hab_pto', methods=['POST'])
def agrega_hab_pto():
    if request.method == 'POST':
        aux_pto=request.form['pto']
        aux_hab = request.form['habil']
        aux_exp = request.form['expe']
        conn = pymysql.connect(host='localhost', user='root', passwd='',db='r_humanos')
        cursor = conn.cursor()
        cursor.execute('insert into puesto_has_habilidad (idPuesto, idHabilidad,Experiencia) '
                       'values (%s,%s,%s)',(aux_pto,aux_hab,aux_exp))
        conn.commit()
        cursor.execute('select idPuesto, Descripcion, SalarioAnual, Beneficios, Bonos, Aprobacion '
        'from puesto where idPuesto=%s', (aux_pto))
        datos = cursor.fetchall()
        cursor.execute('select a.idPuesto, b.idHabilidad,b.Descripcion,c.idPuesto,c.idHabilidad, c.Experiencia '
        ' from puesto a, habilidad b,puesto_has_habilidad c '
        ' where a.idPuesto=c.idPuesto and b.idHabilidad=c.idHabilidad and c.idPuesto=%s', (aux_pto))
        datos1 = cursor.fetchall()
        cursor.execute('select a.idPuesto, b.idIdioma,b.Lenguaje,c.idPuesto, c.idIdioma, c.Nivel '
        'from puesto a, idioma b,puesto_has_idioma c '
        'where a.idPuesto=c.idPuesto and b.idIdioma=c.idIdioma and c.idPuesto=%s', (aux_pto))
        datos2 = cursor.fetchall()
        cursor.execute('select idhabilidad, Descripcion from habilidad order by Descripcion')
        datos3 = cursor.fetchall()
        cursor.execute('select idIdioma, Lenguaje from idioma order by Lenguaje')
        datos4 = cursor.fetchall()
        return render_template("edi_puesto.html", puestos=datos, pue_habs=datos1,
                               pue_idis=datos2, habs=datos3, idiomas=datos4)

@app.route('/agrega_idio_pto', methods=['POST'])
def agrega_idio_pto():
    if request.method == 'POST':
        aux_pto = request.form['ptoi']
        aux_idi = request.form['idio']
        aux_niv = request.form['nive']
        conn = pymysql.connect(host='localhost', user='root', passwd='',db='r_humanos')
        cursor = conn.cursor()
        cursor.execute('insert into puesto_has_idioma (idPuesto, idIdioma, Nivel) '
                       'values (%s,%s,%s)',(aux_pto,aux_idi,aux_niv))
        conn.commit()
        cursor.execute('select idPuesto, Descripcion, SalarioAnual, Beneficios, Bonos, Aprobacion '
        'from puesto where idPuesto=%s', (aux_pto))
        datos = cursor.fetchall()
        cursor.execute('select a.idPuesto, b.idHabilidad,b.Descripcion,c.idPuesto, c.idHabilidad, c.Experiencia '
        ' from puesto a, habilidad b,puesto_has_habilidad c '
        ' where a.idPuesto=c.idPuesto and b.idHabilidad=c.idHabilidad and c.idPuesto=%s', (aux_pto))
        datos1 = cursor.fetchall()
        cursor.execute('select a.idPuesto, b.idIdioma,b.Lenguaje,c.idPuesto, c.idIdioma, c.Nivel '
        'from puesto a, idioma b,puesto_has_idioma c '
        'where a.idPuesto=c.idPuesto and b.idIdioma=c.idIdioma and c.idPuesto=%s', (aux_pto))
        datos2 = cursor.fetchall()
        cursor.execute('select idhabilidad, Descripcion from habilidad order by Descripcion')
        datos3 = cursor.fetchall()
        cursor.execute('select idIdioma, Lenguaje from idioma order by Lenguaje')
        datos4 = cursor.fetchall()
        return render_template("edi_puesto.html", puestos=datos, pue_habs=datos1,
        pue_idis=datos2, habs=datos3, idiomas=datos4)

@app.route('/bo_hab_pto/<string:idP>/<string:idH>')
def bo_hab_pto(idP,idH):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='r_humanos')
    cursor = conn.cursor()
    cursor.execute('delete from puesto_has_habilidad where idPuesto =%s and idHabilidad=%s',(idP,idH))
    conn.commit()
    cursor.execute('select idPuesto, Descripcion, SalarioAnual, Beneficios, Bonos, Aprobacion '
    'from puesto where idPuesto=%s', (idP))
    datos = cursor.fetchall()
    cursor.execute('select a.idPuesto, b.idHabilidad,b.Descripcion,c.idPuesto, c.idHabilidad, c.Experiencia '
    ' from puesto a, habilidad b,puesto_has_habilidad c '
    ' where a.idPuesto=c.idPuesto and b.idHabilidad=c.idHabilidad and c.idPuesto=%s', (idP))
    datos1 = cursor.fetchall()
    cursor.execute('select a.idPuesto, b.idIdioma,b.Lenguaje,c.idPuesto, c.idIdioma, c.Nivel '
    'from puesto a, idioma b,puesto_has_idioma c '
    'where a.idPuesto=c.idPuesto and b.idIdioma=c.idIdioma and c.idPuesto=%s', (idP))
    datos2 = cursor.fetchall()
    cursor.execute('select idhabilidad, Descripcion from habilidad order by Descripcion')
    datos3 = cursor.fetchall()
    cursor.execute('select idIdioma, Lenguaje from idioma order by Lenguaje')
    datos4 = cursor.fetchall()
    return render_template("edi_puesto.html", puestos=datos, pue_habs=datos1,pue_idis=datos2, habs=datos3, idiomas=datos4)

@app.route('/bo_idi_pto/<string:idP>/<string:idI>')
def bo_idi_pto(idP,idI):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='r_humanos')
    cursor = conn.cursor()
    cursor.execute('delete from puesto_has_idioma where idPuesto =%s and idIdioma=%s',(idP,idI))
    conn.commit()
    cursor.execute('select idPuesto, Descripcion, SalarioAnual, Beneficios, Bonos, Aprobacion '
                   'from puesto where idPuesto=%s', (idP))
    datos = cursor.fetchall()
    cursor.execute('select a.idPuesto, b.idHabilidad,b.Descripcion,c.idPuesto, c.idHabilidad, c.Experiencia '
                   'from puesto a, habilidad b,puesto_has_habilidad c '
                   'where a.idPuesto=c.idPuesto and b.idHabilidad=c.idHabilidad and c.idPuesto=%s', (idP))
    datos1 = cursor.fetchall()
    cursor.execute('select a.idPuesto, b.idIdioma,b.Lenguaje,c.idPuesto, c.idIdioma, c.Nivel '
                   'from puesto a, idioma b,puesto_has_idioma c '
                   'where a.idPuesto=c.idPuesto and b.idIdioma=c.idIdioma and c.idPuesto=%s', (idP))
    datos2 = cursor.fetchall()
    cursor.execute('select idhabilidad, Descripcion from habilidad order by Descripcion')
    datos3 = cursor.fetchall()
    cursor.execute('select idIdioma, Lenguaje from idioma order by Lenguaje')
    datos4 = cursor.fetchall()
    return render_template("edi_puesto.html", puestos=datos, pue_habs=datos1, pue_idis=datos2, habs=datos3, idiomas=datos4)

# Idioma
@app.route('/idioma')
def idioma():
    return render_template("idioma.html")

@app.route('/idioma_agr', methods=['POST'])
def idioma_agr():
    if request.method == 'POST':
        aux_idioma = request.form['fidioma']

        conn = pymysql.connect(host='localhost', user='root', passwd='', db='r_humanos')
        cursor = conn.cursor()
        cursor.execute('insert into idioma (Lenguaje) values (%s)',
        (aux_idioma))
        conn.commit()
    return redirect(url_for('agr_datos_idioma'))

@app.route('/bo_idioma/<string:id>')
def bo_idioma(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='r_humanos')
    cursor = conn.cursor()
    cursor.execute('delete from idioma where idIdioma = {0}'.format(id))
    conn.commit()
    return redirect(url_for('agr_datos_idioma'))

@app.route("/agr_datos_idioma")
def agr_datos_idioma():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='r_humanos')
    cursor = conn.cursor()
    cursor.execute(
    'select idIdioma, Lenguaje from idioma order by Lenguaje')
    datos = cursor.fetchall()
    return render_template("tabla_idioma.html", niveles=datos)

@app.route('/ed_idioma/<string:id>')
def ed_idioma(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='r_humanos')
    cursor = conn.cursor()
    cursor.execute('select idIdioma,Lenguaje from idioma where idIdioma = %s', (id))
    dato=cursor.fetchall()
    return render_template("edi_idioma.html", nivel = dato[0])

@app.route('/modifica_idioma/<string:id>', methods=['POST'])
def modifica_idioma(id):
    if request.method == 'POST':
        aux_idioma = request.form['fidioma']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='r_humanos')
        cursor = conn.cursor()
        cursor.execute('update idioma set  Lenguaje=%s where idIdioma=%s',
        (aux_idioma, id))
        conn.commit()
    return redirect(url_for('agr_datos_idioma'))

#Area
@app.route('/area')
def area():
    return render_template("area.html")

@app.route('/area_agr', methods=['POST'])
def area_agr():
    if request.method == 'POST':
        aux_area = request.form['nom_area']
        aux_descripcion = request.form['desc']

        conn = pymysql.connect(host='localhost', user='root', passwd='', db='r_humanos')
        cursor = conn.cursor()
        cursor.execute('insert into area (AreaNombre, AreaDescripcion) values (%s, %s)',
        (aux_area, aux_descripcion))
        conn.commit()
    return redirect(url_for('agr_datos_area'))

@app.route("/agr_datos_area")
def agr_datos_area():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='r_humanos')
    cursor = conn.cursor()
    cursor.execute('select idArea, AreaNombre, AreaDescripcion from area ')
    datos=cursor.fetchall()
    return render_template("tabla_area.html", areas = datos )

@app.route('/ed_area/<string:id>')
def ed_area(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='r_humanos')
    cursor = conn.cursor()
    cursor.execute('select idArea, AreaNombre, AreaDescripcion from area where idArea = %s', (id))
    dato=cursor.fetchall()
    return render_template("edi_area.html", tarea = dato[0])

@app.route('/modifica_area/<string:id>', methods=['POST'])
def modifica_area(id):
    if request.method == 'POST':
        aux_area = request.form['nom_area']
        aux_descripcion = request.form['desc']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='r_humanos')
        cursor = conn.cursor()
        cursor.execute('update area set AreaNombre=%s, AreaDescripcion=%s where idArea=%s',
                       (aux_area,aux_descripcion, id))
        conn.commit()
    return redirect(url_for('agr_datos_area'))

@app.route('/bo_area/<string:id>')
def bo_area(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='r_humanos')
    cursor = conn.cursor()
    cursor.execute('delete from area where idArea = {0}'.format(id))
    conn.commit()
    return redirect(url_for('agr_datos_area'))



# Contacto
@app.route('/contacto')
def contacto():
    return render_template("contacto.html")

@app.route('/contacto_agr', methods=['POST'])
def contacto_agr():
    if request.method == 'POST':
        aux_nombre = request.form['nombre']
        aux_domicilio = request.form['dom']
        aux_razon = request.form['razon']
        aux_tel = request.form['tel']

        conn = pymysql.connect(host='localhost', user='root', passwd='', db='r_humanos')
        cursor = conn.cursor()
        cursor.execute('insert into contacto (Nombre,Domicilio,Razon_Social,Telefono) values (%s,%s,%s,%s)',
        (aux_nombre, aux_domicilio, aux_razon, aux_tel))
        conn.commit()
    return redirect(url_for('agr_datos_contacto'))

@app.route("/agr_datos_contacto")
def agr_datos_contacto():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='r_humanos')
    cursor = conn.cursor()
    cursor.execute('select idcontacto,Nombre,Domicilio,Razon_Social,Telefono from contacto ')
    datos=cursor.fetchall()
    return render_template("tabla_contacto.html", contactos = datos )

@app.route('/ed_contacto/<string:id>')
def ed_contacto(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='r_humanos')
    cursor = conn.cursor()
    cursor.execute('select idcontacto,Nombre,Domicilio,Razon_Social,Telefono from contacto where idcontacto = %s', (id))
    dato=cursor.fetchall()
    return render_template("edi_Contacto.html", tcontacto = dato[0])

@app.route('/modifica_contacto/<string:id>', methods=['POST'])
def modifica_contacto(id):
    if request.method == 'POST':
        aux_nombre = request.form['nombre']
        aux_domicilio = request.form['dom']
        aux_razon = request.form['razon']
        aux_tel = request.form['tel']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='r_humanos')
        cursor = conn.cursor()
        cursor.execute('update contacto set  Nombre=%s,Domicilio=%s,Razon_Social=%s,Telefono=%s where idcontacto=%s',
                       (aux_nombre, aux_domicilio, aux_razon, aux_tel, id))
        conn.commit()
    return redirect(url_for('agr_datos_contacto'))

@app.route('/bo_contacto/<string:id>')
def bo_contacto(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='r_humanos')
    cursor = conn.cursor()
    cursor.execute('delete from contacto where idcontacto = {0}'.format(id))
    conn.commit()
    return redirect(url_for('agr_datos_contacto'))

#PROCESOS DE LA EMPRESA

#Solicitud
@app.route('/solicitud')
def solicitud():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='r_humanos')
    cursor = conn.cursor()
    cursor.execute('select * from solicitud')
    cursor.execute(
        ' select a.idSolicitud, a.FechaSolicitud, a.idArea, b.AreaNombre, a.idPuesto, c.Descripcion, a.NumeroVacante, a.idEstatus_Solicitud, d.Descripcion '
        ' from solicitud a, area b, puesto c, estatus_solicitud d '
        ' where b.idArea=a.idArea and c.idPuesto=a.idPuesto and d.idEstatus_Solicitud=a.idEstatus_Solicitud ')

    datos = cursor.fetchall()
    return render_template("tabla_solicitud.html", solicitudes=datos)

@app.route('/nvo_solicitud')
def nvo_solicitud():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='r_humanos')
    cursor = conn.cursor()
    cursor.execute('select idArea, AreaNombre from area')
    datos1 = cursor.fetchall()
    cursor.execute('select idPuesto, Descripcion from puesto')
    datos2 = cursor.fetchall()
    cursor.execute('select idNivelAcademico, Descripcion from nivelacademico')
    datos3 = cursor.fetchall()
    cursor.execute('select idCarrera, Descripcion from carrera')
    datos4 = cursor.fetchall()
    cursor.execute('select idEstatus_Solicitud, Descripcion from estatus_solicitud')
    datos5 = cursor.fetchall()
    return render_template("agrega_solicitud.html", areas=datos1, puestos=datos2, niveles=datos3, carreras=datos4, estados=datos5)

@app.route('/agrega_solicitud', methods=['POST'])
def agrega_solicitud():
    if request.method == 'POST':
        aux_fec = request.form['fecha']
        aux_are = request.form['area_sol']
        aux_pue = request.form['Puesto_sol']
        aux_niv = request.form['Nivel_sol']
        aux_car = request.form['Carrera_sol']
        aux_vac = request.form['Vacantes_sol']

        conn = pymysql.connect(host='localhost', user='root', passwd='', db='r_humanos')
        cursor = conn.cursor()

        #---------------------estatus de la solicitud 1 pendiente de aprobacion 2 aprobada (si el puesto------------#
        cursor.execute('select Aprobacion from puesto where idPuesto= %s', (aux_pue))
        req_ap= cursor.fetchone ()
        if req_ap[0]==0:
            # El puesto requiere de autorización
            cursor.execute('insert into solicitud (FechaSolicitud, idArea, idPuesto, idNivelAcademico, idCarrera, '
                           'NumeroVacante, idEstatus_Solicitud) values (%s,%s,%s,%s, %s,%s,1)',(aux_fec, aux_are, aux_pue, aux_niv, aux_car, aux_vac))
        else:
            # El puesto no requiere autorización
            cursor.execute(
                'insert into solicitud (FechaSolicitud, idArea, idPuesto, idNivelAcademico, idCarrera, NumeroVacante, idEstatus_Solicitud) '
                'values (%s,%s,%s,%s, %s,%s,2)',(aux_fec, aux_are, aux_pue, aux_niv, aux_car, aux_vac))

        conn.commit()
        cursor.execute(
            ' select a.idSolicitud, a.FechaSolicitud, a.idArea, b.AreaNombre, a.idPuesto, c.Descripcion, a.NumeroVacante, a.idEstatus_Solicitud, d.Descripcion '
            ' from solicitud a, area b, puesto c, estatus_solicitud d '
            ' where b.idArea=a.idArea and c.idPuesto=a.idPuesto and d.idEstatus_Solicitud=a.idEstatus_Solicitud')

        datos = cursor.fetchall()
    return render_template("tabla_solicitud.html", solicitudes=datos)

@app.route('/ed_solicitud/<string:id>')
def ed_solicitud(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='r_humanos')
    cursor = conn.cursor()
    cursor.execute('select idSolicitud, FechaSolicitud, NumeroVacante, idArea, idPuesto, idNivelAcademico, idCarrera, idEstatus_Solicitud '
                   'from solicitud where idSolicitud=%s',(id))
    datos=cursor.fetchall()
    cursor.execute('select idArea, AreaNombre from area')
    datos1 = cursor.fetchall()
    cursor.execute('select idPuesto, Descripcion from puesto')
    datos2 = cursor.fetchall()
    cursor.execute('select idNivelAcademico, Descripcion from nivelacademico')
    datos3 = cursor.fetchall()
    cursor.execute('select idCarrera, Descripcion from carrera')
    datos4 = cursor.fetchall()
    cursor.execute('select idEstatus_Solicitud, Descripcion from estatus_solicitud')
    datos5 = cursor.fetchall()
    cursor.execute('select NumeroVacante from solicitud')
    datos6 = cursor.fetchall()
    return render_template("edi_solicitud.html", solicitudes=datos, areas=datos1, puestos=datos2, niveles=datos3, carreras=datos4, estados=datos5, vacantes=datos6[0])

@app.route('/modifica_solicitud/<string:id>', methods=['POST'])
def modifica_solicitud(id):
    if request.method == 'POST':
        aux_fec = request.form['fecha']
        aux_are = request.form['area_sol']
        aux_pue = request.form['Puesto_sol']
        aux_niv = request.form['Nivel_sol']
        aux_car = request.form['Carrera_sol']
        aux_vac = request.form['Vacantes_sol']
        aux_est = request.form['Estatus_sol']

        conn = pymysql.connect(host='localhost', user='root', passwd='', db='r_humanos')
        cursor = conn.cursor()

        cursor.execute('update solicitud set FechaSolicitud=%s, idArea=%s, idPuesto=%s, idNivelAcademico=%s, '
                       'idCarrera=%s, NumeroVacante=%s, idEstatus_Solicitud=%s '
                       'where idSolicitud= %s',(aux_fec,aux_are,aux_pue,aux_niv,aux_car,aux_vac,aux_est,id))
        conn.commit()
        cursor.execute(
            ' select a.idSolicitud, a.FechaSolicitud, a.idArea, b.AreaNombre, a.idPuesto, c.Descripcion, a.NumeroVacante, a.idEstatus_Solicitud, d.Descripcion '
            ' from solicitud a, area b, puesto c, estatus_solicitud d '
            ' where b.idArea=a.idArea and c.idPuesto=a.idPuesto and d.idEstatus_Solicitud=a.idEstatus_Solicitud ')

        datos = cursor.fetchall()
    return render_template("tabla_solicitud.html", solicitudes=datos)

@app.route('/bo_solicitud/<string:id>')
def bo_solicitud(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='r_humanos')
    cursor = conn.cursor()
    cursor.execute('delete from solicitud where idsolicitud = {0}'.format(id))
    conn.commit()
    cursor.execute(
        ' select a.idSolicitud, a.FechaSolicitud, a.idArea, b.AreaNombre, a.idPuesto, c.Descripcion, a.NumeroVacante, a.idEstatus_Solicitud, d.Descripcion '
        ' from solicitud a, area b, puesto c, estatus_solicitud d '
        ' where b.idArea=a.idArea and c.idPuesto=a.idPuesto and d.idEstatus_Solicitud=a.idEstatus_Solicitud ')

    datos = cursor.fetchall()
    return render_template("tabla_solicitud.html", solicitudes=datos)

#AutorizaSolicitud
@app.route('/autoriza_solicitud')
def autoriza_solicitud():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='r_humanos')
    cursor = conn.cursor()
    cursor.execute('select * from solicitud')
    cursor.execute(
        ' select a.idSolicitud, a.FechaSolicitud, a.idArea, b.AreaNombre, a.idPuesto, c.Descripcion, a.NumeroVacante, a.idEstatus_Solicitud, d.Descripcion '
        ' from solicitud a, area b, puesto c, estatus_solicitud d '
        ' where b.idArea=a.idArea and c.idPuesto=a.idPuesto and d.idEstatus_Solicitud=a.idEstatus_Solicitud')

    datos = cursor.fetchall()
    return render_template("tabla_autoriza_solicitud.html", solicitudes=datos)

@app.route('/aut_solicitud/<string:id>')
def aut_solicitud(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='r_humanos')
    cursor = conn.cursor()
    cursor.execute('update solicitud set idEstatus_Solicitud=2 where idSolicitud=%s', (id))
    conn.commit()
    cursor.execute(
        ' select a.idSolicitud, a.FechaSolicitud, a.idArea, b.AreaNombre, a.idPuesto, c.Descripcion, a.NumeroVacante, a.idEstatus_Solicitud, d.Descripcion '
        ' from solicitud a, area b, puesto c, estatus_solicitud d '
        ' where b.idArea=a.idArea and c.idPuesto=a.idPuesto and d.idEstatus_Solicitud=a.idEstatus_Solicitud')

    datos = cursor.fetchall()
    return render_template("tabla_autoriza_solicitud.html", solicitudes=datos)

@app.route('/can_solicitud/<string:id>')
def can_solicitud(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='r_humanos')
    cursor = conn.cursor()
    cursor.execute('update solicitud set idEstatus_Solicitud=6 where idSolicitud=%s', (id))
    conn.commit()
    cursor.execute(
        ' select a.idSolicitud, a.FechaSolicitud, a.idArea, b.AreaNombre, a.idPuesto, c.Descripcion, a.NumeroVacante, a.idEstatus_Solicitud, d.Descripcion '
        ' from solicitud a, area b, puesto c, estatus_solicitud d '
        ' where b.idArea=a.idArea and c.idPuesto=a.idPuesto and d.idEstatus_Solicitud=a.idEstatus_Solicitud')

    datos = cursor.fetchall()
    return render_template("tabla_autoriza_solicitud.html", solicitudes=datos)

#Publicacion de Solicitud
@app.route('/a_publicar')
def a_publicar():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='r_humanos')
    cursor = conn.cursor()
    cursor.execute(
        ' select a.idSolicitud, a.FechaSolicitud, a.idArea, b.AreaNombre, a.idPuesto, c.Descripcion, a.NumeroVacante, a.idEstatus_Solicitud, d.Descripcion '
        ' from solicitud a, area b, puesto c, estatus_solicitud d '
        ' where b.idArea=a.idArea and c.idPuesto=a.idPuesto and d.idEstatus_Solicitud=a.idEstatus_Solicitud'
        ' and (a.idEstatus_Solicitud=2 or a.idEstatus_Solicitud=3)')

    datos=cursor.fetchall()
    return render_template("publicacion.html", solicitudes = datos)

@app.route('/crea_pub/<string:id>')
def crea_pub(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='r_humanos')
    cursor = conn.cursor()
    cursor.execute(
        ' select a.idSolicitud, a.FechaSolicitud, a.idArea, b.AreaNombre, a.idPuesto, c.Descripcion, a.NumeroVacante, a.idEstatus_Solicitud, d.Descripcion '
        ' from solicitud a, area b, puesto c, estatus_solicitud d '
        ' where b.idArea=a.idArea and c.idPuesto=a.idPuesto and d.idEstatus_Solicitud=a.idEstatus_Solicitud'
        ' and (a.idEstatus_Solicitud=2 or a.idEstatus_Solicitud=3) and idSolicitud=%s', (id))

    dato = cursor.fetchone()
    cursor.execute(
        ' SELECT a.idAnuncio, a.Num_Solicitantes, a.FechaPublicacion, a.FechaCierre, b.Nombre, c.Descripcion '
        ' from anuncio a, contacto b, mediopublicidad c '
        ' where b.idcontacto=a.idcontacto and c.idMedioPublicidad=a.idMedioPublicidad and a.idSolicitud=%s',(id))
    datos = cursor.fetchall()

    cursor.execute(' select idcontacto, nombre from contacto order by nombre ')
    datos1 = cursor.fetchall()
    cursor.execute(' select idMedioPublicidad, Descripcion from mediopublicidad order by Descripcion ')
    datos2 = cursor.fetchall()
    return render_template("crea_publicacion.html", sol=dato, publicaciones=datos, contactos=datos1, medios=datos2)

@app.route('/agrega_publicacion', methods=['POST'])
def agrega_publicacion():
    if request.method == 'POST':
        aux_sol = request.form['n_solicitud']
        aux_fep = request.form['fecha_pub']
        aux_fec = request.form['fecha_cie']
        aux_solicitantes = request.form['n_solicitantes']
        aux_con = request.form['contacto']
        aux_med = request.form['medio']

        conn = pymysql.connect(host='localhost', user='root', passwd='', db='r_humanos')
        cursor = conn.cursor()

        #El Puesto requiere de Autorizacion
        cursor.execute(' insert into anuncio (idSolicitud, Num_Solicitantes, FechaPublicacion, FechaCierre, idcontacto, idMedioPublicidad) '
                       ' values (%s,%s,%s,%s,%s,%s)', ( aux_sol, aux_solicitantes, aux_fep, aux_fec, aux_con, aux_med ))
        conn.commit()
        cursor.execute(' update solicitud set idEstatus_Solicitud=3 where idSolicitud=%s', (aux_sol))
        conn.commit()
        cursor.execute(
            ' select a.idSolicitud, a.FechaSolicitud, a.idArea, b.AreaNombre, a.idPuesto, c.Descripcion, a.NumeroVacante, a.idEstatus_Solicitud, d.Descripcion '
            ' from solicitud a, area b, puesto c, estatus_solicitud d '
            ' where b.idArea=a.idArea and c.idPuesto=a.idPuesto and d.idEstatus_Solicitud=a.idEstatus_Solicitud'
            ' and (a.idEstatus_Solicitud=2 or a.idEstatus_Solicitud=3) and idSolicitud=%s', (aux_sol))

        dato = cursor.fetchone()
        cursor.execute(
            ' SELECT a.idAnuncio, a.Num_Solicitantes, a.FechaPublicacion, a.FechaCierre, b.Nombre, c.Descripcion '
            ' from anuncio a, contacto b, mediopublicidad c '
            ' where b.idcontacto=a.idcontacto and c.idMedioPublicidad=a.idMedioPublicidad and a.idSolicitud=%s', (aux_sol))
        datos = cursor.fetchall()

        cursor.execute(' select idcontacto, nombre from contacto order by nombre ')
        datos1 = cursor.fetchall()
        cursor.execute(' select idMedioPublicidad, Descripcion from mediopublicidad order by Descripcion ')
        datos2 = cursor.fetchall()
        return render_template("crea_publicacion.html", sol=dato, publicaciones=datos, contactos=datos1, medios=datos2)

@app.route('/bo_publicacion/<string:id>')
def bo_publicacion(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='r_humanos')
    cursor = conn.cursor()
    cursor.execute(' select idSolicitud from anuncio where idanuncio = {0}'.format(id))
    aux_sol=cursor.fetchone()
    cursor = conn.cursor()
    cursor.execute(' delete from anuncio where idanuncio = {0}'.format(id))
    conn.commit()
    cursor.execute(
        ' select a.idSolicitud, a.FechaSolicitud, a.idArea, b.AreaNombre, a.idPuesto, c.Descripcion, a.NumeroVacante, a.idEstatus_Solicitud, d.Descripcion '
        ' from solicitud a, area b, puesto c, estatus_solicitud d '
        ' where b.idArea=a.idArea and c.idPuesto=a.idPuesto and d.idEstatus_Solicitud=a.idEstatus_Solicitud'
        ' and (a.idEstatus_Solicitud=2 or a.idEstatus_Solicitud=3) and idSolicitud=%s', (aux_sol[0]))

    dato = cursor.fetchone()
    cursor.execute(
        ' SELECT a.idAnuncio, a.Num_Solicitantes, a.FechaPublicacion, a.FechaCierre, b.Nombre, c.Descripcion '
        ' from anuncio a, contacto b, mediopublicidad c '
        ' where b.idcontacto=a.idcontacto and c.idMedioPublicidad=a.idMedioPublicidad and a.idSolicitud=%s', (aux_sol[0]))
    datos = cursor.fetchall()

    cursor.execute(' select idcontacto, nombre from contacto order by nombre ')
    datos1 = cursor.fetchall()
    cursor.execute(' select idMedioPublicidad, Descripcion from mediopublicidad order by Descripcion ')
    datos2 = cursor.fetchall()
    return render_template("crea_publicacion.html", sol=dato, publicaciones=datos, contactos=datos1, medios=datos2)


##Candidato
@app.route('/candidato')
def candidato():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='r_humanos')
    cursor = conn.cursor()
    cursor.execute(' select Curp, Nombre from candidato order by Nombre')
    datos=cursor.fetchall()
    return render_template("tabla_candidato.html", candidatos = datos)

@app.route('/agrega_candidato', methods=['POST'])
def agrega_candidato():
    if request.method == 'POST':
        aux_cur =request.form['curp']
        aux_nom = request.form['nombre']
        aux_dom = request.form['domicilio']
        aux_tel = request.form['telefono']
        aux_cor = request.form['correoe']
        aux_eda = request.form['edad']
        aux_nss = request.form['nss']
        aux_sex = request.form['sexo']
        aux_eci = request.form['edociv']
        aux_rfc = request.form['rfc']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='r_humanos')
        cursor = conn.cursor()
        cursor.execute('insert into candidato (Curp, Nombre, Domicilio, Telefono, E_Mail, Sexo, Edad, NSS, RFC, idEstadoCivil)'
                       ' values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(aux_cur, aux_nom, aux_dom, aux_tel, aux_cor, aux_sex, aux_eda, aux_nss,aux_rfc, aux_eci))
        conn.commit()

        cursor.execute('select Curp, Nombre, Domicilio, Telefono, E_Mail, Sexo, Edad, NSS, RFC, idEstadoCivil'
                       ' from candidato where Curp=%s',(aux_cur))
        datos=cursor.fetchall()

        cursor.execute('select a.Curp, b.idHabilidad, b.Descripcion, c.Curp, c.idHabilidad, c.Experiencia'
                       ' from candidato a, habilidad b, candidato_has_habilidad c'
                       ' where a.Curp=c.Curp and b.idHabilidad=c.idHabilidad and c.Curp=%s',(aux_cur))
        datos1=cursor.fetchall()

        cursor.execute('select a.Curp, b.idIdioma, b.Lenguaje, c.Curp, c.idIdioma, c.Nivel'
                       ' from candidato a, idioma b, candidato_has_idioma c'
                       ' where a.Curp=c.Curp and b.idIdioma=c.idIdioma and c.Curp=%s',(aux_cur))
        datos2 = cursor.fetchall()

        cursor.execute(
            ' select a.Curp, b.idNivelAcademico, b.Descripcion, c.idCarrera, c.Descripcion, d.Curp, d.idNivelAcademico, d.idCarrera, d.Institucion'
            ' from candidato a, nivelacademico b, carrera c, candidato_has_nivelacademico d'
            ' where a.Curp=d.Curp and b.idNivelAcademico=d.idNivelAcademico and c.idCarrera=d.idCarrera and d.Curp=%s',(aux_cur))
        datos6 = cursor.fetchall()

        cursor.execute(' select idhabilidad, Descripcion from habilidad order by Descripcion')
        datos3 = cursor.fetchall()

        cursor.execute(' select idIdioma, Lenguaje from idioma order by Lenguaje')
        datos4 = cursor.fetchall()

        cursor.execute(' select idNivelAcademico, Descripcion from nivelacademico order by Descripcion')
        datos7 = cursor.fetchall()

        cursor.execute('select idCarrera, Descripcion from carrera order by Descripcion')
        datos8=cursor.fetchall()

        cursor.execute(' select idEstadoCivil, Descripcion from estadocivil')
        datos5 = cursor.fetchall()
        return render_template("edi_candidato.html", carrera_can=datos8,candidatos=datos, can_habs=datos1, can_idis=datos2,can_acas=datos6, habs=datos3, idiomas=datos4,nivel_academico=datos7, ecivil=datos5)


@app.route('/nvo_candidato')
def nvo_candidato():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='r_humanos')
    cursor = conn.cursor()
    cursor.execute('select idEstadoCivil, Descripcion from estadocivil order by Descripcion')
    datos5 = cursor.fetchall()
    return render_template("candidato.html", ecivil=datos5)


@app.route('/modifica_candidato/<string:Curp>', methods=['POST'])
def modifica_candidato(Curp):
    if request.method == 'POST':
        aux_cur = request.form['curp']
        aux_rfc = request.form['rfc']
        aux_nom = request.form['nombre']
        aux_dom = request.form['domicilio']
        aux_tel = request.form['telefono']
        aux_cor = request.form['correoe']
        aux_eda = request.form['edad']
        aux_nss = request.form['nss']
        aux_sex = request.form['sexo']
        aux_eci = request.form['edociv']

        conn = pymysql.connect(host='localhost', user='root', passwd='', db='r_humanos')
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE candidato 
            SET RFC=%s, Nombre=%s, Domicilio=%s, Telefono=%s, E_Mail=%s, Sexo=%s, Edad=%s, NSS=%s, idEstadoCivil=%s
            WHERE Curp=%s
        """,(aux_rfc,aux_nom,aux_dom,aux_tel,aux_cor,aux_sex,aux_eda,aux_nss,aux_eci,Curp))
        conn.commit()
        return redirect(url_for('candidato'))

@app.route('/ed_candidato/<string:Curp>')
def ed_candidato(Curp):
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='r_humanos')
        cursor = conn.cursor()
        cursor.execute(' select Curp, Nombre, Domicilio, Telefono, E_Mail, Sexo, Edad, NSS, RFC, idEstadoCivil'
                       ' from candidato where Curp=%s',(Curp))
        datos=cursor.fetchall()

        cursor.execute(' select a.Curp, b.idHabilidad, b.Descripcion, c.Curp, c.idHabilidad, c.Experiencia'
                       ' from candidato a, habilidad b, candidato_has_habilidad c'
                       ' where a.Curp=c.Curp and b.idHabilidad=c.idHabilidad and c.Curp=%s',(Curp))
        datos1=cursor.fetchall()

        cursor.execute(' select a.Curp, b.idIdioma, b.Lenguaje, c.Curp, c.idIdioma, c.Nivel'
                       ' from candidato a, idioma b, candidato_has_idioma c'
                       ' where a.Curp=c.Curp and b.idIdioma=c.idIdioma and c.Curp=%s',(Curp))
        datos2 = cursor.fetchall()

        cursor.execute(' select a.Curp, b.idNivelAcademico, b.Descripcion, c.idCarrera, c.Descripcion, d.Curp, d.idNivelAcademico, d.idCarrera, d.Institucion'
                       ' from candidato a, nivelacademico b, carrera c, candidato_has_nivelacademico d'
                       ' where a.Curp=d.Curp and b.idNivelAcademico=d.idNivelAcademico and c.idCarrera=d.idCarrera and d.Curp=%s',(Curp))
        datos6 = cursor.fetchall()

        cursor.execute(' select idhabilidad, Descripcion from habilidad order by Descripcion')
        datos3 = cursor.fetchall()

        cursor.execute(' select idIdioma, Lenguaje from idioma order by Lenguaje')
        datos4 = cursor.fetchall()

        cursor.execute(' select idNivelAcademico, Descripcion from nivelacademico order by Descripcion')
        datos7 = cursor.fetchall()

        cursor.execute(' select Curp,Sexo from candidato where Curp=%s',(Curp))
        sexos = cursor.fetchall()

        cursor.execute('select idCarrera, Descripcion from carrera order by Descripcion')
        datos8=cursor.fetchall()

        cursor.execute(' select idEstadoCivil, Descripcion from estadocivil')
        datos5 = cursor.fetchall()
        return render_template("edi_candidato.html", sexo=sexos,carrera_can=datos8, candidatos=datos, can_habs=datos1, can_idis=datos2,can_acas=datos6, habs=datos3, idiomas=datos4, nivel_academico=datos7, ecivil=datos5)

@app.route('/agrega_hab_can', methods=['POST'])
def agrega_hab_can():
    if request.method == 'POST':
        aux_can = request.form['can']
        aux_hab = request.form['habil']
        aux_exp = request.form['expe']
        conn = pymysql.connect(host='localhost', user='root', passwd='',db='r_humanos')
        cursor = conn.cursor()
        cursor.execute('insert into candidato_has_habilidad (Curp, idHabilidad, Experiencia) '
                       'values (%s,%s,%s)',(aux_can,aux_hab,aux_exp))
        conn.commit()
        cursor.execute(' select Curp, Nombre, Domicilio, Telefono, E_Mail, Sexo, Edad, NSS, RFC, idEstadoCivil'
                       ' from candidato where Curp=%s', (aux_can))
        datos = cursor.fetchall()
        cursor.execute(' select a.Curp, b.idHabilidad, b.Descripcion, c.Curp, c.idHabilidad, c.Experiencia'
                       ' from candidato a, habilidad b, candidato_has_habilidad c'
                       ' where a.Curp=c.Curp and b.idHabilidad=c.idHabilidad and c.Curp=%s', (aux_can))
        datos1 = cursor.fetchall()

        cursor.execute(' select a.Curp, b.idIdioma, b.Lenguaje, c.Curp, c.idIdioma, c.Nivel'
                       ' from candidato a, idioma b, candidato_has_idioma c'
                       ' where a.Curp=c.Curp and b.idIdioma=c.idIdioma and c.Curp=%s', (aux_can))
        datos2 = cursor.fetchall()

        cursor.execute(
            ' select a.Curp, b.idNivelAcademico, b.Descripcion, c.idCarrera, c.Descripcion, d.Curp, d.idNivelAcademico, d.idCarrera, d.Institucion'
            ' from candidato a, nivelacademico b, carrera c, candidato_has_nivelacademico d'
            ' where a.Curp=d.Curp and b.idNivelAcademico=d.idNivelAcademico and c.idCarrera=d.idCarrera and d.Curp=%s',(aux_can))
        datos6 = cursor.fetchall()

        cursor.execute(' select idhabilidad, Descripcion from habilidad order by Descripcion')
        datos3 = cursor.fetchall()

        cursor.execute(' select idIdioma, Lenguaje from idioma order by Lenguaje')
        datos4 = cursor.fetchall()

        cursor.execute(' select idNivelAcademico, Descripcion from nivelacademico order by Descripcion')
        datos7 = cursor.fetchall()

        cursor.execute('select idCarrera, Descripcion from carrera order by Descripcion')
        datos8 = cursor.fetchall()

        cursor.execute(' select idEstadoCivil, Descripcion from estadocivil')
        datos5 = cursor.fetchall()
        return render_template("edi_candidato.html", carrera_can=datos8, candidatos=datos, can_habs=datos1,
                               can_idis=datos2,
                               can_acas=datos6, habs=datos3, idiomas=datos4, nivel_academico=datos7, ecivil=datos5)


@app.route('/agrega_idio_can', methods=['POST'])
def agrega_idio_can():
    if request.method == 'POST':
        aux_can = request.form['cani']
        aux_idi = request.form['idio']
        aux_niv = request.form['nive']
        conn = pymysql.connect(host='localhost', user='root', passwd='',db='r_humanos')
        cursor = conn.cursor()
        cursor.execute('insert into candidato_has_idioma (Curp, idIdioma, Nivel) '
                       'values (%s,%s,%s)',(aux_can,aux_idi,aux_niv))
        conn.commit()
        cursor.execute(' select Curp, Nombre, Domicilio, Telefono, E_Mail, Sexo, Edad, NSS, RFC, idEstadoCivil'
                       ' from candidato where Curp=%s', (aux_can))
        datos = cursor.fetchall()
        cursor.execute(' select a.Curp, b.idHabilidad, b.Descripcion, c.Curp, c.idHabilidad, c.Experiencia'
                       ' from candidato a, habilidad b, candidato_has_habilidad c'
                       ' where a.Curp=c.Curp and b.idHabilidad=c.idHabilidad and c.Curp=%s', (aux_can))
        datos1 = cursor.fetchall()

        cursor.execute(' select a.Curp, b.idIdioma, b.Lenguaje, c.Curp, c.idIdioma, c.Nivel'
                       ' from candidato a, idioma b, candidato_has_idioma c'
                       ' where a.Curp=c.Curp and b.idIdioma=c.idIdioma and c.Curp=%s', (aux_can))
        datos2 = cursor.fetchall()

        cursor.execute(
            ' select a.Curp, b.idNivelAcademico, b.Descripcion, c.idCarrera, c.Descripcion, d.Curp, d.idNivelAcademico, d.idCarrera, d.Institucion'
            ' from candidato a, nivelacademico b, carrera c, candidato_has_nivelacademico d'
            ' where a.Curp=d.Curp and b.idNivelAcademico=d.idNivelAcademico and c.idCarrera=d.idCarrera and d.Curp=%s',(aux_can))
        datos6 = cursor.fetchall()

        cursor.execute(' select idhabilidad, Descripcion from habilidad order by Descripcion')
        datos3 = cursor.fetchall()

        cursor.execute(' select idIdioma, Lenguaje from idioma order by Lenguaje')
        datos4 = cursor.fetchall()

        cursor.execute(' select idNivelAcademico, Descripcion from nivelacademico order by Descripcion')
        datos7 = cursor.fetchall()

        cursor.execute('select idCarrera, Descripcion from carrera order by Descripcion')
        datos8=cursor.fetchall()

        cursor.execute(' select idEstadoCivil, Descripcion from estadocivil')
        datos5 = cursor.fetchall()
        return render_template("edi_candidato.html", carrera_can=datos8, candidatos=datos, can_habs=datos1, can_idis=datos2,
            can_acas=datos6, habs=datos3, idiomas=datos4,nivel_academico=datos7, ecivil=datos5)


@app.route('/agrega_aca_can', methods=['POST'])
def agrega_aca_can():
    if request.method == 'POST':
        aux_can = request.form['cana']
        aux_nivel = request.form['nivel']
        aux_carr = request.form['carrera']
        aux_ins = request.form['insti']
        conn = pymysql.connect(host='localhost', user='root', passwd='',db='r_humanos')
        cursor = conn.cursor()
        cursor.execute('insert into candidato_has_nivelacademico (Curp, idNivelAcademico,idCarrera, Institucion) '
                       'values (%s,%s,%s,%s)',(aux_can,aux_nivel,aux_carr,aux_ins))
        conn.commit()
        cursor.execute(' select Curp, Nombre, Domicilio, Telefono, E_Mail, Sexo, Edad, NSS, RFC, idEstadoCivil'
                       ' from candidato where Curp=%s', (aux_can))
        datos = cursor.fetchall()
        cursor.execute(' select a.Curp, b.idHabilidad, b.Descripcion, c.Curp, c.idHabilidad, c.Experiencia'
                       ' from candidato a, habilidad b, candidato_has_habilidad c'
                       ' where a.Curp=c.Curp and b.idHabilidad=c.idHabilidad and c.Curp=%s', (aux_can))
        datos1 = cursor.fetchall()

        cursor.execute(' select a.Curp, b.idIdioma, b.Lenguaje, c.Curp, c.idIdioma, c.Nivel'
                       ' from candidato a, idioma b, candidato_has_idioma c'
                       ' where a.Curp=c.Curp and b.idIdioma=c.idIdioma and c.Curp=%s', (aux_can))
        datos2 = cursor.fetchall()

        cursor.execute(' select a.Curp, b.idNivelAcademico, b.Descripcion, c.idCarrera, c.Descripcion, d.Curp, d.idNivelAcademico, d.idCarrera, d.Institucion'
                       ' from candidato a, nivelacademico b, carrera c, candidato_has_nivelacademico d'
                       ' where a.Curp=d.Curp and b.idNivelAcademico=d.idNivelAcademico and c.idCarrera=d.idCarrera and d.Curp=%s',(aux_can))
        datos6 = cursor.fetchall()

        cursor.execute(' select idhabilidad, Descripcion from habilidad order by Descripcion')
        datos3 = cursor.fetchall()

        cursor.execute(' select idIdioma, Lenguaje from idioma order by Lenguaje')
        datos4 = cursor.fetchall()

        cursor.execute(' select idNivelAcademico, Descripcion from nivelacademico order by Descripcion')
        datos7 = cursor.fetchall()

        cursor.execute('select idCarrera, Descripcion from carrera order by Descripcion')
        datos8=cursor.fetchall()

        cursor.execute(' select idEstadoCivil, Descripcion from estadocivil')
        datos5 = cursor.fetchall()
        return render_template("edi_candidato.html", carrera_can=datos8,candidatos=datos, can_habs=datos1, 
            can_idis=datos2,can_acas=datos6, habs=datos3, idiomas=datos4,nivel_academico=datos7, ecivil=datos5)

@app.route('/bo_hab_can/<string:idC>/<string:idH>')
def bo_hab_can(idC,idH):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='r_humanos')
    cursor = conn.cursor()
    cursor.execute('delete from candidato_has_habilidad where Curp =%s and idHabilidad=%s',(idC,idH))
    conn.commit()
    cursor.execute(' select Curp, Nombre, Domicilio, Telefono, E_Mail, Sexo, Edad, NSS, RFC, idEstadoCivil from candidato where Curp=%s',(idC))
    datos = cursor.fetchall()
    cursor.execute(' select a.Curp, b.idHabilidad, b.Descripcion, c.Curp, c.idHabilidad, c.Experiencia'
                   ' from candidato a, habilidad b, candidato_has_habilidad c'
                   ' where a.Curp=c.Curp and b.idHabilidad=c.idHabilidad and c.Curp=%s',(idC))
    datos1 = cursor.fetchall()

    cursor.execute(' select a.Curp, b.idIdioma, b.Lenguaje, c.Curp, c.idIdioma, c.Nivel'
                   ' from candidato a, idioma b, candidato_has_idioma c'
                   ' where a.Curp=c.Curp and b.idIdioma=c.idIdioma and c.Curp=%s',(idC))
    datos2 = cursor.fetchall()

    cursor.execute(
        ' select a.Curp, b.idNivelAcademico, b.Descripcion, c.idCarrera, c.Descripcion, d.Curp, d.idNivelAcademico, d.idCarrera, d.Institucion'
        ' from candidato a, nivelacademico b, carrera c, candidato_has_nivelacademico d'
        ' where a.Curp=d.Curp and b.idNivelAcademico=d.idNivelAcademico and c.idCarrera=d.idCarrera and d.Curp=%s',(idC))
    datos6 = cursor.fetchall()

    cursor.execute(' select idhabilidad, Descripcion from habilidad order by Descripcion')
    datos3 = cursor.fetchall()

    cursor.execute(' select idIdioma, Lenguaje from idioma order by Lenguaje')
    datos4 = cursor.fetchall()

    cursor.execute(' select idNivelAcademico, Descripcion from nivelacademico order by Descripcion')
    datos7 = cursor.fetchall()

    cursor.execute('select idCarrera, Descripcion from carrera order by Descripcion')
    datos8=cursor.fetchall()

    cursor.execute(' select idEstadoCivil, Descripcion from estadocivil')
    datos5 = cursor.fetchall()

    return render_template("edi_candidato.html", carrera_can=datos8,candidatos=datos, can_habs=datos1, can_idis=datos2, can_acas=datos6,
                           habs=datos3, idiomas=datos4, nivel_academico=datos7, ecivil=datos5)


@app.route('/bo_idi_can/<string:idC>/<string:idI>')
def bo_idi_can(idC,idI):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='r_humanos')
    cursor = conn.cursor()
    cursor.execute('delete from candidato_has_idioma where Curp =%s and idIdioma=%s',(idC,idI))
    conn.commit()
    cursor.execute(
        ' select Curp, Nombre, Domicilio, Telefono, E_Mail, Sexo, Edad, NSS, RFC, idEstadoCivil from candidato where Curp=%s',
        (idC))
    datos = cursor.fetchall()
    cursor.execute(' select a.Curp, b.idHabilidad, b.Descripcion, c.Curp, c.idHabilidad, c.Experiencia'
                   ' from candidato a, habilidad b, candidato_has_habilidad c'
                   ' where a.Curp=c.Curp and b.idHabilidad=c.idHabilidad and c.Curp=%s', (idC))
    datos1 = cursor.fetchall()

    cursor.execute(' select a.Curp, b.idIdioma, b.Lenguaje, c.Curp, c.idIdioma, c.Nivel'
                   ' from candidato a, idioma b, candidato_has_idioma c'
                   ' where a.Curp=c.Curp and b.idIdioma=c.idIdioma and c.Curp=%s', (idC))
    datos2 = cursor.fetchall()

    cursor.execute(
        ' select a.Curp, b.idNivelAcademico, b.Descripcion, c.idCarrera, c.Descripcion, d.Curp, d.idNivelAcademico, d.idCarrera, d.Institucion'
        ' from candidato a, nivelacademico b, carrera c, candidato_has_nivelacademico d'
        ' where a.Curp=d.Curp and b.idNivelAcademico=d.idNivelAcademico and c.idCarrera=d.idCarrera and d.Curp=%s',(idC))
    datos6 = cursor.fetchall()

    cursor.execute(' select idhabilidad, Descripcion from habilidad order by Descripcion')
    datos3 = cursor.fetchall()

    cursor.execute(' select idIdioma, Lenguaje from idioma order by Lenguaje')
    datos4 = cursor.fetchall()

    cursor.execute(' select idNivelAcademico, Descripcion from nivelacademico order by Descripcion')
    datos7 = cursor.fetchall()

    cursor.execute('select idCarrera, Descripcion from carrera order by Descripcion')
    datos8 = cursor.fetchall()

    cursor.execute(' select idEstadoCivil, Descripcion from estadocivil')
    datos5 = cursor.fetchall()

    return render_template("edi_candidato.html", carrera_can=datos8, candidatos=datos, can_habs=datos1, can_idis=datos2,
                           can_acas=datos6, habs=datos3, idiomas=datos4, nivel_academico=datos7, ecivil=datos5)


@app.route('/bo_aca_can/<string:idC>/<string:idA>')
def bo_aca_can(idC, idA):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='r_humanos')
    cursor = conn.cursor()
    cursor.execute("delete from `candidato_has_nivelacademico` where Curp = '%s' and idNivelAcademico='%s'"%(idC,idA))
    conn.commit()
    cursor.execute(
        ' select Curp, Nombre, Domicilio, Telefono, E_Mail, Sexo, Edad, NSS, RFC, idEstadoCivil from candidato where Curp=%s',(idC))
    datos = cursor.fetchall()
    cursor.execute(' select a.Curp, b.idHabilidad, b.Descripcion, c.Curp, c.idHabilidad, c.Experiencia'
                   ' from candidato a, habilidad b, candidato_has_habilidad c'
                   ' where a.Curp=c.Curp and b.idHabilidad=c.idHabilidad and c.Curp=%s', (idC))
    datos1 = cursor.fetchall()

    cursor.execute(' select a.Curp, b.idIdioma, b.Lenguaje, c.Curp, c.idIdioma, c.Nivel'
                   ' from candidato a, idioma b, candidato_has_idioma c'
                   ' where a.Curp=c.Curp and b.idIdioma=c.idIdioma and c.Curp=%s', (idC))
    datos2 = cursor.fetchall()

    cursor.execute(
        ' select a.Curp, b.idNivelAcademico, b.Descripcion, c.idCarrera, c.Descripcion, d.Curp, d.idNivelAcademico, d.idCarrera, d.Institucion'
        ' from candidato a, nivelacademico b, carrera c, candidato_has_nivelacademico d'
        ' where a.Curp=d.Curp and b.idNivelAcademico=d.idNivelAcademico and c.idCarrera=d.idCarrera and d.Curp=%s',(idC))
    datos6 = cursor.fetchall()

    cursor.execute(' select idhabilidad, Descripcion from habilidad order by Descripcion')
    datos3 = cursor.fetchall()

    cursor.execute(' select idIdioma, Lenguaje from idioma order by Lenguaje')
    datos4 = cursor.fetchall()

    cursor.execute(' select idNivelAcademico, Descripcion from nivelacademico order by Descripcion')
    datos7 = cursor.fetchall()

    cursor.execute('select idCarrera, Descripcion from carrera order by Descripcion')
    datos8 = cursor.fetchall()

    cursor.execute(' select idEstadoCivil, Descripcion from estadocivil')
    datos5 = cursor.fetchall()

    return render_template("edi_candidato.html", carrera_can=datos8, candidatos=datos, can_habs=datos1, can_idis=datos2,
                           can_acas=datos6,
                           habs=datos3, idiomas=datos4, nivel_academico=datos7, ecivil=datos5)

@app.route('/bo_candidato/<string:Curp>')
def bo_candidato(Curp):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='r_humanos')
    cursor = conn.cursor()
    cursor.execute("delete from `candidato_has_idioma` where Curp = '%s'"%(Curp))
    conn.commit()
    cursor.execute("delete from `candidato_has_habilidad` where Curp = '%s'"%(Curp))
    conn.commit()
    cursor.execute("delete from `candidato_has_nivelacademico` where Curp = '%s'" % (Curp))
    conn.commit()
    cursor.execute("delete from `candidato` where Curp = '%s'"%(Curp))
    conn.commit()
    return redirect(url_for('candidato'))


if __name__ == "__main__":
    app.run(debug=True, port=5000)
