from flask import Flask, render_template, request, send_file, url_for, jsonify
import os
import pandas as pd

app = Flask(__name__)

# Ruta para el archivo Excel
EXCEL_FILE = 'datos_formulario.xlsx'

# Ruta para el formulario
@app.route('/', methods=['GET', 'POST'])
def formulario():

    
    if request.method == 'POST':
        datos = {}

        # Valores para las listas desplegables
        
        datos['GRUPOS CUPS']=[request.form.get('grupos_cups')]
        datos['CUPS']=int(request.form.get('CUPS'))
        datos['ENUNCIADO CUPS Resolución 2336 de 2023']=[request.form.get('enunciado_cups')]
        datos['Concepto_Especialidad']=[request.form.get('concepto_especialidad')]
        datos['Grupo trabajo']=[request.form.get('grupo_trabajo_piloto')]
        datos['Brigada']=[request.form.get('brigada')]
        datos['Responsable Clinico']=[request.form.get('responsable_clinico')]
        datos['Apoyo']=[request.form.get('apoyo')]
        datos['Responsable ingenieria']=[request.form.get('responsable_ingenieria')]
        #Gris
        datos['Grupos/subgrupos']=[request.form.get('grupos_subgrupos')]
        datos['Descripción del procedimiento (no estructurada)']=[request.form.get('descripcion_no_estructurada')]
        datos['fuente_0']=[request.form.get('fuente_0')]
        #Rosado
        datos['Tipo de procedimiento- naturaleza']=[request.form.get('tipo_procedimiento_naturaleza')]
        datos['fuente_1']=[request.form.get('fuente_1')]
        datos['Accion ejercida']=[request.form.get('accion_ejercida')]
        datos['fuente_2']=[request.form.get('fuente_2')]
        datos['Estructura/órgano/región anatomica']=[request.form.get('estr_org_reg')]
        datos['fuente_3']=[request.form.get('fuente_3')]
        datos['tecnica']=[request.form.get('tecnica')]
        datos['fuente_4']=[request.form.get('fuente_4')]
        datos['Vía de abordaje']=[request.form.get('via_abordaje')]
        datos['fuente_5']=[request.form.get('fuente_5')]
        datos['Dispositivo médico que define el procedimiento']=[request.form.get('DM_Procedimiento')]
        datos['Nombre dispositivo médico']=[request.form.get('nombre_DM')]
        datos['Tipo de dispositivo médico'] = [request.form.get('tipo_DM')]
        datos['codigo UDI-ID o GMDN dispositivo médico'] = [request.form.get('cod_DM')]
        datos['Clase de riesgo dispositivo médico'] = [request.form.get('clase_DM')]
        datos['fuente_6'] = [request.form.get('fuente_6')]
        datos['Especialidad'] = [request.form.get('especialidad')]
        datos['fuente_7'] = [request.form.get('fuente_7')]
        datos['Intervención'] = [request.form.get('intervencion')]
        datos['fuente_8'] = [request.form.get('fuente_8')]
        datos['Agente/metabolito'] = [request.form.get('agente_metabolito')]
        datos['fuente_9'] = [request.form.get('fuente_9')]
        datos['Tipo de muestra'] = [request.form.get('tipo_muestra')]
        datos['fuente_10'] = [request.form.get('fuente_10')]
        datos['Definición del procedimiento (segun estructura semántica)'] = [request.form.get('def_procedimiento')]
        #Verde_turquesa
        datos['Proposito']=[request.form.get('proposito')]
        datos['fuente_11']=[request.form.get('fuente_11')]
        datos['Finalidad']=[request.form.get('finalidad')]
        datos['fuente_12']=[request.form.get('fuente_12')]
        datos['Ambito']=[request.form.get('ambito_habilitacion')]
        datos['fuente_13']=[request.form.get('fuente_13')]
        datos['Modalidad']=[request.form.get('modalidad')]
        datos['fuente_14']=[request.form.get('fuente_14')]
        datos['Area clínica o disciplina del conocimiento']=[request.form.get('area_clinica_disciplina')]
        datos['fuente_15']=[request.form.get('fuente_15')]
        datos['Diagnóstico relacionado CIE 10'] = [request.form.get('dx_cie10')]
        datos['Diagnóstico relacionado CIE 11'] = [request.form.get('dx_cie11')]
        datos['Grado de invasividad']=[request.form.get('invasividad')]
        datos['fuente_16']=[request.form.get('fuente_16')]
        datos['Riesgos']=[request.form.get('riesgo_paciente')]
        datos['fuente_17']=[request.form.get('fuente_17')]
        datos['Cantidad DM']=[request.form.get('cantidad_dm')]  
        cantidad_dm = int(request.form.get('cantidad_dm'))    
        for i in range(1, cantidad_dm + 1):
            datos[f"Otros dispositivos esenciales: Nombre dispositivo médico {i}"] = [request.form.get(f"nombre_dm_{i}")]
            datos[f"Otros dispositivos esenciales: Tipo dispositivo médico {i}"] = [request.form.get(f"tipo_dm_{i}")]
            datos[f"Otros dispositivos esenciales: Código UDI-ID o GMDN dispositivo médico {i}"] = [request.form.get(f"codigo_dm_{i}")]
            datos[f"Otros dispositivos esenciales: Clase de riesgo dispositivo médico {i}"] = [request.form.get(f"clas_riesgo_dm_{i}")]
            datos[f"fuente_dm_{i}"] = [request.form.get(f"fuente_dm_{i}")]
        datos['Método de análisis']=[request.form.get('metodo')]
        datos['fuente_18']=[request.form.get('fuente_18')]
        datos['Temperatura de conservación']=[request.form.get('temperatura')]
        datos['fuente_19']=[request.form.get('fuente_19')]
        # Lila
        datos['Extensor 1']=[request.form.get('extensores_1')]
        datos['Extensor 2']=[request.form.get('extensores_2')]
        datos['Extensor 3']=[request.form.get('extensores_3')]
        # Naranja
        datos['Evidencia que desaconseje su uso actual']=[request.form.get('evidencia_uso')]
        datos['Dicotomizada obsolescencia evidencia científica']=[request.form.get('dicotomia_obselencia_ci')]
        datos['fuente_20']=[request.form.get('fuente_20')]
        datos['Opinión clinica que desaconseje su uso actual']=[request.form.get('opinion_clinica')]
        datos['Dicotomizada obsolescencia evidencia clínica']=[request.form.get('dicotomia_obselencia_cl')]
        datos['fuente_21']=[request.form.get('fuente_21')]
        datos['Frecuencia de uso (categoría por percentil)']=[request.form.get('frecuencia_uso')]
        datos['Obsolecencia (regla de decisión: evidencia que desaconseje su uso u opinión clínica que desaconseja su uso + baja frecuencia (no explicada por prevalencia de la condición o indicación del procedimiento)']=[request.form.get('obsolescencia')]
        #azul
        datos['Procedimiento que realice la misma función'] = [request.form.get('pro_funcion')]
        datos['fuente_22'] = [request.form.get('fuente_22')]
        datos['Procedimiento que realice la misma función con: mayor efectividad, seguridad o sea más especifico'] = [request.form.get('pro_mejor_funcion')]
        #verde_amarilloso
        datos['Codigo ICHI'] = [request.form.get('codigo_ichi')]
        datos['Descripción ICHI objetivo'] = [request.form.get('des_ichi_objetivo')]
        datos['Descripción ICHI acción'] = [request.form.get('des_ichi_accion')]
        datos['Descripción ICHI medio'] = [request.form.get('des_ichi_medio')]
        datos['Descripción ICHI procedimiento'] = [request.form.get('des_ichi_procedimiento')]

        


        # Convertir los datos a un DataFrame de pandas
        df = pd.DataFrame(datos)

        # Verificar si el archivo Excel ya existe
        if os.path.exists(EXCEL_FILE):
            # Si existe, lo abrimos y agregamos los nuevos datos
            df_existente = pd.read_excel(EXCEL_FILE)
            df_combinado = pd.concat([df_existente, df], ignore_index=True)
            df_combinado =df_combinado.groupby('CUPS').last().reset_index()
            df_combinado.to_excel(EXCEL_FILE, index=False)
        else:
            # Si no existe, creamos uno nuevo
            df.to_excel(EXCEL_FILE, index=False)
        
        # Redirigir a la página de descarga del archivo Excel
        return '''
        Datos recibidos y almacenados. <br>
        <a href="/descargar">Descargar archivo Excel</a>
        '''

        return f"Datos recibidos: {datos}"
    
    grupos_cups_options = ['Quirúrgico', 'No quirúrgico - Consulta' , 'No quirúrgico - Monitoreo', 'No quirúrgico - Diagnóstico', 'No quirúrgico - Terapéutico/Intervención',  'No quirúrgico - Otro', 'Imangenología', 'Laboratorio clínico', 'Odontológico']
    tipo_procedimiento_naturaleza_options = ['Quirúrgico', 'No quirúrgico', 'No aplica']
    accion_ejercida_options = ['Ablación', 'Anastomosis', 'Destrucción/Fragmentación', 'Dilatación', 'Drenaje', 'Extracción', 'Fijación', 'Incisión', 'Reparación', 'Reemplazo', 'Revascularización', 'Escisión', 'Resección',  'Extirpación', 'Abrasión', 'Alteración', 
                               'Aspiración o succión', 'Creación', 'División', 'Eliminación o Remoción', 'Implantación', 'Inserción', 'Liberación', 'Reimplantación', 'Reposición', 'Restricción', 'Revisión', 'Adaptación', 'Evaluación', 'Consulta', 'Control', 'Infiltración',
                               'Infusión', 'Internación', 'Irrigación', 'Lavado', 'Limpieza', 'Lisis', 'Medición', 'Obtención', 'Oclusión', 'Perfusión', 'Recolección', 'Reducción', 'Reintervención', 'Remodelación', 'Reparación', 'Resección', 'Restricción', 'Retiro',
                               'Sustitución', 'Tipificación', 'Tracción', 'Valoración por primera vez', 'Verificación', 'Interconsulta', 'Participación en junta médica o equipo interdisciplinario', 'Cuidado intrahospitalario', 'Asistencia intrahospitalaria', 'Consulta de urgencias',
                               'Educación en salud', 'No aplica', 'Administración', 'Obtención de imágenes']
    via_abordaje_options = ['Vía abierta', 'Vía percutánea', 'Vía percutánea endoscópica', 'Vía a través de orificios naturales', 'Vía a través de orificios naturales endoscópica', 'Vía a través de orificios naturales con asistencia percutánea',
                            'Vía externa', 'No aplica']
    proposito_options = ['Diagnóstico', 'Terapéutico', 'Preventivo', 'Paliativo', 'Rehabilitativo', 'De apoyo', 'De monitoreo', 'No especifico']
    naturaleza_options = ['Quirúrgico', 'No quirúrgico', 'No aplica', 'No información']
    finalidad_options = ['Funcional', 'Estética/cosmética', 'No aplica']
    #finalidad_options = ['Funcional', 'Estética', 'Cosmética', 'Suntuaria', 'Prevención', 'Reconstrucción', 'No aplica', 'No información']
    ambito_options = ['Consulta externa', 'Urgencias', 'Hospitalización', 'Cirugía', 'Obstetricia y ginecología', 'Pediatría', 'Medicina interna', 'Cuidado critico', 'Psiquiatria y salud mental', 'Rehabilitación', 'Varios servicios', 'Sala de procedimientos', 'No especifico']
    modalidad_options = ['Intramural', 'Extramural',  'Telemedicina', 'Mixta']
    #modalidad_options = ['Intramural', 'Extramural unidad móvil', 'Extramural domiciliaria', 'Extramural jornada de salud',  'Telemedicina', 'Mixto', 'No aplica']
    invasividad_options = ['Invasivo', 'No invasivo', 'Minimamente invasivo', 'No aplica']
    riesgo_paciente_options = ['Bajo', 'Moderado', 'Alto', 'Muy alto', 'No aplica']
    dicotomia_obselencia_options = ['Sí','No']
    lateralidad_options = ['Unilateral', 'Bilateral', 'Izquierda', 'Derecha', 'No especifica', 'No aplica', 'No información']
    sexo_options = ['Masculino', 'Femenino', 'Ambos', 'Intersexo']
    extensores_options = ['Ubicación','Cuantificadores', 'Número de estructuras', 'Número de intervenciones', 'Área', 'Longitud', 'Tamaño', 'Tiempo', 'Lateralidad', 'Proximidad', 'Dirección', 'Profundidad', 'Ubicación/Localización', 'Complejidad', 'Completitud', 
                          'Sexo', 'Enfoque de la atención', 'Grupo etario', 'Orden', 'No aplica']
    tipo_dm_options = ['No invasivo', 'Invasivo', 'Activo (equipo biomédico)', 'Sobre medida', 'Como parte de una sustancia', 'Fin anticonceptivo', 'Uso desinfección/limpieza', 'No activo/imágenes dx', 'De tejidos animales o derivados', 'No aplica', 'No información']
    clase_riesgo_dm_options = ['I', 'IIa', 'IIb', 'III', 'No aplica']
    anatomia_sistemica_options = ['Sistema nervioso y función mental', 'Sistema visual', 'Sistema auditivo', 'Sistema hematopoyético o linfático', 'Sistema endocrino', 'Sistema circulatorio', 'Sistema respiratorio/voz/habla', 'Sistema digestivo', 'Sistema tegumentario', 
                                    'Sistema musculoesquelético', 'Sistema urinario', 'Sistema reproductor masculino', 'Sistema reproductor femenino', 'Otros sistemas o funciones no especificadas', 'No aplica']

    
    return render_template('formulario.html',
                            grupos_cups_options = grupos_cups_options,
                            tipo_procedimiento_naturaleza_options = tipo_procedimiento_naturaleza_options,
                            accion_ejercida_options = accion_ejercida_options, 
                            via_abordaje_options = via_abordaje_options,
                            lateralidad_options = lateralidad_options,
                            proposito_options = proposito_options,
                            naturaleza_options = naturaleza_options, 
                            invasividad_options = invasividad_options, 
                            finalidad_options = finalidad_options, 
                            dicotomia_obselencia_options = dicotomia_obselencia_options, 
                            sexo_options = sexo_options, 
                            ambito_options = ambito_options, 
                            modalidad_options = modalidad_options, 
                            riesgo_paciente_options = riesgo_paciente_options, 
                            extensores_options = extensores_options,
                            tipo_dm_options = tipo_dm_options,
                            clase_riesgo_dm_options = clase_riesgo_dm_options, 
                            anatomia_sistemica_options = anatomia_sistemica_options)

