# tplinkreboot

Descrição

programa para rebootar roteadores TPLINKs via requests http. Essa necessidade foi pensada, pois o firmware original não possui opção para reboot programado. A ideia é utilizar um raspberry pi executando esse código no crontab. Essa necessidade se deu em função do roteador AP travar com intermitência devido a link de 100 Mbit contratado pela operadora.

Sobre o repositório

1 - analisando o código de da página de login

o arquivo login.htm é o código montado na página. esse código é carregado na raiz. não existe uma página de redirecionamento. 
o arquibo sysreboot.htm é o arquivo que possui um script que solicita confirmação a caixa de diálogo pode ser vista em login conf.jpg

Códigos python

o arquivo tplinkreboot v3 é o arquivo que estou trabalhando. eu obtenho resposta da autenticação (200) porém ao abrir o site eu não consigo fazer com que a página de reboot passe da confirmação de download gerada pelo script. 

Os outros códigos foram implementações usadas em outros equipamentos com outras páginas e mecanismos de entrada
