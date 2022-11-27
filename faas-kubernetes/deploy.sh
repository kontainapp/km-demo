#!/bin/bash

print_help() {
    echo "usage: $0 [ --start=NUM --count=NUM --ipv=[4|6] ] [image_name | delete]"
    echo ""
    echo "--start  start index of next pod (default 1)"
    echo "--count how many pods to create (default 1) "
    echo "--ipv Ip version (default 4)"

}

start_idx=1
pod_count=1
ipv=4

arg_count=$#
for arg in "$@"
do
   case "$arg" in
        --start=*)
            start_idx="${1#*=}"
        ;;
        --count=*)
            pod_count="${1#*=}"
        ;;
        --ipv=*)
            ipv="${1#*=}"
        ;;
        --* | -*)
            echo "unknown option ${1}"
            print_help
        ;;
        *)
            image="${1#*=}"        
        ;; 
        --help | -h)
            print_help
        ;;
    esac
    shift
done

if [ -z "$image" ]; then 
    echo "Image is required"
    exit 1
fi

if [ "$image" = "delete" ]; then 
    for (( i=$start_idx; i<=$pod_count; i++ ))
    do
        kubectl delete pod $(kubectl get pods --no-headers=true | awk '{  print $1  }' | grep sb- | \
            awk -F'-' -v start=$start_idx -v end=pod_count '{ if ($2 >= start && $2 <= end) print $0}')    
    done
    exit
fi


for (( i=$start_idx; i<=$pod_count; i++ ))
do
   yaml_str="
apiVersion: v1
kind: Pod
metadata:
  name: sb-$i-$$
  labels:
    app.kubernetes.io/name: snap-test-$i
    app: faas
spec:
    runtimeClassName: kontain
    nodeSelector:
      sandbox: kontain
    containers:
    - name: sb-pod
      image: ${image}
      imagePullPolicy: IfNotPresent
      env:
      - name: SNAP_LISTEN_PORT
        value: \"i${ipv} 8080\"
      - name: SNAP_LISTEN_TIMEOUT
        value: \"1000\"
      ports:
      - containerPort: 8080
        name: http-web-svc
    #   readinessProbe:
    #     httpGet:
    #         path: /
    #         port: 8080
    #     initialDelaySeconds: 15
    #     periodSeconds: 30
    #     failureThreshold: 1        
    #   livenessProbe:
    #     httpGet:
    #         path: /
    #         port: 8080
    #     initialDelaySeconds: 15
    #     periodSeconds: 30
    #     failureThreshold: 1        
# ---
# apiVersion: v1
# kind: Service
# metadata:
#   name: sb-$i-$$
# spec:
#   selector:
#     app.kubernetes.io/name: snap-test-$i
#   ports:
#   - name: sb-service-port
#     protocol: TCP
#     port: 8080
#     targetPort: http-web-svc
" 
    echo "$yaml_str" > dpl-$i.yaml
    kubectl apply -f dpl-$i.yaml
    rm dpl-$i.yaml
done
