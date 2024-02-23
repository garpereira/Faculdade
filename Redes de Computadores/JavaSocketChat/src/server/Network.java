package server;

import java.net.NetworkInterface;

public class Network {
    // test the network interface
    public static void main(String[] args) throws Exception {
        NetworkInterface ni = NetworkInterface.getByName("eth0");
        System.out.println("Network interface name: " + ni.getName());
        System.out.println("Network interface display name: " + ni.getDisplayName());
        System.out.println("Network interface MAC address: " + ni.getHardwareAddress());
        System.out.println("Network interface MTU: " + ni.getMTU());
        System.out.println("Network interface is loopback: " + ni.isLoopback());
        System.out.println("Network interface is up: " + ni.isUp());
        System.out.println("Network interface is virtual: " + ni.isVirtual());
    }
}
