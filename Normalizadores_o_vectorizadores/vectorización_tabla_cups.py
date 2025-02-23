import pandas as pd


archivo_excel = "TablaReferencia_CUPSRips__1.xlsx" 
df = pd.read_excel(archivo_excel)


df["Habilitado"] = df["Habilitado"].apply(lambda x: 1 if x == "SI" else 0)


df.rename(columns={"Extra_I:UsoCodigoCUP": "UsoCodigoCUP"}, inplace=True)


print(df.head())


df.to_excel("Documentos_procesados/cups_procesado.xlsx", index=False)

print("✅ Archivo procesado y guardado como 'cups_procesado.xlsx'")