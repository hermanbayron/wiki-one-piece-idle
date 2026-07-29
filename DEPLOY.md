# Despliegue en VPS

Este proyecto comparte el Caddy del VPS con otra app.

## Caddyfile obligatorio

El archivo `/opt/wiki-one-piece-idle/Caddyfile` debe conservar siempre ambos dominios:

```caddyfile
wiki-onepiece.duckdns.org {
  root * /usr/share/caddy
  encode gzip
  header {
    X-Content-Type-Options nosniff
  }
  file_server
}

casa-arte.duckdns.org {
  reverse_proxy posada-nginx:80
}
```

No desplegar un `Caddyfile` que tenga solamente la wiki, porque rompe `casa-arte.duckdns.org`.

## Antes de actualizar

```bash
cd /opt/wiki-one-piece-idle
cp Caddyfile Caddyfile.backup
git pull
docker restart wiki-one-piece-idle
```

## Verificacion despues de desplegar

```bash
cat /opt/wiki-one-piece-idle/Caddyfile
curl -I https://wiki-onepiece.duckdns.org
curl -I https://casa-arte.duckdns.org/tienda
```

Ambos dominios deben responder correctamente.

## No hacer

- No reemplazar el `Caddyfile` por uno que contenga solamente `wiki-onepiece.duckdns.org`.
- No borrar `/opt/wiki-one-piece-idle/Caddyfile` sin backup.
- No usar `docker compose down` si puede eliminar una red compartida como `caddy-proxy`.
- No levantar otro contenedor ocupando los puertos `80` y `443`.
