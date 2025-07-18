Since lot of application uses Postgresql specially immich and Paperless. I wanted to solve the ops to manage these databases, specially automated backups and disaster recovery. 

Our Story Hero https://cloudnative-pg.io/, This operator does all the heavy lifting for us while we manage configurations. 

My Top Goals

- No Management Overhead to keep them Up.
- Backups !!!
	- Daily Full Backup.
	- Incremental Hourly or 6 hours backup.
	- Saving Backups.
		- Use R2 to save at least last 3 days backup.
		- Use Local storage Minio etc. 
	- [ ] [PG Dump Backups](https://cloudnative-pg.io/documentation/1.24/troubleshooting/#emergency-backup), Before Upgrading.
		```
		kubectl exec pg-paperless-cluster-1 -c postgres -- psql -l
		kubectl exec pg-paperless-cluster-1 -c postgres -- pg_dump -Fc -d Paperless-pgsql > Paperless-pgsql-28-11-24.dump
		kubectl exec pg-immich-cluster-1 -c postgres -- pg_dump -Fc -d postgresql_immich_pgsql > postgresql_immich_pgsql-28-11-24.dump
		```
- Able to Restore.
	- [ ] Every Week automation to test these restoration.
### Troubleshooting 

#### Disk space 

In case of backups failed, pg-wal folder keeps filing, attach a pod 

```
kubectl debug -n kube-system -it --image alpine node/$NODE -- cd /host/var/mnt/
```

Delete some unnecessary files until cluster comes ups again.


#### Permission Error 

```
{"level":"info","ts":"2025-06-14T06:32:21.391015806Z","logger":"initdb","msg":"initdb: error: could not create directory \"/var/lib/postgresql/data/pgdata\": Permission denied\n","pipe":"stderr","logging_pod":"pg-n8n-cluster-1-initdb"}
```

```
#Get Into Node and Navigate to Dir and change permission
kubectl debug -n kube-system -it --image alpine node/i1-1806-talos-worker01
Chown -R 26: tape /host/var/mnt/ssd_nvme_predator_GM 7000/cloudnative-pg/DIR/
```

#### Reset Counter 

Deleting the pod will reset the counter, However make sure you have backup.