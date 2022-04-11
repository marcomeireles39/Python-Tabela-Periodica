# Python Tabela Periodica
classe responsável por acessar informações da API periodic-table-api-go
e facilitar a obtenção de dados da tabela periodica e dar a opção de
criar um banco de dados sqlite para guardar todas as informações:

__arquivo TPeriodica.py__

__Contem toda a estrutura da nossa classe__

classes utilizadas

    import json - Biblioteca pra adequação do código json recebido

    import requests - Biblioteca responsável pela conexão e obtenção dos dados de retorno
    
    from Bd import Bd_sql - Essa biblioteca foi a que criei responsável por criar um banco de dados
                            com as informações que eu quero gravar no caso um banco de dados com os
                            dados obtidos sobre os elementos da tabela periodica.



__Metodos da classe__

    obj_ini.carregar() - Método responsável por carregar os dados do elemento que será feita a pesquisa.
                         A pesquisa será em com o numero atômico do elemento que será inserido quando
                         ao criar o objeto:
                            obj_ini.Tabela_Periodica(nAtomico)    
    
    obj_ini.info() - Método que retorna todos os dados do elemento químicos em um dicionário qualquer dúvida
                     estude os dados de retorno nessa classe.
    

    obj_ini.to_sqlite(dic, cindice, cvalor) - Esse método possibilita que os dados obtidos das pesquisas
                                                    sejam salvas em um banco de dados sqlite e funciona da
                                                    seguinte forma:
                        - dic - Discionario retornado da pesquisa
                        - cindice True ou False - True : Habilita a inserção do indice na tabela
                                                False : Desabilita a inserção do indice na tabela


                        - cvalor True ou False - True : Habilita a inserção dos valores na tabela
                                                False : Desabilita a inserção dos valores na tabela

__Como usar :__

        from TPeriodica import Tabela_Periodica - importa a classe Tabela_Periodica

        tp = Tabela_Periodica(2) - Instancia a classe e já insere o número atômico do elemento
        
        tp.carregar() - Carrega os dados da API externa

        elemento =tp.info() - Retorno das informações em um dicionário

        tp.to_sqlite(elemento, True, True) - caso queira pode jogar a informação em um banco de dados
                                              já criado ou que ainda não criou, caso ainda não criou
                                              observado sempre os parametros parametros de indice e valores.


__OBS:__
Os dados da biblioteca Bd.py poderam ser visto em um dos repositórios aqui criados e como atualização usei
uma biblioteca para tradução dos dados que estavam em inglês é a biblioteca https://github.com/avedensky/google-translate-python
do programador Alexey Vedensky.