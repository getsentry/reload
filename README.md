# **_re:load_**

An analytics ETL for Redshift. Pairs well with [re:dash](https://github.com/getredash/redash).

## Run Server

`make dev`

## Rebuild `ra.min.js`

```
npm install
npm run build
```

## Integration testing

Start the server and point your browser to `localhost:port/client/test.html`. Check that no javascript errors were thrown.
