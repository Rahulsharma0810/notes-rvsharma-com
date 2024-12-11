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

