import pandas as pd


archivo_excel = "Base_de_conocimiento\TablaReferencia_RIPSCausaExternaVersion2__1.xlsx" 
df = pd.read_excel(archivo_excel)


df["Habilitado"] = df["Habilitado"].apply(lambda x: 1 if x == "SI" else 0)


print(df.head())


df.to_excel("Documentos_procesados/Causa_externa_procesado.xlsx", index=False)

print("✅ Archivo procesado y guardado como 'Causa_externa_procesado.xlsx'")