# we need to add a task here that can
# do the thumbnail generation in the background.
# If celery is enabled, we can use that, otherwise, we can use a thread.
# Though, I am a bit unsure that if the background job should be in this codebase
# or in the base code of the CMS.
# There needs to have a clean check in the code to ensure it is backward compatible and also
# compatible with both CMS and Intranet.

def process_thumbnail(img_file_obj_id):
    pass

