import psycopg2

class Session_bdd:

    def abrir(self):
        conexion = psycopg2.connect(database="proyectobdd", user="postgres", password="postgres")
        return conexion

    #EJEMPLO SACADO DE MI RPOYECTO DE BDD XDXDXD
    '''def consulta(self, datos_sesion):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select correo, password from usuarios where correo=%s and password=%s"
        cursor.execute(sql, datos_sesion)
        data = cursor.fetchone()
        print(data)
        return data '''