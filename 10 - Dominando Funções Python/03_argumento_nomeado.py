def salvar_carro(marca, modelo, ano, placa):
    print(f"Carro inserido com sucesso! {marca}-{modelo}-{ano}- {placa}")

salvar_carro("Fiat", "Palio", 1999, "ABC-1234")
salvar_carro(marca="Fiat", modelo="Uno", ano="2005", placa="FTH-5950")
salvar_carro(**{"marca":"Fiat", "modelo": "Toro", "ano": 2020, "placa":"KZU3D82"})