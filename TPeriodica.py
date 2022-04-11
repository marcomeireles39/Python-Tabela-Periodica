# Arquivo : TPeriodica 
# Criador : Marco Aurélio
# Data : 10-04-2022

import json
import requests
from Bd import Bd_sql
from translate import Translator

class Tabela_Periodica:

    """_summary_
    classe responsavel por acessar informações da API periodic-table-api-go
    e facilitar a obtenção de dados da tabela periodica
    """
    conteudo = None
    
    Natomico = int(0)   
    def __init__(self, natomico):
        """_sumário_
        Método construtor que precisa do parametro natomico ou numero atômico do elemento
        
        Args:
            natomico (_integer_): numero atômico
        """
        self.Natomico = natomico
    
    def carregar(self):
        
        """__Sumário__
        Método responsável por se conectar a API e pegar as informações
        """
        
        r = requests.get('https://periodic-table-api.herokuapp.com/atomicNumber/{}'.format(self.Natomico))
        jon_tab = json.loads(r.text)
        self.conteudo = jon_tab
        

    def info(self):
        diciona = {"numero_atômico":self.conteudo['atomicNumber'], "massa_atômica": self.conteudo["atomicMass"],
                   "raio_atômico":self.conteudo["atomicRadius"], "ponto_ebulição":self.conteudo["boilingPoint"],          
                   "tipo_ligação":self.conteudo["bondingType"], "cor":self.conteudo["cpkHexColor"],
                   "densidade":self.conteudo["density"], "afinidade_eletrônica":self.conteudo["electronAffinity"],
                   "eletro_negatividade":self.conteudo["electronegativity"], "config_eletrônica":self.conteudo["electronicConfiguration"],
                   "grupo":self.conteudo["groupBlock"], "raio_ion":self.conteudo["ionRadius"],
                   "energia_ionização":self.conteudo["ionizationEnergy"], "ponto_fusão":self.conteudo["meltingPoint"],
                   "nome":self.conteudo["name"], "estado_oxidação":self.conteudo["oxidationStates"],
                   "estado_padrão":self.conteudo["standardState"], "simbolo":self.conteudo["symbol"],
                   "raio_van_del":self.conteudo["vanDelWaalsRadius"], "ano_descoberta":self.conteudo["yearDiscovered"]
                   }
        return diciona
    
    def to_sqlite(self, dic, cindice, cvalor):
        indice = ''
        valor = ''
        i = int(0)
        for di in dic:
            di2= Translator(to_lang="pt")
            di2 = di2.translate(dic[di])
            
            i += 1
            if (i < len(dic)):
                if (cindice == True):
                    indice +='{} text, '.format(di)
                if (cvalor == True):
                    valor += "'{}', ".format(di2)
            else:
                if (cindice == True):
                    indice +='{} text '.format(di)
                if (cvalor == True):                    
                    valor += "'{}' ".format(di2)
        
        db = Bd_sql('tabela_periodica.db','elementos') 
        db.Criar_bd(indice)
        db.Incluir_dados(valor)