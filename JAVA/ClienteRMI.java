import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.util.Scanner;

public class ClienteRMI {
    public static void main(String[] args) {
        try {
            Scanner input = new Scanner(System.in);
            Registry registry = LocateRegistry.getRegistry("127.0.0.1" , 1099);
            InterfaceRemotaRMI stub = (InterfaceRemotaRMI) registry.lookup("AbcBolinhas");

            System.out.println("Digite um CPF:"); 
            String cpf = input.nextLine(); 

            System.out.println(cpf+" eh um CPF valido? " + stub.CheckCPF(cpf));
            System.out.println("3 e par: " + stub.isPar(3));
            System.out.println("100 e par: " + stub.isPar(100));


        } catch (Exception e) {
            System.err.println("! Erro no cliente: " + e.toString());
        }
    }
}