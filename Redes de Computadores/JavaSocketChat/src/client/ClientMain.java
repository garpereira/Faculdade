package client;

import java.net.Socket;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.util.Scanner;

public class ClientMain {
    public static void main(String[] args) {
        try {
            Socket cliente = new Socket("172.21.219.198", 9090);

            System.out.println("Conectado ao servidor! Digite 'sair' para encerrar a conexão.");
            ObjectOutputStream output = new ObjectOutputStream(cliente.getOutputStream());
            Scanner inputCliente = new Scanner(System.in);

            // Cria um novo thread para receber mensagens do servidor
            Thread t = new Thread(new ServerHandler(cliente));
            t.start();

            while (true) {
                System.out.println("Digite uma mensagem: ");
                String mensagem = inputCliente.nextLine();
                output.writeObject(mensagem);

                if (mensagem.equals("sair")) {
                    break;
                }
            }

            inputCliente.close();
            output.close();
            cliente.close();
            System.out.println("Conexão encerrada!");
        } catch (Exception e) {
            e.printStackTrace(); // Imprime a pilha de rastreamento da exceção
        }
    }
}

class ServerHandler implements Runnable {
    private Socket cliente;

    public ServerHandler(Socket cliente) {
        this.cliente = cliente;
    }

    public void run() {
        try {
            ObjectInputStream inputServer = new ObjectInputStream(cliente.getInputStream());

            while (true) {
                String mensagemServer = inputServer.readObject().toString();
                if (mensagemServer != null) {
                    System.out.println("Mensagem recebida do Servidor: " + mensagemServer);
                }
            }
        } catch (Exception e) {
            e.printStackTrace(); // Imprime a pilha de rastreamento da exceção
        }
    }
}