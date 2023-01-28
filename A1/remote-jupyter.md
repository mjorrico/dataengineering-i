# How to Access Jupyter Server
 In this example, our floating IP is `130.238.29.56` and static IP is `192.168.2.21`.
## 1. Opening Appropriate Ports
1. Open port that Jupyter listens to (Defaults to 8888).
   
    ![test](asset/port-settings.png)

2. Run Jupyter server using the following command.
    ```bash
    jupyter notebook --ip=192.168.2.21
    ```
3. Access Jupyter from remote browser using floating IP.
    ```
    http://130.238.29.56:8888
    ```

## 2. Port Forwarding
1. Run Jupyter server as usual
    ```bash
    jupyter notebook
    ```
2. Two ways to forward ports
   1. Inline CLI `ssh` command. We'll forward port `8888` from server to port `1234` of local machine.
        ```bash
        ssh -i [path_to_private_key] -L 1234:localhost:8888 ubuntu@130.238.29.56
        ```
   3. The `ssh`'s `config` file. Place it under `~/.ssh/`.
        ```bash
        
        ```