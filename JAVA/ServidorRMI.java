import java.rmi.registry.Registry;
import java.rmi.registry.LocateRegistry;
import java.rmi.server.UnicastRemoteObject;

public class ServidorRMI implements InterfaceRemotaRMI {
 
    public boolean CheckCPF(String cpf) {
        return Uteis.IsValidCPF(cpf);
    }

    public boolean isPar(int n)
    {
        System.out.println("Requisição recebida com o seguinte argumento: " + n);
        return n % 2 == 0;
    }

    public static void main(String args[]) {
        try {
            ServidorRMI obj = new ServidorRMI();
            InterfaceRemotaRMI stub = (InterfaceRemotaRMI) UnicastRemoteObject.exportObject(obj, 0);
            String refRemota = stub.toString();
            System.out.println("Stub Gerado: " + refRemota.substring(refRemota.indexOf("endpoint")));

            Registry registro = LocateRegistry.createRegistry(1099);
            refRemota = registro.toString();
            System.out.println("Registro: " + refRemota.substring(refRemota.indexOf("endpoint")));

            registro.rebind("AbcBolinhas", stub);
            System.out.println("Servidor pronto!!!");
        } catch (Exception e) {
            System.out.println("Erro no servidor:"+e.getMessage());
        }
    }
}