import pathlib
import tomli
import os

path = pathlib.Path(__file__).parent / "event-consumer.toml"
with path.open(mode="rb") as fp:
    event_consumer_config = tomli.load(fp)
    PAYLOADS_FILE = os.path.join(event_consumer_config['payloads_folder'],
                                 event_consumer_config['payloads_file'])
