#Area de Imports
from validate_docbr import CPF
from datas_br import DatasBr
from cpf_cnpj import DocCnpj,DocCpf,Documento
import requests
from acesso_cep import BuscaEndereco
import re
from telefonesBR import TelefonesBR
#Area de Testes Telefones


#Area de Testes Validação CPF

#Area de Testes Cep/Requests
meu_cep = "03645000"
objetocep = BuscaEndereco(meu_cep)
print(objetocep)
bairro = objetocep.acessa_via_cep()
print(bairro)

#Area de testes Datas
agora = DatasBr()
print(agora)



