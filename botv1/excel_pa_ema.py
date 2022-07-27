import pandas as pd
print('cls')
content_ids = '234567890'
content_user = 'narnia'
content_puntaje = '54'
content_msj ="jgvcy5ersvgyv fdcufvfghbv jygt"
col1 = "IDs"
col2 = "Usuario"
col3 = "Puntaje"
col4 = "Mensajes"
data = pd.DataFrame({col1:content_ids})#, col2:content_user, col3:content_puntaje, col4:content_msj})
data.to_excel('sample_data.xlsx', sheet_name='sheet1', index=False)