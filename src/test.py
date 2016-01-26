from lib.media_server import MediaServer
from lib.media_repository import MediaRepository
from lib.saved_images import SavedImages
import time

media_repository = MediaRepository()
media_server = MediaServer(media_repository)
saved_images = SavedImages(media_server)

def run():
    saved_image = saved_images.next()
    print "%s - printed" % saved_image.media.id
    media_repository.save(saved_image.media.as_printed())

    time.sleep(3)


run()
run()
run()
run()
run()
run()
run()
run()
run()
run()
run()
run()
run()
