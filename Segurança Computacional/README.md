# Trabalho Final

## Chat Criptografado utilizando PyQt5

Este é um aplicativo de chat criptografado desenvolvido com a biblioteca PyQt5. O aplicativo permite que os usuários se conectem a um destinatário específico fornecendo o endereço IP de destino. Cada mensagem enviada é criptografada usando os algoritmos RC4 e SDES para garantir a segurança das comunicações.

### Requisitos

Certifique-se de ter os seguintes requisitos instalados antes de executar o aplicativo:

- Python 3.x
- PyQt5

Você pode instalar as dependências necessárias usando o `pip`:

```
pip install to-requirements.txt
```

### Executando o Aplicativo

1. Clone o repositório do projeto:

```
git clone https://github.com/seu-usuario/nome-do-repositorio.git
```

2. Navegue até o diretório do projeto:

```
cd nome-do-repositorio
```

3. Execute o aplicativo:

```
python chat_app.py
```

4. O aplicativo de chat será iniciado. Insira o endereço IP do destinatário e clique no botão "Conectar".

5. Digite sua mensagem no campo de entrada de texto na parte inferior da janela e pressione Enter ou clique no botão "Enviar". Sua mensagem será criptografada e enviada ao destinatário.

6. O destinatário receberá a mensagem criptografada e será responsável por descriptografá-la e exibi-la no seu próprio chat.

### Personalização

Você pode personalizar o aplicativo de acordo com suas necessidades. Aqui estão algumas modificações que você pode considerar:

- Melhorar a interface do usuário: O PyQt5 oferece muitas opções para personalizar a aparência do aplicativo. Você pode modificar o layout, cores, estilos de botões, etc., para melhorar a experiência do usuário.

- Adicionar autenticação: Para aumentar a segurança, você pode adicionar um sistema de autenticação, como login e senha, antes de permitir que os usuários se conectem.

- Implementar outros algoritmos de criptografia: Além do RC4 e SDES, existem muitos outros algoritmos de criptografia disponíveis. Você pode explorar e implementar outros algoritmos, como AES, RSA, etc., para aumentar ainda mais a segurança das comunicações.

- Lidar com erros e exceções: Atualmente, o aplicativo não lida com erros e exceções. Você pode adicionar tratamento de erros apropriado para lidar com problemas de conexão, erros de criptografia, etc.

### Licença

Este projeto é licenciado sob a [MIT License](https://opensource.org/licenses/MIT). Sinta-se à vontade para usá-lo e modificá-lo de acordo com suas necessidades.

Espero que este aplicativo de chat criptografado seja útil para você. Lembre-se de seguir as práticas de segurança recomendadas ao lidar com informações sensíveis e ao implementar criptografia em seus próprios projetos.

Agradeço por utilizar este aplicativo e por contribuir para a comunidade de software livre. Se você tiver alguma sugestão de melhoria ou encontrar algum problema, não hesite em entrar em contato ou abrir uma issue no repositório do projeto.

Divirta-se conversando de forma segura e criptografada!

Atenciosamente,
Garpereira
