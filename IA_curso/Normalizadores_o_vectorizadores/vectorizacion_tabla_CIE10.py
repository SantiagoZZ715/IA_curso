import pandas as pd


archivo_excel = "Base_de_conocimiento\TablaReferencia_CIE10__1.xlsx" 
df = pd.read_excel(archivo_excel)


df["HabilitadoCIE10"] = df["HabilitadoCIE10"].apply(lambda x: 1 if x == "SI" else 0)


print(df.head())


df.to_excel("Documentos_procesados/cie10_procesado.xlsx", index=False)

print("✅ Archivo procesado y guardado como 'cie10_procesado.xlsx'")