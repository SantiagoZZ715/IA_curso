import pandas as pd


archivo_excel = "Base_de_conocimiento\TablaReferencia_RIPSFinalidadConsultaVersion2__1.xlsx" 
df = pd.read_excel(archivo_excel)


df["Habilitado"] = df["Habilitado"].apply(lambda x: 1 if x == "SI" else 0)


print(df.head())


df.to_excel("Documentos_procesados/Finalidad_consulta_procesado.xlsx", index=False)

print("✅ Archivo procesado y guardado como 'Finalidad_consulta_procesado.xlsx'")