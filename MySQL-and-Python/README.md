### Create a ConfigMap with the mysql init script
    
    kubectl create configmap mysql-queries-configmap --from-file=MySQL_Queries/BucketList.sql

### kubectl apply commands in order


    kubectl apply -f mysql-configmap.yml
    kubectl apply -f mysql-secret.yml 
    kubectl apply -f mysql-deployment.yml
    kubectl apply -f mysql-service.yml
    kubectl apply -f deployment.yml
    kubectl apply -f service.yml

### kubectl Port Forward

    kubectl port-forward service/my-app-service 8080:80
