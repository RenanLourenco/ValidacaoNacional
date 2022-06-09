from datetime import datetime,timedelta
class DatasBr:
    def __init__(self):
        self.momento_cadastro = datetime.today()

    def __str__(self):
        return self.format_data()

    def mes_cadastro(self):
        meses = ["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]
        mes_cadastro = self.momento_cadastro.month
        return meses[mes_cadastro - 1]

    def semana_cadastro(self):
        dia_semana = ["Segunda","Terça","Quarta","Quinta","Sexta","Sábado","Domingo"]
        semana_cadastro = self.momento_cadastro.weekday()
        return dia_semana[semana_cadastro]

    def format_data(self):
        data_formatada = self.momento_cadastro.strftime("%d/%m/%Y %H:%M")
        return data_formatada

    def tempo_cadastro(self):
        temp_cadastro= (datetime.today() + timedelta(days=30)) - self.momento_cadastro
        return temp_cadastro 