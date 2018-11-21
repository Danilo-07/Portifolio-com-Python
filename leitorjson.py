import json

dicionario = {"patche2001": "2001 - Patch Grande Costas H.O.G. Logo",
              "patche2002": "2002 - Patch Grande (Costas) H.O.G. Heritage Logo",
              "patche2003": "2003 - Patch Grande Ladies of Harley (LOH)",
              "patche2022": "2022 - Patch Pequeno H.O.G. Logo",
              "patche2023": "2023 - Patch Pequeno H.O.G. Heritage Logo",
              "patche2024": "2024 - Patch Pequeno Ladies of Harley (LOH)",
              "patche2025": "2025 - Director",
              "patche2026": "2026 - Road Captain",
              "patche2027": "2027 - Chapter Member",
              "patche2028": "2028 - Secretary",
              "patche2029": "2029 - Past Director",
              "patche2030": "2030 - Past Officer",
              "patche2031": "2031 - Activities Officer",
              "patche2033": "2033 - Assistant Director",
              "patche2034": "2034 - Life Member",
              "patche2035": "2035 - Safety Officer",
              "patche2036": "2036 - Ladies Of Harley Officer",
              "patche2037": "2037 - Photographer",
              "patche2038": "2038 - Treasurer",
              "patche2039": "2039 - Historian",
              "patche2040": "2040 - Editor",
              "patche2041": "2041 - Head Road Captain",
              "patche2042": "2042- Webmaster",
              "patche2043": "2043 - Membership Officer",
              "patche2021": "2021 - Rota 65 Cuiabá Chapter Brasil"}


def gera_pedido(resposta):
    resultado = json.loads(resposta)
    pedido = ''
    for valor in resultado:
            if (valor['name'] == 'nome'):
                nome = valor['value']
            elif (valor['name'] == 'phone'):
                telefone = valor['value']
            elif not(valor['value'] == '0'):
                pedido += '{}, na quantidade:{}.\n'.format(dicionario[valor['name']], valor['value'])

    pedido = '{} (telefone: {}) solicitou os seguintes patch(es):\n'.format(nome, telefone) + pedido

    return pedido
