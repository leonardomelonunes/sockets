import java.rmi.Remote;
import java.rmi.RemoteException;

public interface InterfaceRemotaRMI extends Remote {
    boolean CheckCPF(String cpf) throws RemoteException;
    boolean isPar(int n) throws RemoteException;
}