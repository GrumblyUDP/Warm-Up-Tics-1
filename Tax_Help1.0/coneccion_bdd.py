import psycopg2

class main:

    def abrir(self): #Se conecta a la base de datos, modificar parametros dependiendo de tu contraseña o nombre de la database local
        conexion = psycopg2.connect(database="warmuptest", user="postgres", password="admin")
        return conexion

    def alta(self, tupla): #Registra el usuario
        cone=self.abrir()
        cursor=cone.cursor()
        sql = "insert into usuario(rut,nombre) values (%s,%s)"
        cursor.execute(sql, tupla)
        cone.commit()


    def consulta(self, datos_sesion):#busca el usuario en la base de datos para el logini
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select rut, nombre from usuario where rut=%s and nombre=%s"
        cursor.execute(sql, datos_sesion)
        data = cursor.fetchone()
        print(data)
        return data

    def ingreso_honorarios_brutos(self, honorarios):
        cone = self.abrir()
        cursor = cone.cursor()

        sql = "insert into tabla_honorarios values (honorarios[0],honorarios[1],honorarios[2],honorarios[3],honorarios[4],honorarios[5],honorarios[6],honorarios[7],honorarios[8],honorarios[9],honorarios[10],honorarios[11],honorarios[12], honorarios[13])"
        cursor.execute(sql, honorarios)
        cone.commit()

    def obtencion_porcentaje_honorario(self):
        cone = self.abrir()
        cursor = cone.cursor()
        sql = "select porcen from porcentaje where annio='2021'"
        cursor.execute(sql)
        data = cursor.fetchone()[0] #regresa el primer dato de la tupla
        return data
    def obtencion_honorarios_mensuales(self, rut_sesion):
        cone = self.abrir()
        cursor = cone.cursor()
        sql = "select lastval(),mes1,mes2,mes3,mes4,mes5,mes6,mes7,mes8,mes9,mes10,mes11,mes12 from tabla_honorarios where rut=%s"
        cursor.execute(sql)
        data = cursor.fetchone()  # regresa el primer dato de la tupla
        return data

    def obtencion_retencion_honorario_mensual(arr_honorarios_mensuales):
        retencion_honorario_mensual = []
        #porcentaje = obtencion_porcentaje_honorario(self)
        for x in arr_honorarios_mensuales:

            retencion_honorario_mensual.append(arr_honorarios_mensuales)

    def obtencion_limite_presuncion(self):
        cone = self.abrir()
        cursor = cone.cursor()
        sql = "select limite from tabla_presuncion where annio='2021'"
        cursor.execute(sql)
        data = cursor.fetchone()[0]  # regresa el primer dato de la tupla
        return data

    def obtencion_datos_factor(self,renta_imponible_anual):
        arr_indexing= []
        arr_indexing.append(renta_imponible_anual)

        cone = self.abrir()
        cursor = cone.cursor()
        sql = "select factor,cant_rebajar from tabla_ria where annio='2021' and  final >= %s"
        cursor.execute(sql, arr_indexing)
        data = cursor.fetchone()  # regresa el primer dato de la tupla
        return data

    def calculos(self):
        cone = self.abrir()
        cursor = cone.cursor()