@app.route('/descargar')
def descargar():
    # Ruta para descargar el archivo Excel
    if os.path.exists(EXCEL_FILE):
        return send_file(EXCEL_FILE, as_attachment=True)
    else:
        return "El archivo no existe."
    
# Ruta para buscar en la base de datos (archivo Excel)
@app.route('/buscar_cups', methods=['POST'])
def buscar_cups():
    print("Solicitud POST recibida")  # Depuración para verificar si se recibe la solicitud
    data = request.get_json()
    CUPS = data.get('CUPS', '')

    print(type(CUPS))
    
    print(f"CUPS buscado: {CUPS}")  # Depuración del valor ingresado

    # Cargar el archivo Excel y filtrar
    try:
        df = pd.read_excel(EXCEL_FILE, dtype={'CUPS' :str})

        print(df)

        # Filtrar por la columna "ENUNCIADO CUPS Resolución 2336 de 2023"
        result = df[df["CUPS"] == CUPS ]


        # Reemplazar valores NaN con algo compatible con JSON (por ejemplo, una cadena vacía o None)
        result = result.fillna('')

        result_dict = result.to_dict(orient='records')

        print(f"Resultados encontrados: {result_dict}")  # Depuración de los resultados

        return jsonify(result_dict)
    except Exception as e:
        print(f"Error al procesar el archivo Excel: {str(e)}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
