# Simple inferring app using tensorflow

Note that we require our own custom built version of tensorflow.
The code isn't changed, we just compile it with `-D_GTHREAD_USE_RECURSIVE_MUTEX_INIT_FUNC=1`
to disable use of non-POSIX primitives that are not supported on musl.

To build this version, in `build_tensorflow` run `make BUILD=yes` (although it takes 2 - 3 hours).
To avoid long compile time simple `make` will download pre-compiled wheel.

## Docker

To build and run regular docker container with this app:

```bash
make container
docker run -v $(pwd)/tmp:/mnt:Z --name test-app --rm -it -p 5000:5000 test-app /bin/sh
```

To do the same in kontainer:

```bash
make kontainer
docker run --runetime=krun -v $(pwd)/tmp:/mnt:Z --name test-app --rm -it -p 5000:5000 test-app-k /bin/sh
```

## To test:

Once inside the container with the app, to run the app:

```bash
python app.py
```

It takes several seconds for the application to initialize.
Message `WARNING: This is a development server. Do not use it in a production deployment.` is normal and expected,
it it simply because the app.py uses simple developer's flask configuration.

And to test, from the host, run:

```bash
curl -s -X POST -F image=@dog2.jpg 'http://localhost:5000/predict' | jq .
```

If everything is OK, it prints something like:

```json
{
  "predictions": [
    {
      "label": "Bernese_mountain_dog",
      "probability": 0.620712161064148
    },
    {
      "label": "Appenzeller",
      "probability": 0.28114044666290283
    },
    {
      "label": "EntleBucher",
      "probability": 0.07214776426553726
    },
    {
      "label": "Border_collie",
      "probability": 0.012632192112505436
    },
    {
      "label": "Greater_Swiss_Mountain_dog",
      "probability": 0.007238826714456081
    }
  ],
  "success": true
}
```

reporting probabilities that the presented image (`dog2.jpg`) is image of the particular dog breed.

## snapshot

Run kontainer the same way as above:

```bash
docker run --runtime=krun -v /opt/kontain/bin/km_cli:/opt/kontain/bin/km_cli \
  -v $(pwd)/tmp:/mnt:rw --name test-app --rm -it -p 5000:5000 test-app /bin/sh
```

On the host, run

```bash
./test.sh
```

The script will take care of carefully measuring start time and response time, and display the difference.

Inside the kontainer, run:

```bash
/run.sh
```

The app will start, and eventually respond to the request.

To take the snapshot:

```bash
docker exec -it test-app /opt/kontain/bin/km_cli -s /tmp/km.sock
```

To show snapshot, run the

```bash
./test.sh
```

again, and then run:

```bash
/run_snap.sh
```
