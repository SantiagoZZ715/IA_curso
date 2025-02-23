import pandas as pd


archivo_excel = "Base_de_conocimiento\TablaReferenciaPaises.xlsx" 
df = pd.read_excel(archivo_excel)

print(df.head())

df.to_excel("Documentos_procesados/Paises_procesado.xlsx", index=False)

print("✅ Archivo procesado y guardado como 'Paises_procesado.xlsx'")