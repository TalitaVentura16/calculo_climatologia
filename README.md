# calculo_climatologia

Bem-vindo, este programa tem como objetivo obter dados de precipitação acumulada para um período de 306 com intervalos de 5 dias, na climatologia esse tipo de dado é denominado pêntada. 
Para a realização do projeto é utilizada a base de dados - CHIRPS, do Google Earth Engine.

**Descrição da base presente na documentação do GEE**

Grupo de Riscos Climáticos Precipitação por infravermelho com dados da estação (CHIRPS) é um conjunto de dados de precipitação quase-global de 30+ anos. CHIRPS incorpora Imagens de satélite com resolução de 0,05° com dados de estações in situ criar séries temporais de chuvas em grade para análise de tendências e sazonais monitoramento de secas.

**Informações Importantes**

Para poder realizar o uso do programa, é necessário que você tenha o Google Earth Engine configurado em seu computador. 


**Instalação do Google Earth Engine**

O Google Earth Engine é uma plataforma para análise de dados geoespaciais. Para começar a usá-lo, siga as etapas abaixo para instalar o Earth Engine Python SDK e autenticar sua conta.

Passo 1 - Configure sua conta no Google:

Antes de começar, certifique-se de ter uma conta do Google. Se você ainda não tiver, crie uma conta do Google[“https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjDr_LPkYCBAxVfpZUCHeU5DngQFnoECAYQAQ&url=https%3A%2F%2Fearthengine.google.com%2F&usg=AOvVaw1qiiFMCBGGLG3qkRo-8udO&opi=89978449”]

Passo 2 - Instalar o Earth Engine Python SDK

O Earth Engine Python SDK é uma biblioteca que permite interagir com o Google Earth Engine usando a linguagem Python. Para instalá-lo, siga estas etapas:
Abra um terminal ou prompt de comando.
Execute o seguinte comando para instalar o Earth Engine Python SDK:

      pip install earthengine-api

Passo 3 - Autenticar sua Conta

Após instalar o Earth Engine Python SDK, você precisa autenticar sua conta do Google Earth Engine. É necessário conceder permissão para poder acessar os recursos do Earth Engine. No terminal ou prompt de comando, execute o seguinte comando:

      earthengine authenticate

Vai abrir uma janela do navegador, solicitando que você faça login na sua conta do Google. Faça o login com a mesma conta que você usou para configurar o Earth Engine.

Após fazer login, você verá uma mensagem informando que a autenticação foi bem-sucedida. Você também receberá um código de autorização que você deve colar de volta no terminal.

Cole o código de autorização no terminal e pressione Enter.

Sua conta do Google Earth Engine está agora autenticada e pronta para uso. ✨

**Atenção!**

O Google Earth Engine solicita algumas informações pessoais como nome, país, justificativa para o uso (eu defini a minha como a obtenção de dados para fins acadêmicos), e instituição a qual você está associado para poder conceder acesso à ferramenta. Como sou universitária informei o nome da minha Universidade, você também pode fazer o mesmo ou definir como para fins pessoais de estudo. 
Caso você faça parte de alguma instituição de iniciativa privada para trabalho pode ser necessário a configuração de informações diferentes, com justificativas diferentes, que podem inclusive solicitar o pagamento de planos. Certifique-se de fornecer informações precisas e relevantes de acordo com o seu caso específico.


**OBS**

Caso você tenha alguma dúvida não hesite em me contatar, meu objetivo assim como o seu é aprender e obter dados 😉. 
Vamos alcançar o sucesso juntos! 🚀💪 











