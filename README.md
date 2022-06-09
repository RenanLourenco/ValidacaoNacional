# ValidacaoNacional

Feito em python, codigo do curso de validação de dados brasileiros na alura

Projeto de Validação Nacional

* Features
Validação - deve conter 11 dígitos e utilizar biblioteca de validação
Máscara - 999.999.999-99

* CNPJ 
Validação - Deve conter	14 dígitos e utilizar biblioteca de validação
Máscara - 99.999.999/0001-99

* Telefone/Celular
Validação - Deve conter de 10 a 11 caracteres (inclui código de área)
Máscara - (99)9999-9999

Parte 2

* Data e Hora 
Deve salvar o momento do cadastro
Deve retornar data e hora no formato pt-BR
Deve ser capaz de mostrar há quanto tempo um usuário está cadastrado

* CEP
Validação - Deve conter 8 dígitos
Máscara - 99999-999
Acessar WebService ViaCEP e retornar Endereço

No código, há areas para testar o código, facilitando na visualização:

Para testar a validação de telefone: variavel_objeto = TelefonesBR(variavel_telefone) # variavel_telefone é a variavel com a str do telefone.
Telefone molde: +## (##)####-#### LEMBRANDO É TELEFONE, E NÃO CELULAR

Para testar a validação de CPF,CNPJ: documento_cnpj = Documento.cria_documento(exemplo_cnpj) # exemplo_cnpj é a variavel com str do cnpj
                                     documento_cpf = Documento.cria_documento(exemplo_cpf) # exemplo_cpf é a variavel com str cpf
                                     
Para testar a validação de CEP: objeto_cep = BuscaEndereco(variavel_cep) # variavel_cep é a variavel com str do cep 

Para testar a classe de Data e Hora = variavel = Datasbr()
                                     
                                     
