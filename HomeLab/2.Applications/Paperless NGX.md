
Not using oci://ghcr.io/gabe565/charts

Because the chart doesn't support extraVolumes, extraVolumesMounts, Needed for hooking custom script in PaprlessNgx

We need to attach configmap in pod like

```
    extraVolumes:
    - name: script-volume
      configMap:
        name: paperlessngx-scripts
        defaultMode: 755
    extraVolumeMounts:
    - name: script-volume
      mountPath: /usr/src/paperless/scripts
```


While Connecting Google SSO, One Regular Login, Connect your Account with Google by Going to Paperlessngx Profile page.